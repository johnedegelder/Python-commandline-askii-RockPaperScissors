import random
import sys
import time

# Define Some Variables
number = random.randint(1,3)
UserVal = 0
SelectedNumber = 0
run = True
Winner = "winner"

# Start up program
while run == True:
    print("Starting Game.......")
    time.sleep(1.5)
    # Home Screen
    if SelectedNumber == 0:
        print("ROCK, PAPER, SCISSORS! \nEnter: \n1 - for rules \n2 - to start game \n3 - to exit ")
        SelectedNumber =int(input("Enter your selection: "))

        # Rules
        if SelectedNumber == 1:
            print("Rock beats Scissors, Scissors beat Paper, Paper beats rock")
            User_yn = input("Do you wish to start a game now? y/n:")
            if User_yn == "y":
                SelectedNumber = 2
            else: SelectedNumber = 0
        # ACTUAL GAME
        while (SelectedNumber == 2):
            # user value selection and askii value

            print("Enter: \n R - for Rock \n P - for Paper \n S - for Scissors \n Q - to Quit")
            UserInput = str.upper(input("You Pick: "))
            if UserInput == "R":
                UserVal = 1
                RPS = "Rock"
                UserHand = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
            elif UserInput == "P":
                UserVal = 2
                RPS="Paper"
                UserHand = "     _______\n ---'   ____)____\n           ______)\n           _______)\n         _______)\n---.__________)"
            elif UserInput == "S":
                UserVal = 3
                RPS = "Scissors"
                UserHand = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
            elif UserInput == "Q":
                sys.exit(0)
            else:
                time.sleep(1.5)
                print("\nಠ__ಠ Next time...Please enter an accepted value\n")
                time.sleep(2.5)
                continue


            # computer value selection and askii value
            number = random.randint(1,3)

            # rock
            if number == 1:
                CompVal = 1
                CompCh = "Rock"
                CompHand ="  _______    \n (____   '---\n(_____)      \n(_____)      \n (____)      \n  (___)__.---"
            # Paper
            if number == 2:
                CompVal = 2
                CompCh = "Paper"
                CompHand = "      _______    \n  ___(____   '---\n (______         \n(_______         \n (_______        \n   (_________.---"
            # Scissors
            if number == 3:
                CompVal = 3
                CompCh = "Scissors"
                CompHand ="        _______    \n  _____(____   '---\n (_______          \n(___________       \n       (____)      \n        (___)__.---"


            # Who wins is determined here
            # For User Input Rock
            if UserInput == "R" and number == 1:
                Winner = "Noone"
            if UserInput == "R" and number == 2:
                Winner = "Computer"

            if UserInput == "R" and number == 3:
                Winner = "You"

            # For User Input Paper
            if UserInput == "P" and number == 1:
                Winner = "You"

            if UserInput == "P" and number == 2:
                Winner = "Noone"
            if UserInput == "P" and number == 3:
                Winner = "Computer"

            # for User Input Scissors
            if UserInput == "S" and number == 1:
                Winner = "Computer"

            if UserInput == "S" and number == 2:
                Winner = "You"
            if UserInput == "S" and number == 3:
                Winner = "Noone"

            # Print outputs

            print("You Choose " + RPS)
            print(UserHand)
            time.sleep(1.5)
            print("Computer Chooses " + CompCh)
            print(CompHand)
            time.sleep(1.5)
            print("Since you chose " + RPS + " and the Computer Choose " + CompCh + " The Winner Is " + Winner + "!!")
            time.sleep(1.5)



        # Exit code from home screen
        if SelectedNumber == 3:
            sys.exit(0)
        else:
            time.sleep(1.5)
            print("ಠ__ಠ")
            time.sleep(1.5)
            print("DO YOU LACK THE ABILITY TO FOLLOW BASIC INSTRUCTIONS??")
            time.sleep(3)
            print("you fucked up bud... you fucked up good")
            time.sleep(3)
            print("Process Terminated")
            time.sleep(1.5)
            run = False

