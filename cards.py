from random import randint
cards = {'heart_6' : 1, 'heart_7' : 2, 'heart_8' : 3, 'heart_9' : 4, 'heart_10' : 5,
'heart_jack' : 6, 'heart_queen' : 7, 'heart_king' : 8, 'heart_ace' :9,
'diamond_6' : 1, 'diamond_7' : 2, 'diamond_8' : 3, 'diamond_9' : 4, 'diamond_10' : 5,
'diamond_jack' : 6, 'diamond_queen' : 7, 'diamond_king' : 8, 'diamond_ace' :9,
'club_6' : 1, 'club_7' : 2, 'club_8' : 3, 'club_9' : 4, 'club_10' : 5,
'club_jack' : 6, 'club_queen' : 7, 'club_king' : 8, 'club_ace' :9,
'spade_6' : 1, 'spade_7' : 2, 'spade_8' : 3, 'spade_9' : 4, 'spade_10' : 5,
'spade_jack' : 6, 'spade_queen' : 7, 'spade_king' : 8, 'spade_ace' :9}

deck = []
for key in cards.keys():
	deck.append(key)

n = 0
while (n < 2 or n > 6):
	n = int(input('insert n: '))
kon = []
viner = []
for i in range(n):
	koll = 6
	viner1 = 0
	x1 = []
	for i in range(koll):
		x1.append(str(deck.pop(randint(0,(len(deck)-1)))))
		y = x1
#		viner1.append(cards[y])
		viner1 = viner1 + int(cards[y])			
	kon.append(x1)
	viner.append(viner1)

print(viner)
for i in range(n):
	print("user %s =" %str(i+1) , kon[i])
