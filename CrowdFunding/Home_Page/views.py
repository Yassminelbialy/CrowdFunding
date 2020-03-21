from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from Project_Creation.models import Projects, Category

def content(request,*arg,**karg):
    return render(request,"Home_Page/test.html",{})
def index(request):
    #slider latest top rated project
    top_rated = Projects.objects.order_by('-created').order_by('-average_rate')[:5]
    #card of 5 latest project
    latest_projects = Projects.objects.order_by('-created')[:5]
    #Chosen by Admin
    chosen_projects = Projects.objects.filter(choosen_byAdmin = True).order_by('-created')[:5]
    # All Categories list
    categories = Category.objects.all()

    context = {
        'top_rated': top_rated,
        'latest_projects': latest_projects,
        'chosen_projects': chosen_projects,
        'categories': categories
    }

    return render(request, 'Home_Page/index.html', context)


def select_tag(request, cat_id):
    c = get_object_or_404(Category, pk=cat_id)
    category_projects = c.projects_set.all()
    context = {
        'category_name': c.name,
        'category_projects': category_projects
    }
    return render(request, 'Home_Page/category.html', context)
