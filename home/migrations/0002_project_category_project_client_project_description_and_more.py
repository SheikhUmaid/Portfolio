# Generated by Django 4.1.2 on 2022-10-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(default='aa', upload_to='project_pics'),
        ),
        migrations.AddField(
            model_name='project',
            name='section',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
