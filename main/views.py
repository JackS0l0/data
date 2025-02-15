from django.shortcuts import render
from app.utils import common_data
from contents.models import Services,Projects,Blog
def index(request):
    data=common_data()
    context={
        'title':'Home',
        'services':Services.objects.all().order_by('-date')[0:6],
        'projects':Projects.objects.all().order_by('-date')[0:6],
        'blog_big':Blog.objects.all().order_by('-date')[0:1],
        'blog':Blog.objects.all().order_by('-date')[1:7],
    }
    data.update(context)
    return render(request, 'index.html',data)