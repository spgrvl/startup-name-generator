# Nouns list was obtained from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

def get_nouns():
    file = open('lists/nounlist.txt', 'r')
    nouns = file.read().splitlines()
    return nouns