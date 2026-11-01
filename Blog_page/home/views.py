from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')

def feature(request):
    return render(request, 'feature.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')

def not_found(request, exception):
    return render(request, '404.html', status=404)