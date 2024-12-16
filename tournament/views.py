from django.shortcuts import render, redirect
from .forms import TournamentCreateForm, RegisterTournament, MatchUserForm
from .models import Tournament, Registration, Match
from siteutils.models import menu_items
from .TourLogic import StartSingleElim, createPairingsSingle
from django.http import HttpResponse


items = menu_items.objects.filter(login_logout = 'Login')

def TourHome(request): #just shows all tournaments
    TourList = Tournament.objects.all()
    
    form = TournamentCreateForm(request.POST or None)
    context = {"TourList": TourList, "form": form, "items": items}
    return render (request, "tournament/tourhome.html", context)

def TourCreate(request): #Creates a tournament record
    
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
    
    tournament = Tournament.objects.get(pk=tour_id)
    RegPlayers = Registration.objects.filter(tournament = tour_id)
    context = {"Tournament": tournament, "Players": RegPlayers, "items": items}
    return render(request, "tournament/tourdetail.html", context)

def Register(request, tour_id): #Handle registration 
    
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
    if tour.status == 'PLANNED':
        if tour.type == 'SINGLEELIM':
            startTour = StartSingleElim(tour.id)
        return redirect("/tournament/"+str(tour.id)+"/matches")
    else:
        return redirect("/tournament/"+str(tour.id)+"/matches")

def ViewMatches(request, tour_id):
     tour = Tournament.objects.get(pk=tour_id)
     PageTitle = "Round " + str(tour.current_round) + " for " + tour.title
     currentMatches = Match.objects.filter(tournament = tour, RoundNum = tour.current_round)
     context = {"items": items, "PageTitle": PageTitle, "Matches": currentMatches, "tour": tour, "RoundNum": tour.current_round}
     return render(request, "tournament/matches.html", context)

def ViewOneMatch(request, match_id):
    matchRec = Match.objects.get(pk=match_id)
    form = MatchUserForm(request.POST or None)
    PageTitle = matchRec.Player1
    context = {"Items": items, "form": form }
    if request.method == 'POST' and form.is_valid(): 
        matchRec.P1WinCount = form.cleaned_data['P1WinCount']
        matchRec.P1LoseCount = form.cleaned_data['P2WinCount']
        matchRec.P2WinCount = form.cleaned_data['P2WinCount']
        matchRec.P2LoseCount = form.cleaned_data['P1WinCount']
        matchRec.DrawCount = form.cleaned_data['DrawCount']
        matchRec.complete = True
        if matchRec.P1WinCount > matchRec.P2WinCount:
            matchRec.winner = matchRec.Player1
        elif matchRec.P1WinCount < matchRec.P2WinCount:
            matchRec.winner = matchRec.Player2
        else:
            matchRec.isDraw = True
            matchRec.winner = None
        matchRec.save()

    
    return render(request, "tournament/match.html", context)

def NextRound(request, tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    nextRound = tour.current_round + 1
    tour.current_round = nextRound
    if tour.type == 'SINGLEELIM':
        newMatches = createPairingsSingle(tour, nextRound)
    tour.save()
    return redirect("/tournament/"+str(tour.id)+"/matches")






    
    
