from django.shortcuts import render
from app.utils import common_data
from contents.models import Services,Projects
def index(request):
    data=common_data()
    context={
        'title':'Home',
        'services':Services.objects.all().order_by('-date'),
        'projects':Projects.objects.all().order_by('-date'),
    }
    data.update(context)
    return render(request, 'index.html',data)