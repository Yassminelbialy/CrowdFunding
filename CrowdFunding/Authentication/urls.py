from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required

#templates url
# app_name="auth"

urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('register',views.RegistrationView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('profile',login_required(views.ProfileView.as_view()),name='profile'),
    path('logout', views.LogoutView.as_view(),name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate')
]
