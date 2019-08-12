import json
import pandas as pd

with open("mtg_card_data.json", "r") as read_file:
    card_data = json.load(read_file)

for card in card_data.items():
    print(card[0])
    for num,field in enumerate(card[1]):
        print(num,field)
    break

s = set()
for card in card_data.values():
    s.add(card[3])
    
print(s)