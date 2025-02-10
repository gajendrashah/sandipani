from django.shortcuts import render, redirect
from django.http import JsonResponse


# Create your views here.
from django.http import HttpResponse
from .models import Carousel, About, Service, Testimonial, TopDestination, FAQ, StudyCountry, Country, PopularCourse, Advertisement, QuoteForm, ExpertTeam


def indexabc(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    carousel = Carousel.objects.all()
    about = About.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    top_destinations = TopDestination.objects.all()
    faqs = FAQ.objects.all()
    countries = Country.objects.all() 
    expert_team = ExpertTeam.objects.all()
    ads = Advertisement.objects.filter(is_active=True)  
    services = Service.objects.all()
    return render(request, "sanapp/index.html", {"countries": countries,"carousel": carousel, "about": about, "services": services, "testimonials": testimonials, "top_destinations": top_destinations, "faqs": faqs, "ads": ads, "expert_team": expert_team})




    

def country(request, country_name):
    countries = Country.objects.all()
    study_country = StudyCountry.objects.filter(country__name__iexact=country_name)
    popular_courses = PopularCourse.objects.all()
    faqs = FAQ.objects.all()
    return render(request, f"sanapp/study/{country_name}.html", {"study_country": study_country, "countries": countries, "popular_courses": popular_courses, "faqs": faqs})
    
def aboutPage(request, country_name = None):
    countries = Country.objects.all()
    about = About.objects.all()
    services = Service.objects.all()
    expert_team = ExpertTeam.objects.all()
    return render(request, "sanapp/about.html", {"countries": countries, "about": about, "services": services, "expert_team": expert_team})



def servicePage(request, country_name = None):
    countries = Country.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()        
    return render(request, "sanapp/service.html", {"countries": countries, "services": services, "testimonials": testimonials})

def contactPage(request, country_name = None):
    countries = Country.objects.all()
    return render(request, "sanapp/contact.html", {"countries": countries})

def blogPage(request, country_name = None):
    countries = Country.objects.all()
    return render(request, "sanapp/blog.html", {"countries": countries})

def get_quote(request):
    ads = Advertisement.objects.filter(is_active=True)
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():

            # Process the form (e.g., save to DB, send email)
            return JsonResponse({"success": True, "message": "Your quote request has been submitted!"})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    form = QuoteForm()
    return render(request, "sanapp/getquote.html", {"form": form})

def ads_view(request):
    ads = Advertisement.objects.filter(is_active=True)
    return render(request, 'ad.html', {'ads': ads})
