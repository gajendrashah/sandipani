from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:country_name>/", views.country, name="country"),
    path("/about/", views.aboutPage, name="about"),
    path("/service/", views.servicePage, name="service"),
    path("/contact/", views.contactPage, name="contact"),
    path("/blog/", views.blogPage, name="blog"),
    path("/quote/", views.get_quote, name="quote"),
    path('ads/', views.ads_view, name='ads'),
]