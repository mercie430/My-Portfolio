from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('portfolio/', views.service, name = 'service'),
]