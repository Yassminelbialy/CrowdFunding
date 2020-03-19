from django.forms import ModelForm
from .models import Projects, Images 
from django import forms 
from taggit.managers import TaggableManager 

categories = ( 
        ("1", "Health"), 
        ("2", "Sports"), 
        ("3", "Innovation"), 
        ("4", "Creativity"), 
        ("5", "BLABLABLA"), 
        ("6","any thing")
    ) 

class ProjectForm(ModelForm):
    title = forms.CharField()
    details = forms.Textarea()
    category = forms.ChoiceField(choices = categories)
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