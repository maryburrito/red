from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('HH', views.index, name='index'),
    path('map', views.kala, name='kala'),
    path('questions', views.question_list, name='question_list'),
    path('menstruation', TemplateView.as_view(template_name="menstruation/main.html"), name='menstruation'),
    path('menstruation/basics', TemplateView.as_view(template_name="menstruation/subpages/basics.html"), name='menstruation_basics'),
    path('obstacles', TemplateView.as_view(template_name="obstacles.html"), name='obstacles'),
    path('stigma', TemplateView.as_view(template_name="stigma.html"), name='stigma'),
    path('about', TemplateView.as_view(template_name="about.html"), name='about'),
     path('menstruation/extratips', TemplateView.as_view(template_name="menstruation/subpages/extratips.html"), name='menstruation_extratips'),
      path('menstruation/products', TemplateView.as_view(template_name="menstruation/subpages/products.html"), name='menstruation_products'),
       path('menstruation/professionals', TemplateView.as_view(template_name="menstruation/subpages/professionals.html"), name='menstruation_professionals'),
       path('', TemplateView.as_view(template_name="home.html"), name='home'),
]