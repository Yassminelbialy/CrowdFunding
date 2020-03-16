from django.shortcuts import render
from Authentication.models import Users

# Create your views here.

#profile page
def profile(request,id):
    obj=Users.objects.get(user_id=id)
    context={
        "data":obj
    }
    print(context)
    return render(request,"profile/user_profile.html",context)
