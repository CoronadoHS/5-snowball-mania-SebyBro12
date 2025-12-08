''' 
    Name: Snowball-Mania
    Author: Sebastien Gray
    Date: 12/5/2025
    Class: AP Computer Science Principles
    Python: 
'''

import random
import time


def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    playerList = []
    myName = input("What is your name? ")
    playerList.append(myName)
    print("Add other players (one at a time) by typing their names and hitting ENTER. Type DONE when finished.")
    nextName = input()
    while (nextName != "DONE"):
        playerList.append(nextName)
        nextName = input()
    print("Great - time to play!")
    return playerList


def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    thrower = random.choice(players)
    return thrower
    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    victim = random.choice(players)
    while (t == victim):
        victim = random.choice(players)
    return victim 
def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than 4 (60% chance), return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    hitNum = random.randint (1,10)
    if (hitNum > 4):
        return True
    else: 
        return False


def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while (len(players) > 1):
        thrower = getThrower(players)
        vitcim = getVictim(players,thrower)
        hitResult = getHitResult()

        if (hitResult == True):
            koresult = random.randint(1,2)
            if (koresult == 1):
                print(thrower + " throws at " + vitcim + " and hits, but " + vitcim + " stands strong!")
            else: 
                 print(thrower + " throws at " + vitcim + " and absolutley destroys " + vitcim + " who is out of the match!")
                 players.remove(vitcim)    
        else:
            print(thrower + " throws at " + vitcim + " but misses completely.") 
        time.sleep(3)        
    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messages
    '
    ' Return: none
    '''
    printIntro()
    # testPlayers = ["John","Taylor","Elam","Jack","Tyler","Sebastien","Collin","Aron", "Jared","landon","Mr. Yeh","Sam"]
    testPlayers = getNames()
    playSnowballFight(testPlayers)
    printOutro(testPlayers[0])


runProgram()

# testThrower = getThrower(testPlayers)
# testVictim = getVictim(testPlayers,testThrower)
# testHit = getHitResult()

# if (testHit == True):
#     print(testThrower + " throws at " + testVictim + "... and hits!")
# else:
#     print(testThrower + " throws at " + testVictim + "... and misssed!")