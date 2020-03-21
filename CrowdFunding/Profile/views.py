from django.shortcuts import render
from Authentication.models import Users
from Project_Creation.models import Projects
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,redirect
from django.db.models import Sum
import re
# Create your views here.

# profile page
def profile(request,id):
    user = get_object_or_404(Users,user_id=id)
    projects= Projects.objects.filter(user_id_id=id)
    extra_info = ExtraInfo.objects.filter(User_id_id=id)
    # donation = Donation.objects.filter(user_id_id=id)
    donation=Donation.objects.values('user_id_id',"project_Id_id").annotate(Sum("amount")).filter(user_id_id=id )
    print(donation)
    projects_user_donate_for_ids=[]
    for item in donation:
        projects_user_donate_for_ids.append(item['project_Id_id'])
    projects_user_donate_for = Projects.objects.filter(id__in=projects_user_donate_for_ids)
    projects_with_amount=[]
    for project, donation in zip(projects_user_donate_for,donation):
        setattr(project, "amount", donation['amount__sum'])
        projects_with_amount.append(project)    
    context={
        "data":user,
        "projects":projects,
        "extra_info":extra_info,
        "donation":donation,
        "projects_user_donate_for": projects_user_donate_for
    }


    return render(request,"profile/user_profile.html",context)


@csrf_exempt
def edit_profile(request):
    if request.method=='POST':
        propertyName = request.POST.get('propertyName', False)
        newValue = request.POST['newValue'];
        print(propertyName)
        if(propertyName=="First_name"):
            if ' ' in newValue or len(newValue) > 8 or len(newValue) < 4:
                return HttpResponse("incorrect")
            else:
                Users.objects.filter(user_id=request.POST['id']).update(First_name=newValue)
                return HttpResponse("done")
        elif(propertyName=="Last_name"):
            if ' ' in newValue or len(newValue) > 8 or len(newValue) < 4:
                return HttpResponse("incorrect")
            else:
                Users.objects.filter(user_id=request.POST['id']).update(Last_name=newValue)
                return HttpResponse("done")
        elif(propertyName == "email"):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if re.search(regex, newValue):
                Users.objects.filter(user_id=request.POST['id']).update(email=newValue)
                return HttpResponse("done")
            else:
                return HttpResponse("incorrect")
        elif(propertyName == "phone"):
            regex = '^01[0,2,5,1]{1}[0-9]{8}'
            if re.search(regex, newValue):
                Users.objects.filter(user_id=request.POST['id']).update(phone=newValue)
                return HttpResponse("done")
            else:
                return HttpResponse("incorrect")
        elif(propertyName == "password"):
            if len(newValue) >= 6:
                Users.objects.filter(user_id=request.POST['id']).update(password=newValue)
                return HttpResponse("done")
            else:
                return HttpResponse("incorrect")
        elif(propertyName == "country"):
            ExtraInfo.objects.filter(User_id_id=request.POST['id']).update(country=newValue)
            return HttpResponse("done")
        elif(propertyName == "FB_link"):
            regex ="(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?"
            if re.search(regex, newValue):
                ExtraInfo.objects.filter(User_id_id=request.POST['id']).update(FB_link=newValue)
                return HttpResponse("done")
            else:
                return HttpResponse("incorrect")
        elif(propertyName == "Birth_day"):
            regex = '^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$'
            if re.search(regex, newValue):
                ExtraInfo.objects.filter(User_id_id = request.POST['id']).update(Birth_day= newValue)
                return HttpResponse("done")
            else:
                return HttpResponse("incorrect")
        


#addinf Extra information


def add_info(request,id):
    if request.method == 'POST':
        ExtraInfo.objects.create(
            User_id_id=id,
            country=request.POST['country'],
            FB_link=request.POST['facebook'],
            Birth_day=request.POST['birthdate']
        )

    return redirect(profile,id=id)


#remove user account
@csrf_exempt
def remove_account(request):
    if request.method == 'POST':
       id=request.POST['id'] 
       if Users.objects.filter(user_id=id,password=request.POST['password']).count():
           Users.objects.filter(user_id=id,password=request.POST['password']).delete()
           return HttpResponse("deleted")
       else:
           return HttpResponse("incorrect")
    


    

    
    
