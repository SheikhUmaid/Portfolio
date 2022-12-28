from django.shortcuts import render
from .models import Project, Contact, Testimonial

# Create your views here.



def index(request):
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    print(len(projects))
    number_of_projects = len(projects)
    hours_of_support = number_of_projects * 4
    happy_clients = number_of_projects
    hard_workers = number_of_projects * 2
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return render(request, 'index.html', {"message": "Message Sent"})
    return render(request, 'index.html', {"projects": projects, "testimonials": testimonials, "number_of_projects": number_of_projects, "hours_of_support": hours_of_support, "happy_clients": happy_clients, "hard_workers": hard_workers})



def project(request, title):
    project = Project.objects.get(title = title)
    return render(request, 'portfolio-details.html', {"project": project})