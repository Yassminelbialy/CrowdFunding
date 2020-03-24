from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Project_Creation.models import Images, Projects, Category
from Project_Creation.forms import ProjectForm, ImageForm
from Make_Donation.models import Donation
from Home_Page.models import Comments
from Authentication.models import Users
from taggit.models import Tag
from django import forms

# Create your views here.
#to test later

#@login_required
def create_project(request):
    categories = Category.objects.all().values_list("name",flat=True) 
    ImageFormSet = modelformset_factory(Images, form = ImageForm, extra = 4)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = Images.objects.none())
        if form.is_valid() and formset.is_valid():
            project = form.save(commit = False)
            if request.category in categories:
                project.category_id =  Category.objects.get(name=request.category).id

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
                    {'projectForm': form, 'formset': formset, "categories":categories}
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
      

def delete_project(request, id):
    if request.method == 'GET':
        project_deleted = Projects.objects.get(id=id)
        project_deleted_user_id = project_deleted.user_id
        project_deleted.delete()
        
        return redirect('user/Profile/%d' % (project_deleted_user_id)) 


def donate_project(request, id):
    if request.method == 'POST':
        amount = request.POST.get('donation')
        project = Projects.objects.get(id=id)
        user = project.user_id
        donation = Donation.objects.create(amount = amount, project_id = id, user_id = user)

def comment_project(request, id): 
    if request.method == 'POST':
        content = request.POST.get('content')
        project = Projects.objects.get(id=id)
        user = project.user_id
        comment = Comments.objects.create(content=content, user_id = user, project_id = project.id)
        
        
    