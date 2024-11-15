from django.shortcuts import render
from .models import Deck, DeckEntry
from django.http import HttpResponse #just for testing

def index(request):
    deck_collection = Deck.objects.all() #.all is what made this work and grab all cards
    context = {"collection": deck_collection}
    return render(request, "decks/index.html", context)

def detail(request, deck_id):
    entry_collection = DeckEntry.objects.filter(rel_deck=deck_id)
    context = {"collection": entry_collection}
    return render(request, "decks/detail.html", context)


