from django.shortcuts import render
from .models import Card


def index(request):
    #card_list = Card.objects.all()
    entry_cards = Card.objects.filter(level='entry').order_by('id')
    enhanced_cards = Card.objects.filter(level='enhanced').order_by('id')
    iot_cards = Card.objects.filter(level='internet_of_things').order_by('id')
    wearable_cards = Card.objects.filter(level='wearable').order_by('id')
    thd_cards = Card.objects.filter(level='3D_printing').order_by('id')

    return render(request,'arduino/index.html',{
        #'card_list':card_list,
        'entry_cards':entry_cards,
        'enhanced_cards':enhanced_cards,
        'iot_cards':iot_cards,
        'wearable_cards':wearable_cards,
        'thd_cards':thd_cards
    })
