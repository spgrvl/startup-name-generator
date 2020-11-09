from lists.config import ebird_api_key
from ebird.api import get_taxonomy
import re

def get_bird_names():
    taxonomy = get_taxonomy(ebird_api_key)
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