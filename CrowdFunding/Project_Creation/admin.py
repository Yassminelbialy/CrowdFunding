from django.contrib import admin
from .models import Projects,Images,Tags,Category
# Register your models here.
admin.site.register(Projects)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(Category)
