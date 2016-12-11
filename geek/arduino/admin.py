from django.contrib import admin

from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    fields = ['board_model', 'discription','img','level']

admin.site.register(Card, CardAdmin)
