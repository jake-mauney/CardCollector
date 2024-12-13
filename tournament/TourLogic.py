from .models import Tournament, Registration, Match
import math

def StartSingleElim(tour_id):
    tour = Tournament.objects.get(pk=tour_id)
    regPlayers = Registration.objects.filter(tournament = tour)
    numPlayers = len(regPlayers)
    run = 1
    for player1, player2 in zip(regPlayers[::2], regPlayers[1::2]): #itterate through registered players in groups of two
        print("This is the "+ str(run)+ " run and Player 1 is "+player1.player.first_name+ " " +player1.player.last_name+" and player 2 is "+player2.player.first_name+ " " +player2.player.last_name)
        run +=1

    if numPlayers % 2 !=0: #check if regplayer is divisable by 2. If not then that means someone gets a bye round 1
        print("This is the odd man out "+ regPlayers[len(regPlayers)-1].player.first_name +  " " +regPlayers[len(regPlayers)-1].player.last_name)
    else:
        print("even number of players")
