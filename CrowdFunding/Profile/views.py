from django.shortcuts import render
from Authentication.models import Users
from Project_Creation.models import Projects
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# profile page
def profile(request,id):
    user=Users.objects.get(user_id=id)
    projects= Projects.objects.filter(user_id_id=id)
    print(projects)
    context={
        "data":user,
        "projects":projects
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
        return HttpResponse("done")





    

    
    
