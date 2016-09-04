import operator as op
from functools import reduce
from collections import Counter
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

Players = {'P1':'', 'P2':'' }

bet = []
die = 0
amount = 0
bet.append(die)
bet.append(amount)
Players['P1'] = bet

import random
roll1 = []
roll2 = []
for x in range (0, 5):
    roll1.append(random.randint(1, 6))
    roll2.append(random.randint(1, 6))
roll = roll1 + roll2
print(roll)

def isBetValid(Bet, roll):
	print(Bet[0]) 
	AllDie = [x for x in roll if x == Bet[0]]
	print(AllDie)
	return (len(AllDie) >= Bet[1])

def probLeast(xDice, totDice):
	sum = 0
	for x in range(xDice, totDice):
		sum = sum + ncr(totDice, x) * (1/6)**x*(5/6)**(totDice - x)
	return sum

freqList = Counter(roll1)
bet2 = []
		
bet2.append(int(input()))
bet2.append(int(input()))
Players['P2'] = bet2 
val = 0

while True:
	checkInRoll = freqList[Players['P2'][0]]
	print(checkInRoll)
	print(Players['P2'][0])
	val = (Players['P2'][0] - checkInRoll) if (Players['P2'][0] - checkInRoll) > 0 else 0
	prob = probLeast(val, len(roll) - checkInRoll)
	if prob < 0.5:
		isBetValid(bet, roll)
		break
	else:
		if(Players['P2'][1] + 1 <= 6):
			Players['P1'][1] = Players['P2'][1] + 1
			Players['P1'][0] = Players['P2'][0]
		else:
			Players['P1'][1] = Players['P2'][1] 
			Players['P1'][0] = Players['P2'][0] + 1
		
		print("Bot says bet is", Players['P1'][0], Players['P1'][1] )
		inp = input()
		if(inp == 'c'):
			print("is bet valid:",isBetValid(Players['P1'], roll))
			print(roll)
			break
		else:
			bet2[0] = int(input())
			bet2[1] = int(input())
			Players['P2'] = bet2 
			
		
		
	



	