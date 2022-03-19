import random
card = range(1, 101)
card = random.sample(card, len(card))
print(card)
card_num = 2
player_num = 5
for i in range(0, player_num):
    txt = str(card[0:card_num])
    card = card[card_num:]
    file = open(str(i) + ".txt", "w")
    file.write(txt)
