from ScryfallRequest import SFrequest
from time import sleep
import json

def extract_simple_card_data(a):
    out = dict()
    keys = ['name','released_at','set_name','set_type','mana_cost','cmc','object','type_line','id','rarity']
    for i in a['data']:
        if i['lang'] == 'en' and i['layout'] == 'normal':
            out[i['name']+"_"+i['set']] = [i[k] for k in keys]
    return out

def pages_to_file(n):

    sparse_data = dict()
    for page in range(1,n):
        J = SFrequest(f"cards?page={page}")
        dat = extract_simple_card_data(J)
        sparse_data.update(dat)
        # Pause for a moment to not overload the site
        sleep(.1)
    
    with open('mtg_card_data.json', 'w') as outfile:
        json.dump(sparse_data, outfile)
    
    
pages_to_file(1462)