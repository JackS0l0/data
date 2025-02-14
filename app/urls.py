from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main import views as mainviews
from contents import views as contentsviews
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='index'),
    path('service/<str:slug>/',contentsviews.ServicesDetailView.as_view(),name='post'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)