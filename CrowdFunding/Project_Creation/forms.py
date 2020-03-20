from django.forms import ModelForm
from .models import Projects, Images, Category
from django import forms 
from taggit.managers import TaggableManager 



categories = Category.objects.all() 


class ProjectForm(ModelForm):
    title = forms.CharField()
    details = forms.Textarea()
    category =  forms.CharField(label='What is your favorite fruit?',
                                 widget=forms.Select(choices=categories))
    tags = TaggableManager()
    max_target = forms.DecimalField(max_value = 10000000000)
    start_date = forms.DateField(widget=forms.DateInput)
    end_date = forms.DateField(widget=forms.DateInput)
    cover = forms.ImageField()
    
    class Meta: 
        model = Projects
        fields =  [  
                    'title','details',
                        'category','tags',
                        'max_target', 'start_date',
                        'end_date', 
                        'cover'
                ]

    
class ImageForm(ModelForm):
    image = forms.ImageField(label = 'Image')    
    class Meta:
        model = Images
        fields = ['image']    