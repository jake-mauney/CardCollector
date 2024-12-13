from django.shortcuts import render, redirect
from .forms import TournamentCreateForm, RegisterTournament
from .models import Tournament, Registration, Match
from siteutils.models import menu_items
from .TourLogic import StartSingleElim
from django.http import HttpResponse

def TourHome(request): #just shows all tournaments
    TourList = Tournament.objects.all()
    items = menu_items.objects.all()
    form = TournamentCreateForm(request.POST or None)
    context = {"TourList": TourList, "form": form, "items": items}
    return render (request, "tournament/tourhome.html", context)

def TourCreate(request): #Creates a tournament record
    items = menu_items.objects.all()
    form = TournamentCreateForm(request.POST or None)
    context = {"form": form, "items": items}
    if request.method == 'POST' and form.is_valid(): 
        #sets the values
        title_form = form.cleaned_data['title']
        game_form = form.cleaned_data['game']
        format_form = form.cleaned_data['format']
        entry_fee_form = form.cleaned_data['entry_fee']
        #actually create the record
        newTour = Tournament.objects.create(title=title_form, game = game_form, format = format_form, entry_fee = entry_fee_form  )
        return redirect(TourHome) #return to view all tournaments once they create
    return render (request, "tournament/createtour.html", context)



def TourDetails(request, tour_id): #Details of tournament when we click into it from tour home
    items = menu_items.objects.all()
    tournament = Tournament.objects.get(pk=tour_id)
    RegPlayers = Registration.objects.filter(tournament = tour_id)
    context = {"Tournament": tournament, "Players": RegPlayers, "items": items}
    return render(request, "tournament/tourdetail.html", context)

def Register(request, tour_id): #Handle registration 
    items = menu_items.objects.all()
    currUser = request.user
    tournament = Tournament.objects.get(pk=tour_id)
    currentRegistration = Registration.objects.filter(tournament = tour_id, player = request.user)
    if Registration.objects.filter(tournament = tour_id, player = request.user).exists(): #if you are already registered a record will be returned and context will not contain the form for html
       context= {"Tournament": tournament,  "items": items}
    else:
        form = RegisterTournament(request.user, request.POST or None)
        if request.method == 'POST' and form.is_valid():
        #sets the values
            player_form = request.user
            deck_form = form.cleaned_data['deck']
        #actually create the record
            newReg = Registration.objects.create(player=player_form, tournament = tournament, deck = deck_form  )
            return redirect("/tournament/"+str(tournament.id))
        context = {"Tournament": tournament, "form": form, "items": items, "current": currentRegistration}
    return render(request, "tournament/register.html", context)

def StartTournament(request, tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    items = menu_items.objects.filter(login_logout = 'Login')
    PageTitle = "Matches for " + tour.title
    context = {"Items": items, "PageTitle": PageTitle}
    if tour.type == 'SINGLEELIM':
        startTour = StartSingleElim(tour.id)
        context["Matches"] = startTour
    return redirect("/tournament/"+str(tour.id)+"/matches")

def ViewMatch(request, tour_id):
     tour = Tournament.objects.get(pk=tour_id)
     items = menu_items.objects.filter(login_logout = 'LOGIN')
     PageTitle = "Matches for " + tour.title
     currentMatches = Match.objects.filter(tournament = tour, MatchNum = tour.current_match)
     context = {"items": items, "PageTitle": PageTitle, "Matches": currentMatches}
     return render(request, "tournament/match.html", context)




    
    
