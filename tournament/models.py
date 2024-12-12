from django.db import models
from decks.models import Deck
from playerprofile.models import Player
from django.contrib.auth.models import User

format_options = [('STANDARD', 'Standard'), ('PIONEER', 'Pioneer'), ('MODERN', 'Modern'), ('PAUPER', 'Pauper')]
tour_status_options = [('PLANNED', 'Planned'), ('IN PROCESS', 'In Process'), ("COMPLETE", "Complete"), ("CANCELLED", "Cancelled")]
class Tournament(models.Model):
    title = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    format = models.CharField(max_length=200, choices=format_options)
    status = models.CharField(choices=tour_status_options, max_length=200)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_date = models.DateField(null=True)
    runner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.title

class Registration(models.Model): #join between user deck and tournament
    player = models.ForeignKey(User, on_delete=models.PROTECT)
    deck = models.ForeignKey(Deck, on_delete=models.PROTECT)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.player) + " - " + str(self.tournament)

class Match(models.Model):
    Player1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Player1") #related name so I can use two foreign key field with Player
    Player2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Player2")
    P1WinCount = models.IntegerField() #win for each so each player can report and validation
    P2WinCount = models.IntegerField()
    P1LoseCount = models.IntegerField()
    P2LoseCount = models.IntegerField()
    DrawCount = models.IntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    MatchNum = models.IntegerField() #tracks which match this is, is it the first match or the 5th?

    def __str__(self):
        return str(self.Player1)+" - "+str(self.Player2)