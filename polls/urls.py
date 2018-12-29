from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('HH', views.index, name='index'),
    path('map', views.kala, name='kala'),
    path('questions', views.question_list, name='question_list'),
    path('menstruation', TemplateView.as_view(template_name="menstruation.html"), name='menstruation'),
    path('obstacles', TemplateView.as_view(template_name="obstacles.html"), name='obstacles'),
]