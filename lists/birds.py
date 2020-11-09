import threading
import requests
import json
import re

def obtain_taxonomy():
    global taxonomy
    taxonomy_raw = requests.get('https://api.ebird.org/v2/ref/taxonomy/ebird?fmt=json').text
    taxonomy = json.loads(taxonomy_raw)

def get_bird_names():
    while type(taxonomy) == str:
        pass
    birds = set()
    for bird in taxonomy:
        try:
            entry = bird['familyComName']
            names = re.split(',| |-', entry)
            for name in names:
                if name[-1] == 's':
                    name = name[:-1]
                birds.add(name)
        except:
            pass
    return list(birds)

taxonomy = ""
taxonomy_thread = threading.Thread(target=obtain_taxonomy)
taxonomy_thread.start()