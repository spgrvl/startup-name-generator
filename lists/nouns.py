# Nouns list was obtained from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

with open('lists/nounlist.txt', 'r') as file:
    nouns = file.read().splitlines()

def get_nouns():
    return nouns