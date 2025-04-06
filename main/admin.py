from django.contrib import admin
from .models import Hero, About, AboutSection, Skills, Resume

# Register your models here.
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(AboutSection)
admin.site.register(Skills)
admin.site.register(Resume)