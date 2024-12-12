from django import forms
from .models import Tournament, Registration
from django.forms import ModelForm
from decks.models import Deck
from django.views.generic.edit import FormView

class TournamentCreateForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['title','game','format', 'entry_fee'] 


class RegisterTournament(ModelForm):

    class Meta:
        model = Registration
        fields = [  'deck']