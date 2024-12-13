from .models import Tournament, Registration, Match

def StartSingleElim(tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    regPlayers = Registration.objects.filter(tournament = tour)
    numPlayers = len(regPlayers)
    return 'null'