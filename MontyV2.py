# Monty Python Game
# By DeeAnne Doseman
# This is a simulation of the Monty Hall game from Let's Make A Deal.
# In this game, the host will show you a door with a zonk prize.  Then they will 
# offer you another door.  You can switch or keep the door offered to go for a win.

import random

def randomNumber(start,end):
    num = random.randint(start,end)
    return num
    
def game():
    print " "
    print " "
    doorWin = randomNumber(1,3)
    #doorWin = random.randint(1,3)
    # print "winning door",doorWin
    if doorWin == 1:
        doorLose = randomNumber(1,2)
        # doorLose = random.randint(1,2)
        if doorLose == 1:
            print "Zonk is behind door number #2"
            zonkDoor = 2
        else:
            print "Zonk is behind door number #3"
            zonkDoor = 3
    if doorWin == 2:
        doorLose = randomNumber(1,2)
        #doorLose = random.randint(1,2)
        if doorLose == 1:
            print "Zonk is behind door number #1"
            zonkDoor = 1
        else:
            print "Zonk is behind door number #3"
            zonkDoor = 3
    if doorWin == 3:
        doorLose = randomNumber(1,2)
        # doorLose = random.randint(1,2)
        if doorLose == 1:
            print "Zonk is behind door number #1"
            zonkDoor = 1
        else:
            print "Zonk is behind door number #2"
            zonkDoor = 2
            
    # Now Monty tells the player a door to pick
    if zonkDoor == 1:
        montyDoor = randomNumber(1,2)
        # montyDoor = random.randint(1,2)
        if montyDoor == 1:
            print "You have a chance at door #2, will you take it?"
            doorChoice = 2
        else:
            print "You have a chance at door #3, will you take it?"
            doorChoice = 3
    if zonkDoor == 2:
        montyDoor = randomNumber(1,2)
        # montyDoor = random.randint(1,2)
        if montyDoor == 1:
            print "You have a chance at door #1, will you take it?"
            doorChoice = 1
        else:
            print "You have a chance at door #3, will you take it?"
            doorChoice = 3
    if zonkDoor == 3:
        montyDoor = randomNumber(1,2)
        # montyDoor = random.randint(1,2)
        if montyDoor == 1:
            print "You have a chance at door #1, will you take it?"
            doorChoice = 1
        else:
            print "You have a chance at door #2, will you take it?"
            doorChoice = 2
    
    # print "Monty has given you:",doorChoice    
    
    # player has a choice to keep the door or switch to other door
    print " "
    print "  "
    print "Now you have a decision, do you keep the door or switch to the"
    print "other door.  Enter 1 to keep the offered door or 2 to switch doors"
    yourChoice = raw_input("What is your choice: ")
    # print "your choice:",yourChoice
    yourChoice = int(yourChoice)
    
    # keep what you offered
    if yourChoice == 1:
        if doorChoice == 1:
            picked = 1
        if doorChoice == 2:
            picked = 2
        if doorChoice == 3:
            picked = 3
            
    # switch routine       
    if yourChoice == 2:
        if zonkDoor == 1 and doorChoice == 2:
            picked = 3
        if zonkDoor == 1 and doorChoice == 3:
            picked = 2
        if zonkDoor == 2 and doorChoice == 1:
            picked = 3
        if zonkDoor == 2 and doorChoice == 3:
            picked = 1
        if zonkDoor == 3 and doorChoice == 1:
            picked = 2
        if zonkDoor == 3 and doorChoice == 2:
            picked = 1
            
    # print the users choice
    print " "
    print "You have chosen door #",picked
    print " "
            
    # Did you win?
    if picked == doorWin:
        print "Congratulations, you won the grand prize."
        winStat = 1
    else:
        print "Sorry you got zonked."
        print "The grand prize is behind door #",doorWin
        winStat = 0
    return winStat
    
win = 0
lose = 0 
howMany = int(raw_input("How many games would you like to play: "))     
for runThrough in range(howMany):
    print " "
    print "Game #",runThrough + 1
    winStat = game()
    if winStat == 1:
        win = win + 1
    else:
        lose = lose + 1
        
print " "
print "The totals for your",runThrough + 1,"games is:"
print "Wins = ",win
print "Lose = ",lose
