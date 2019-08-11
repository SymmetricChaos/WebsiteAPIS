import json
with open("scryfall-default-cards.json", "r") as read_file:
    card_data = json.load(read_file)

print(card_data[0])

def extract_info(a):
    out = dict()
    keys = ['set','set_type','cmc','object','type_line']
    for i in a:
        print(i)
        out[i['name']] = [i[k] for k in keys]
    return out

a = extract_info(card_data)

print(a)

#just_cmc = []
#for i in card_data.values():
#    if "Token" not in i[3] and "Land" not in i[3]:
#        just_cmc.append(int(i[1]))
#print(just_cmc)