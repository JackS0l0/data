from django.db import models
class HeaderWall(models.Model):
    img=models.URLField('Photo',default='')
    def __str__(self):
        return f'Photo {self.id}'
    class Meta:
        verbose_name='Photo'
        verbose_name_plural='Photos'