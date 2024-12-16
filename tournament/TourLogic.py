from .models import Tournament, Registration, Match
import math

def StartSingleElim(tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    tour.status='IN PROGRESS'
    matchOrder = 1
    tour.current_round= matchOrder
    tour.save()
    #regPlayers = Registration.objects.filter(tournament = tour)
    #numPlayers = len(regPlayers)
    
    firstPairings = createPairingsSingle(tour, matchOrder)
    return firstPairings

#function that takes in the tour, and the match order and will create pairings without any consideration to record. Cause its single elim. Everyone has the same record. 
def createPairingsSingle(tour, run):
    regPlayers =  Registration.objects.filter(tournament = tour)
    numPlayers = len(regPlayers)
    matchCollection = []
    for player1, player2 in zip(regPlayers[::2], regPlayers[1::2]): #itterate through registered players in groups of two
        newMatch = Match.objects.create(Player1 = player1.player, Player2 = player2.player, RoundNum = 1, tournament = tour)
        run +=1
        matchCollection.append(newMatch)

    if numPlayers % 2 !=0: #check if regplayer is divisable by 2. If not then that means someone gets a bye round 1
        newBye = Match.objects.create(Player1 = regPlayers[len(regPlayers)-1].player, P1WinCount = 3, tournament = tour, RoundNum = 1, complete = True, winner = regPlayers[len(regPlayers)-1].player)
        print("This is the odd man out "+ regPlayers[len(regPlayers)-1].player.first_name +  " " +regPlayers[len(regPlayers)-1].player.last_name)
        matchCollection.append(newBye)
    else:
        print("even number of players")
    
    return matchCollection
