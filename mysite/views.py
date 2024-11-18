from django.shortcuts import render
from django.http import HttpResponse
from cards.models import Card
from decks.models import Deck, DeckEntry
from django.db.models import Count
from siteutils.models import menu_items

def index(request):
    items = menu_items.objects.all()
    card_collection = Card.objects.all() #.all is what made this work and grab all cards
    context = {"collection": card_collection, "items": items}
    return render(request, "mysite/index.html", context)