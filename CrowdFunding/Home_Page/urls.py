from django.urls import path
from . import views

app_name = 'Home_Page'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:cat_id>',views.select_tag, name='category'),
	path('search/', views.search, name='search'),
]