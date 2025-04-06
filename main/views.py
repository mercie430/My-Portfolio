from django.shortcuts import render
from .models import Hero, About, AboutSection, Skills, Resume
# Create your views here.
def index(request):
    hero = Hero.objects.all()
    about = About.objects.first()
    aboutsection = AboutSection.objects.all()
    skill = Skills.objects.all()
    resume = Resume.objects.first()

    context = {
        'hero': hero,
        'about':about,
        'aboutsection':aboutsection,
        'skill':skill,
        'resume':resume
    }
    
    return render(request, 'index.html', context)


def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')