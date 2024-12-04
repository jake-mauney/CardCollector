from django.db import models
from decks.models import Deck
from playerprofile.models import Player


class Tournament(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Registration(models.Model): #join between user deck and tournament
    deck = models.ForeignKey(Deck, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.player) + " - " + str(self.tournament)

class Match(models.Model):
    Player1 = models.ForeignKey(Player, on_delete=models.PROTECT)