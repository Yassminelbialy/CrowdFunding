from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Project_Creation.models import Images, Projects
from Project_Creation.forms import ProjectForm, ImageForm
from taggit.models import Tag
from django import forms

# Create your views here.
#to test later

#@login_required
def create_project(request):
    ImageFormSet = modelformset_factory(Images, form = ImageForm, extra = 4)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = Images.objects.none())
        if form.is_valid() and formset.is_valid():
            project = form.save(commit = False)
            project.user = request.user
            project.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(project = project, image = image)
                photo.save()
                form.save_m2m() #tags saving many to many 
                
            messages.success(request, "project saved!")
            return render(request, 'userProfile.html')

        else:
            print(form.errors, formset.errors)
            
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render (
                    request, 'projects/project_create.html',
                    {'projectForm': form, 'formset': formset}
                )
    
    
    
def show_project(request, id): 
    project = get_object_or_404(Projects, id = id)
    project_tags = project.tags_set.all()
    project_images=project.image_set.all()
    context = {
        "project":project, 
        "project_images":project_images, 
        "project_tags":project_tags
    }
    return render(request, 'projects/project_show.html' , context)
      
