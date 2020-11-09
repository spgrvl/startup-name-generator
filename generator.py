from lists.nouns import get_nouns
from lists.birds import get_bird_names
import random

choice=True
while choice:
    print("""
    ##############################
    ### STARTUP NAME GENERATOR ###
    #                            #
    #      Select category:      #
    #      1. Nouns              #
    #      2. Bird Species       #
    #                            #
    #      Enter 0 to exit.      #
    ##############################
    """)
    choice=input("What would you like to do? ")
    if choice=="1":
        nouns = get_nouns()
        startup_name = nouns[random.randint(0,len(nouns)-1)].capitalize()
        print("\nYour startup name is", startup_name)
    elif choice=="2":
        birds = get_bird_names()
        startup_name = birds[random.randint(0,len(birds)-1)].capitalize()
        print("Your startup name is", startup_name)
    elif choice=="0":
        choice = False
    else:
        print("\nNot a valid choice, try again!")