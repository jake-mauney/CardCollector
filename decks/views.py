from django.shortcuts import render
from .models import Deck, DeckEntry
from siteutils.models import menu_items

def index(request):
    deck_collection = Deck.objects.all() #.all is what made this work and grab all cards
    items = menu_items.objects.all()
    context = {"collection": deck_collection, "items": items}
    return render(request, "decks/index.html", context)

def detail(request, deck_id):
    entry_collection = DeckEntry.objects.filter(rel_deck=deck_id)
    items = menu_items.objects.all()
    deck = Deck.objects.get(pk=deck_id)
    context = {"collection": entry_collection, "deck": deck, "items": items}
    return render(request, "decks/detail.html", context)


