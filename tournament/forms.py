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

    def __init__(self, user, *args, **kwargs): #This is what ensures a user selects a deck they own. I have no idea how this works. https://tinyurl.com/36ue7wtb
        super(RegisterTournament, self).__init__(*args, **kwargs)
        self.fields['deck'].queryset = Deck.objects.filter(owner=user)