from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question


def index(request):
    return HttpResponse("Hello, Mary. This is the polls index.")

def kala(request):
    dog_names = ["Remus", "Pace", "Cassie"]
    return render(request, 'polls/map.html', {"dogs": dog_names})

def question_list(request):
    qs = Question.objects.filter(active=True)
    return render(request, "polls/question_list.html", {"questions": qs}) 

def menstruation(request):
    return render(request, "menstruation.html")