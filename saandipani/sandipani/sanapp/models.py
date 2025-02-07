from django.db import models
from tinymce.models import HTMLField
    
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    quote = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='services/')
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='about/')
    def __str__(self):
        return self.title
    
class Mission(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class Vision(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class TopDestination(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='top_destination/')
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='testimonial/')
    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = HTMLField()
    def __str__(self):
        return self.question








