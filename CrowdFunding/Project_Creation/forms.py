from django.forms import ModelForm
from .models import Projects, Images, Category
from django import forms 
from taggit.managers import TaggableManager 
from Make_Donation.models import Donation
from Home_Page.models import Comments, Report

#categories = Category.objects.all().values_list("name",flat=True) 


class ProjectForm(ModelForm):
    title = forms.CharField()
    details = forms.Textarea()
   # category =  forms.CharField(label='What is your favorite category',
    #                             widget=forms.Select(choices=categories))
    tags = TaggableManager()
    max_target = forms.DecimalField(max_value = 10000000000)
    start_date = forms.DateField(widget=forms.DateInput)
    end_date = forms.DateField(widget=forms.DateInput)
    cover = forms.ImageField()
    
    class Meta: 
        model = Projects
        fields =  [  
                    'title','details',
                        'tags',
                        'max_target', 'start_date',
                        'end_date', 
                        'cover'
                ]

    
class ImageForm(ModelForm):
    image = forms.ImageField(label = 'Image')    
    class Meta:
        model = Images
        fields = ['image']    
        
        
        
class DonationForm(ModelForm):
    amount = forms.IntegerField()
    class Meta:
        model = Donation
        fields = ['amount']
        

class ReportForm(ModelForm):
    pass 
        