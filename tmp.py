#cards = {'heart_6' : 1, 'heart_7' : 2, 'heart_8' : 3, 'heart_9' : 4, 'heart_10' : 5,
#'heart_jack' : 6, 'heart_queen' : 7, 'heart_king' : 8, 'heart_ace' :9,
#'diamond_6' : 1, 'diamond_7' : 2, 'diamond_8' : 3, 'diamond_9' : 4, 'diamond_10' : 5,
#'diamond_jack' : 6, 'diamond_queen' : 7, 'diamond_king' : 8, 'diamond_ace' :9,
#'club_6' : 1, 'club_7' : 2, 'club_8' : 3, 'club_9' : 4, 'club_10' : 5,
#'club_jack' : 6, 'club_queen' : 7, 'club_king' : 8, 'club_ace' :9,
#'spade_6' : 1, 'spade_7' : 2, 'spade_8' : 3, 'spade_9' : 4, 'spade_10' : 5,
#'spade_jack' : 6, 'spade_queen' : 7, 'spade_king' : 8, 'spade_ace' :9}
#viner1 = ['club_8']

#viner1.append(cards[x1])
#print(cards[viner1[0]])
from random import randint

mast = ['heart', 'diamond', 'club', 'spade']

card = ['_6', '_7', '_8', '_9', '_10', '_jack', '_queen', '_king', '_ace']

koz = mast[randint(0,(len(mast)-1))]
print(koz)
cards = {}

for i in mast:
	znach = 0
	for j in card:
		
		ind = str(i + j)
		if i == koz:
			znach = znach + 1
			cards[ind] = znach +9
		else:
			znach = znach + 1
			cards[ind] = znach
			

print(cards)
