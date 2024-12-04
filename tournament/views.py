from django.shortcuts import render
from .forms import TournamentCreateForm
from .models import Tournament, Registration, Match

def TourCreate(request):
    
    return render (request, "tournament/createtour.html")

def TourHome(request):
    TourList = Tournament.objects.all()
    form = TournamentCreateForm(request.POST or None)
    context = {"TourList": TourList, "form": form}
    #what to do when POST, new tournament form handler
    if request.method == 'POST' and form.is_valid():
        #sets the values
        title_form = form.cleaned_data['title']
        game_form = form.cleaned_data['game']
        format_form = form.cleaned_data['format']
        #actually create the record
        newTour = Tournament.objects.create(title=title_form, game = game_form, format = format_form  )
    return render (request, "tournament/tourhome.html", context)
