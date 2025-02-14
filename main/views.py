from django.shortcuts import render
from app.utils import common_data
from contents.models import Services,Projects
def index(request):
    data=common_data()
    context={
        'title':'Home',
        'services':Services.objects.all().order_by('-date')[0:6],
        'projects':Projects.objects.all().order_by('-date')[0:6],
    }
    data.update(context)
    return render(request, 'index.html',data)