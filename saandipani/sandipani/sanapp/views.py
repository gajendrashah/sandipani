from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Carousel, About, Service, Testimonial, TopDestination


def indexabc(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    carousel = Carousel.objects.all()
    about = About.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    top_destinations = TopDestination.objects.all()
    return render(request, "sanapp/index.html", {"carousel": carousel, "about": about, "services": services, "testimonials": testimonials, "top_destinations": top_destinations})





