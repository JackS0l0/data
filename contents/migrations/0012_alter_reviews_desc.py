# Generated by Django 5.1.6 on 2025-02-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_remove_reviews_img_remove_reviews_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='desc',
            field=models.TextField(default='', verbose_name='Review'),
        ),
    ]
