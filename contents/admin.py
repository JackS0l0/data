from django.contrib import admin
from .models import Projects,Services,Blog,Reviews
@admin.register(Projects)
class ProjectsControl(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
@admin.register(Services)
class ServicesControl(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
@admin.register(Blog)
class BlogControl(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
@admin.register(Reviews)
class ReviewsControl(admin.ModelAdmin):
    list_display=['partner']
    search_fields=['partner']