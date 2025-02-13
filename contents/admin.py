from django.contrib import admin
from .models import Projects,Services
@admin.register(Projects)
class ProjectsControl(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
@admin.register(Services)
class ServicesControl(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']