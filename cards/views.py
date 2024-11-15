from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from decks.models import Deck, DeckEntry
from django.db.models import Count

def index(request):
    card_collection = Card.objects.all() #.all is what made this work and grab all cards
    context = {"collection": card_collection}
    return render(request, "cards/index.html", context)

def detail(request, card_id):
    card = Card.objects.get(id = card_id)
    like_cards=Card.objects.filter(name=card.name).exclude(pk=card_id)
    context = {"card_name":card.name, "card_set":card.set_code, "foil":card.foil, "set_num":card.set_num, "likeCollection":like_cards}  #passes the card name that I need to display. can comma seperate no problem. The quotes are what you referencein the html
    return render(request, "cards/detail.html", context) #tells what template to use for the specified url "detail"
