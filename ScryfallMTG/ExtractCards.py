from ScryfallRequest import SFrequest
from time import sleep

def extract_info(a):
    out = dict()
    keys = ['set','set_type','cmc','object','type_line']
    for i in a['data']:
        out[i['name']] = [i[k] for k in keys]
    return out

sparse_data = dict()
for page in range(1,50):
    J = SFrequest(f"cards?page={page}")
    dat = extract_info(J)
    sparse_data.update(dat)
    # Pause for a moment to not overload the site
    sleep(.1)

for i in sparse_data.items():
    print(i)



#just_cmc = []
#for i in sparse_data.values():
#    if "Token" not in i[3] and "Land" not in i[3]:
#        just_cmc.append(int(i[1]))
#print(just_cmc)
    
#with open('OWLmatches.json', 'w') as outfile:
#    json.dump(J, outfile)