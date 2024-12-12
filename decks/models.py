from django.db import models
from cards.models import Card
from django.contrib.auth.models import User

format_choice = [ ('STANDARD', 'Standard'), ('PIONEER', 'Pioneer'), ('PAUPER', 'Pauper'), ('MODERN','Modern')]
location_choice = [('MAIN', 'Mainboard'), ('SIDE', 'Sideboard')]

class Deck(models.Model):
    name = models.CharField(max_length=200)
    format = models.CharField(max_length= 10, choices=format_choice, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.name #this makes it so that when the app general references the card model it will return the name rather than just the pure object

class DeckEntry(models.Model):
    rel_card = models.ForeignKey(Card, on_delete=models.PROTECT)
    rel_deck = models.ForeignKey(Deck, on_delete=models.PROTECT)
    location = models.CharField(max_length=20, choices=location_choice)
    def __str__(self):
        return self.rel_card.name #this makes it so that when the app general references the card model it will return the name rather than just the pure object
