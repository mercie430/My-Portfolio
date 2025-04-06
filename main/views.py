from django.shortcuts import render
from .models import Hero, About, AboutSection
# Create your views here.
def index(request):
    hero = Hero.objects.all()
    about = About.objects.first()
    aboutsection = AboutSection.objects.all()

    context = {
        'hero': hero,
        'about':about,
        'aboutsection':aboutsection
    }
    
    return render(request, 'index.html', context)


def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')