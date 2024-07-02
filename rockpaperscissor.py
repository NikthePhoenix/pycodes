import random 

print("LET THE GAMES BEGIN \n ================")
print("Rock Paper Scissors")

def set_player(player):
    if(player=='rock'):
        return 1
    elif(player=='scissor'):
        return 2
    elif(player=='paper'):
        return 3
    return 0

def set_machine(machine):
    if(machine==1):
        return 'rock'
    elif(machine==2):
        return 'scissor'
    elif(machine==3):
        return 'paper'
    return 0
    

def decide_winner(machine, player):
    if(player == 0):
        print('LEARN TO SPELL')
    elif((player==1 and machine==2) or (player==2 and machine==3) or (player==3 and machine==1)):
        print('Player wins')
    elif(player==machine): 
        print('Tie')
    else: print('Machine wins')


while True:
    #Variable declaration
    player_1 = input("\nEnter your answer (rock, paper or scissor)\n")
    machine = random.randint(1,3)
    player_num = set_player(player_1)
    machine_word = set_machine(machine)

    #output
    print("Your move was : ", player_1)
    print("Machine's move was : ", machine_word)
    decide_winner(machine=machine, player=player_num)

