import json
import numpy as np
import matplotlib.pyplot as plt

with open("mtg_card_data.json", "r") as read_file:
    card_data = json.load(read_file)

names = []
cmcs = []

for card in card_data.values():
    if "Land" not in card[7]:
        if "funny" not in card[3]:
            if card[0] not in names:
                names.append(card[0])
                cmcs.append(card[5])

print(np.mean(cmcs))
H = np.histogram(cmcs)

plt.scatter([i for i in range(10)],H[0])