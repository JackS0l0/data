from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class Services(models.Model):
    name=models.CharField('Title',max_length=200)
    img=models.URLField('Photo',default='',null=True,blank=True)
    mini_desc=models.TextField('Mini Description',default='')
    desc=RichTextField('Description',default='')
    date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField('Slug',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
class Projects(models.Model):
    name=models.CharField('Name',max_length=200)
    img=models.URLField('Photo',default='',null=True,blank=True)
    desc=RichTextField('Description',default='')
    date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField('Slug',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'