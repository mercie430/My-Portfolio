from django.db import models

# Create your models here.
class Hero(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    work_button = models.CharField(max_length=50)
    contact_button = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hero')


    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'about')
    header = models.CharField(max_length=150)
    desc1 = models.TextField()
    desc2 = models.TextField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    email  = models.EmailField()
    occupation = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.title




























































