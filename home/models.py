
from venv import create
from django.db import models
# import reverse
from django.urls import reverse
from PIL import Image
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100, default = "")
    description = models.CharField(max_length=250, default = "")
    section = models.CharField(max_length=20, default = "")
    category = models.CharField(max_length=20,default = "")
    client = models.CharField(max_length=100,default = "")
    image1 = models.ImageField(upload_to='project_pics', default = "aa" )
    image2 = models.ImageField(upload_to='project_pics',blank = True, default = None)
    image3 = models.ImageField(upload_to='project_pics', blank=True, default= None)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])
        
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image1.path)
        if img.height>300 or img.width >300:
            output_size = (800,600)
            img.thumbnail(output_size)
            img.save(self.image1.path)
    
class Contact(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    subject = models.CharField(max_length = 250)
    message = models.TextField(max_length= 5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length = 100)
    comp = models.TextField(max_length = 5000)
    occupation = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='testimonials_pictures', default = "aa" )

    def __str__(self) -> str:
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height>300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)