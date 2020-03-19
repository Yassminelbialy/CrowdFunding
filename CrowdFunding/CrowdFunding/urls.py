"""CrowdFunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Profile import views as profile_views
from Project_Creation.views import create_project, show_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/profile/<int:id>',profile_views.profile),
<<<<<<< HEAD
    path('user/profile/edit',profile_views.edit_profile), 
    path('user/profile/addProject', create_project, name = "create_project"),  
    path('user/profile/projects/<int:id>', show_project, name = "show_project"),
=======
    path('user/profile/edit',profile_views.edit_profile),
    path('user/addExtrainformation/<int:id>', profile_views.add_info)
>>>>>>> dbb737d95f708dd760634c604521df771b225f0b
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)