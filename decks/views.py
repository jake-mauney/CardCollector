from django.shortcuts import render
from .models import Deck, DeckEntry, Card
from siteutils.models import menu_items
from django.db.models import Count
from django.db.models import Subquery

def index(request):
    deck_collection = Deck.objects.all() #.all is what made this work and grab all cards
    items = menu_items.objects.all()
    context = {"collection": deck_collection, "items": items}
    return render(request, "decks/index.html", context)

def detail(request, deck_id):
    entry_collection = DeckEntry.objects.filter(rel_deck=deck_id)
    card_collection = Card.objects.filter(id__in=Subquery(DeckEntry.objects.filter(rel_deck=deck_id).values('id')))
    #loop through collection, if name exsist in list then up by one, if not then create/append
    items = menu_items.objects.all()
    deck = Deck.objects.get(pk=deck_id)
    context = {"collection": card_collection, "deck": deck, "items": items}
    return render(request, "decks/detail.html", context)


