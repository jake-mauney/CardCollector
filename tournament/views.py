from django.shortcuts import render
from .forms import TournamentCreateForm, RegisterTournament
from .models import Tournament, Registration, Match
from siteutils.models import menu_items

def TourCreate(request):
    items = menu_items.objects.all()
    form = TournamentCreateForm(request.POST or None)
    context = {"form": form, "items": items}
    return render (request, "tournament/createtour.html", context)

def TourHome(request):
    TourList = Tournament.objects.all()
    items = menu_items.objects.all()
    form = TournamentCreateForm(request.POST or None)
    context = {"TourList": TourList, "form": form, "items": items}
    #what to do when POST, new tournament form handler
    if request.method == 'POST' and form.is_valid():
        #sets the values
        title_form = form.cleaned_data['title']
        game_form = form.cleaned_data['game']
        format_form = form.cleaned_data['format']
        #actually create the record
        newTour = Tournament.objects.create(title=title_form, game = game_form, format = format_form  )
    return render (request, "tournament/tourhome.html", context)

def TourDetails(request, tour_id):
    items = menu_items.objects.all()
    tournament = Tournament.objects.get(pk=tour_id)
    RegPlayers = Registration.objects.filter(tournament = tour_id)
    context = {"Tournament": tournament, "Players": RegPlayers, "items": items}
    return render(request, "tournament/tourdetail.html", context)

def Register(request, tour_id):
    items = menu_items.objects.all()
    tournament = Tournament.objects.get(pk=tour_id)
    form = RegisterTournament(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #sets the values
        player_form = form.cleaned_data['player']
        deck_form = form.cleaned_data['deck']
        #actually create the record
        newReg = Registration.objects.create(player=player_form, tournament = tournament, deck = deck_form  )
    context = {"Tournament": tournament, "form": form, "items": items}
    return render(request, "tournament/register.html", context)
