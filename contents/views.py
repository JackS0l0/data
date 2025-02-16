from django.shortcuts import render
from django.views.generic import DetailView,ListView
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
class ServicesListView(ListView):
    model=Services
    template_name='list.html'
    context_object_name='services'
    paginate_by=12
    ordering=['-date']
    def get_context_data(self, **kwargs):
        context=super(ServicesListView,self).get_context_data(**kwargs)
        context['title']=f'Services - Data'
        context.update(common_data())
        return context
class ProjectsListView(ListView):
    model=Projects
    template_name='list.html'
    context_object_name='projects'
    paginate_by=12
    ordering=['-date']
    def get_context_data(self, **kwargs):
        context=super(ProjectsListView,self).get_context_data(**kwargs)
        context['title']=f'Projects - Data'
        context.update(common_data())
        return context
class BlogListView(ListView):
    model=Blog
    template_name='list.html'
    context_object_name='blog'
    paginate_by=12
    ordering=['-date']
    def get_context_data(self, **kwargs):
        context=super(BlogListView,self).get_context_data(**kwargs)
        context['title']=f'Services - Data'
        context.update(common_data())
        return context