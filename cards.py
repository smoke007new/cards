from random import randint

suit = ['heart', 'diamond', 'club', 'spade']

card = ['_6', '_7', '_8', '_9', '_10', '_jack', '_queen', '_king', '_ace']

trump = suit[randint(0,(len(suit)-1))] #random suit

cards = {}
#weight card generation
for i in suit:
	weight = 0
	for j in card:
		
		ind = str(i + j)
		if i == trump:
			weight = weight + 1
			cards[ind] = weight +9
		else:
			weight = weight + 1
			cards[ind] = weight
#deck mixing
deck = []
for key in cards.keys():
	deck.append(key)
#check on the number of players
n = 0
while (n < 2 or n > 6):
	n = int(input('enter the number of players: '))
game = []	#handing over cards
vinner = []	#card weight
for i in range(n):
	quantity = 6
	vinner1 = 0
	x1 = []
	for i in range(quantity):
		x1.append(str(deck.pop(randint(0,(len(deck)-1)))))
		
		if x1[i] == trump:
			vinner1 = vinner1 + cards[x1[i]] + 9	#trump test
		else:
			vinner1 = vinner1 + cards[x1[i]]
	game.append(x1)
	vinner.append(vinner1)

print('trump:', trump)
#hand printing
for i in range(n):
	print("player %s =" %str(i+1) , game[i])
#determination of the winner
vinner_index = vinner.index(max(vinner))
print('better cards player %s, card: ' %str(vinner_index + 1), game[vinner_index])