from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from . models import Random_Numbers
import random
import time
# Create your views here.
class NewTaskForm(forms.Form):
    """docstring ss NewTaskForm."""
    user_submitted_answer = forms.CharField(label = "Your Answer ")

def index(request):
    return render(request, "DoYourMath/index.html")

def multiplication(request):
    numbers = Random_Numbers()
    numbers.n1 = random.randint(100,999)
    numbers.n2 = random.randint(100,999)
    numbers.ans = numbers.n1 * numbers.n2
#    if numbers.ans == int(request.GET[user_submitted_answer["ans"]]):
#        return (HttpResponse("<h1> Correct</h1>"))

    return render(request, "DoYourMath/Multiplication.html",{
    "numbers" : numbers,
    "form" : NewTaskForm()
    })

def substraction(request):
    numbers = Random_Numbers()
    numbers.n1 = random.randint(100,999)
    numbers.n2 = random.randint(100,999)
    numbers.ans = numbers.n1 - numbers.n2
    return render(request, "DoYourMath/Substraction.html",{
    "numbers" : numbers,
    "form" : NewTaskForm()
    })



def addition(request):
    numbers = Random_Numbers()
    numbers.n1 = random.randint(100,999)
    numbers.n2 = random.randint(100,999)
    numbers.ans = numbers.n1 + numbers.n2
    return render(request, "DoYourMath/Addition.html",{
    "numbers" : numbers,
    "form" : NewTaskForm()
    })

def division(request):
    numbers = Random_Numbers()
    numbers.n1 = random.randint(100,999)
    numbers.n2 = random.randint(100,999)
    numbers.ans = numbers.n1 / numbers.n2

    return render(request, "DoYourMath/Division.html",{
    "numbers" : numbers,
    "form" : NewTaskForm()
    })

def answer(request,user_answer):
    return render(request, "DoYourMath/answer.html",{
    "user_answer":user_answer
    })
