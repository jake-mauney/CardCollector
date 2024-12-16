from django.db import IntegrityError
from .models import Tournament, Registration, Match
import math

def StartSingleElim(tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    tour.status='IN PROGRESS'
    round = 1
    tour.current_round = round
    tour.save()
    #regPlayers = Registration.objects.filter(tournament = tour)
    #numPlayers = len(regPlayers)
    
    firstPairings = createPairingsSingle(tour, round)
    return firstPairings

#function that takes in the tour, and the match order and will create pairings without any consideration to record. Cause its single elim. Everyone has the same record. 
def createPairingsSingle(tour, run):
    if run == 1:
        regPlayers =  Registration.objects.filter(tournament = tour)
        numPlayers = len(regPlayers)
        matchCollection = []
        for player1, player2 in zip(regPlayers[::2], regPlayers[1::2]): #itterate through registered players in groups of two
            newMatch = Match.objects.create(Player1 = player1.player, Player2 = player2.player, RoundNum = 1, tournament = tour)
            matchCollection.append(newMatch)

        if numPlayers % 2 !=0: #check if regplayer is divisable by 2. If not then that means someone gets a bye round 1
            newBye = Match.objects.create(Player1 = regPlayers[len(regPlayers)-1].player, P1WinCount = 3, tournament = tour, RoundNum = 1, complete = True, winner = regPlayers[len(regPlayers)-1].player)
            print("This is the odd man out "+ regPlayers[len(regPlayers)-1].player.first_name +  " " +regPlayers[len(regPlayers)-1].player.last_name)
            matchCollection.append(newBye)
        else:
            print("even number of players IN THE FIRST RUN")
    else: #users winner cause thats the relevant person from that last match which is what this is working with. 
        players = Match.objects.filter(tournament = tour, RoundNum = run-1)
        numPlayers = len(players)
        matchCollection = []
        newMatch = None
        for player1, player2 in zip(players[::2], players[1::2]):
            try:
                newMatch = Match.objects.create(Player1 = player1.winner, Player2 = player2.winner, RoundNum = run, tournament = tour)
            except IntegrityError as e:
                print(e)
            matchCollection.append(newMatch)
            print("HEY YOU GOT TO WHERE YOU WANT MATCH RECORD NOT SAVING")
        if numPlayers % 2 !=0: #check if regplayer is divisable by 2. If not then that means someone gets a bye round 1
            newBye = Match.objects.create(Player1 = players[len(players)-1].winner, P1WinCount = 3, tournament = tour, RoundNum = 1, complete = True, winner = players[len(players)-1].player)
            print("This is the odd man out "+ players[len(players)-1].winner.first_name +  " " +players[len(regPlayers)-1].winner.last_name)
            matchCollection.append(newBye)
        else:
            print("even number of players")
    return matchCollection
