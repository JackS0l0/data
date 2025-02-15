from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Services,Projects,Blog
from app.utils import common_data
class ServicesDetailView(DetailView):
    model=Services
    template_name='post.html'
    context_object_name='services'
    def get_context_data(self, **kwargs):
        context=super(ServicesDetailView,self).get_context_data(**kwargs)
        context['title']=self.object.name
        context.update(common_data())
        return context
class ProjectsDetailView(DetailView):
    model=Projects
    template_name='post.html'
    context_object_name='projects'
    def get_context_data(self, **kwargs):
        context=super(ProjectsDetailView,self).get_context_data(**kwargs)
        context['title']=self.object.name
        context.update(common_data())
        return context
class BlogDetailView(DetailView):
    model=Blog
    template_name='post.html'
    context_object_name='blog'
    def get_context_data(self, **kwargs):
        context=super(BlogDetailView,self).get_context_data(**kwargs)
        context['title']=self.object.name
        context.update(common_data())
        return context