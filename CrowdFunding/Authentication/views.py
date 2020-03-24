from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib import messages
# from validate_email import validate_email
# from django.core.validators import validate_email
# from .validators import validate_even
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes , force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from Authentication.forms import UserForm 

from django.contrib.auth import authenticate , login ,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import uuid

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'auth/register.html',context={
                                               'user_form':user_form,
                                               'profile_form':profile_form,
                                               'registered':registered
                                            })



class RegistrationView(View):
    def get(self,request):
        return render(request,'auth/register.html')

    def post(self,request):
        context = {
            'data':request.POST,
            'has_error':False
        }

        email =request.POST.get('email')
        username =request.POST.get('fname')
        full_name =request.POST.get('lname')
        password =request.POST.get('password')
        password2 =request.POST.get('password2')
        # phone=request.POST.get('phone')

        if len(password) < 6:
            messages.add_message(request,messages.ERROR,'password should at least 6 characters')
            context['has_error']=True
        if password != password2:
            messages.add_message(request,messages.ERROR,'password dont match')
            context['has_error']=True

        if email=='':
            messages.add_message(request,messages.ERROR,'please provide a vaild email')
            context['has_error']=True
        try:
            if User.objects.get(email=email):
                messages.add_message(request,messages.ERROR,'email is taken please enter another email')
                context['has_error']=True
        except Exception as identifier:
            pass
        try:
            if User.objects.get(username=username):
                messages.add_message(request,messages.ERROR,'username is taken please enter another username')
                context['has_error']=True
        except Exception as identifier:
            pass

        if context['has_error']:
            return render(request,'auth/register.html',context,status=400)

        user=User.objects.create_user(username=username,email=email)
        user.set_password=password
        user.first_name=username
        user.last_name=full_name
        user.is_active=False

        user.save()

        
        current_site = get_current_site(request)
        email_subject = 'Activate your account'
        message=render_to_string('auth/activate.html',
            {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)

            }
        )
        email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
            
        )
        email_message.send()

        messages.add_message(request,messages.SUCCESS,'account created successfully')

        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == '':
            messages.add_message(request, messages.ERROR, 'email are required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR, 'Password is required')
            context['has_error'] = True
        
        user = authenticate(email=email, password=password)
        if not context['has_error'] and not user:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True
        if context['has_error']:
             return render(request, 'auth/login.html', context=context, status=401)
        login(request, user)
        return redirect('profile')
        return redirect(settings.LOGIN_REDIRECT_URL)

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            
            messages.add_message(request,messages.SUCCESS,'account activated successfull')
            return redirect('login')
        return render(request,'auth/activate_failed.html',status=401)
class ProfileView(View):
    def get(self,request):
        return render(request,'profile.html')

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have successfully logged out')
        return redirect('login')
