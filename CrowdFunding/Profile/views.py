from django.shortcuts import render
<<<<<<< HEAD
from Authentication.models import Users
from Project_Creation.models import Projects
=======
from Authentication.models import Users 
from Project_Creation.models import Projects
from Make_Donation.models import Donation
from .models import ExtraInfo
>>>>>>> dbb737d95f708dd760634c604521df771b225f0b
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,redirect
from django.db.models import Sum


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
        propertyName=request.POST['propertyName']
        print(propertyName)
        if(propertyName=="First_name"):
            Users.objects.filter(user_id=request.POST['id']).update(First_name=request.POST['newValue'])
        elif(propertyName=="Last_name"):
            Users.objects.filter(user_id=request.POST['id']).update(Last_name=request.POST['newValue'])
        elif(propertyName == "email"):
            Users.objects.filter(user_id=request.POST['id']).update(email=request.POST['newValue'])
        elif(propertyName == "phone"):
            Users.objects.filter(user_id=request.POST['id']).update(phone=request.POST['newValue'])
            print(request.POST['newValue'])
        elif(propertyName == "password"):
            Users.objects.filter(user_id=request.POST['id']).update(password=request.POST['newValue'])
        elif(propertyName == "country"):
            ExtraInfo.objects.filter(User_id_id=request.POST['id']).update(country=request.POST['newValue'])
        elif(propertyName == "FB_link"):
            ExtraInfo.objects.filter(User_id_id=request.POST['id']).update(FB_link=request.POST['newValue'])
        elif(propertyName == "Birth_day"):
            ExtraInfo.objects.filter(User_id_id = request.POST['id']).update(Birth_day= request.POST['newValue'])
        return HttpResponse("done")


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
    


    

    
    
