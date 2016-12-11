from django.shortcuts import render
from .models import Card


def index(request):
    card_list = Card.objects.all()
    return render(request,'arduino/index.html',{'card_list':card_list})
