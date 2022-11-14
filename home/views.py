from django.shortcuts import render
from .models import Project, Contact, Testimonial

# Create your views here.



def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return render(request, 'index.html', {"message": "Message Sent"})
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {"projects": projects, "testimonials": testimonials})





def project(request, title):
    project = Project.objects.get(title = title)
    return render(request, 'portfolio-details.html', {"project": project})