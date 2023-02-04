#!/usr/bin/env python
# Terminal Poker Dice Game
# DoobieVsDoom

# import statements
import random
from itertools import groupby

# rules of the game
nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine:"9", ten:"10", jack:"J", queen:"Q", king:"K", ace:"A"}

# score variables
playerScore = 0
compScore = 0

# function definitions
# start function
def start():
	print("Let's Play a Game of Terminal Poker Dice :)")
	while game():
		pass
	scores()

# game function
def game():
	print("The Computer will Help You Throw your 5 Dice...")
	throws()
	return (playAgain())

# throws function
def throws():
	rollNumber = 5
	dice = roll(rollNumber)
	dice.sort()
	for i in range(len(dice)):
		print("Dice ", i + 1, ": ", names[dice[i]])

	result = hand(dice)
	print("You Currently have", result)

	while True:
		rerolls = int(input("How Many Dice Do You Want to Throw Again? "))
		try:
			if rerolls in (1,2,3,4,5):
				break
		except ValueError:
			pass
		print("Oops! Please Enter 1, 2, 3, 4, 5")

	if rerolls == 0:
		print("You Finish with", result)
	else:
		rollNumber = rerolls
		diceRerolls = roll(rollNumber)
		diceChanges = list(range(rerolls))
		print("Enter the Number of a Dice to Reroll: ")
		iterations = 0
		while iterations < rerolls:
			iterations += 1
			while True:
				selection = int(input(" "))
				try:
					if selection in (1,2,3,4,5):
						break
				except ValueError:
					pass
				print("Oops! Please Enter 1, 2, 3, 4 or 5")
			diceChanges[iterations - 1] = selection - 1
			print("You have Changed the Dice: ", selection)
		iterations = 0
		while iterations < rerolls:
			iterations += 1
			replacement = diceRerolls[iterations - 1]
			dice[diceChanges[iterations - 1]] = replacement

		dice.sort()
		for i in range(len(dice)):
			print("Dice ",i + 1,":", names[dice[i]])

		result = hand(dice)
		print("You Finish with", result)

# roll function
def roll(rollNumber):
	numbers = range(1,7)
	dice = list(range(rollNumber))
	iterations = 0
	while iterations < rollNumber:
		iterations += 1
		dice[iterations - 1] = random.choice(numbers)
	return (dice)

# hand function
def hand(dice):
	diceHand = [len(list(group)) for key, group in groupby(dice)]
	diceHand.sort(reverse = True)
	straight1 = [1,2,3,4,5]
	straight2 = [2,3,4,5,6]

	if dice == straight1 or dice == straight2:
		return ("A Straight")
	elif diceHand[0] == 5:
		return ("Five of a Kind!")
	elif diceHand[0] == 4:
		return ("Four of a Kind!")
	elif diceHand == 3:
		if diceHand[1] == 2:
			return ("Full House!")
		else:
			return ("Three of a Kind!")
	elif diceHand[0] == 2:
		if diceHand[1] == 2:
			return ("Two Pair.")
		else:
			return ("One Pair.")
	else:
		return ("A High Card!")

# play again function
def playAgain():
	answer = input("Would You like to Play Again? [Y/N]: ")
	if answer in ("Y", "y", "Yes", "yes", "YES"):
		return (answer)
	else:
		print("Thank You for Playing :) Until Next Time!")

# scores function
def scores():
	global playerScore, compScore
	print("==== HIGH SCORES ====")
	print("Player: ", playerScore)
	print("Computer: ", compScore)

# import statement allowing code to integrate into another script
if __name__ == "__main__":
	start()