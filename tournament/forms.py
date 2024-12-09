from django import forms
from .models import Tournament, Registration
from django.forms import ModelForm

class TournamentCreateForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['title','game','format']

class RegisterTournament(ModelForm):
    class Meta:
        model = Registration
        fields = [ 'player', 'deck']
