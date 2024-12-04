from django import forms
from .models import Tournament
from django.forms import ModelForm

class TournamentCreateForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['title','game','format']
