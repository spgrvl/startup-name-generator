from lists.nouns import get_nouns
from lists.birds import get_bird_names
from lists.colors import get_colors
from domain_checker import check_availability, quit_webdriver
import random

def find_name(name_type):
    if name_type == "noun":
        names = get_nouns()
    elif name_type == "bird":
        names = get_bird_names()
    domain_available = False
    while domain_available == False:
        startup_name = names[random.randint(0,len(names)-1)].capitalize()
        domain_available = check_availability(startup_name.lower())
        if domain_available == False:
            colors = get_colors()
            startup_name = colors[random.randint(0,len(colors)-1)].capitalize() + startup_name
            domain_available = check_availability(startup_name.lower())
    print("\nYour startup name is {} and domain {}.com is available!".format(startup_name, startup_name.lower()))

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
        find_name('noun')
    elif choice=="2":
        find_name('bird')
    elif choice=="0":
        choice = False
    else:
        print("\nNot a valid choice, try again!")
quit_webdriver()