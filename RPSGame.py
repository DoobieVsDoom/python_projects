#!/usr/bin/env python

# Rock, Paper, Scissors Terminal Game
# DoobieVsDoom

# import statements
import random
import time

# variables
rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

# Player score: playerScore and Computer score: compScore
playerScore = 0
compScore = 0

# Function definitions
# start function
def start():
	print("Let's play a game of Rock, Paper, Scissors")
	while game():
		pass
	scores()

# game function
def game():
	player = move()
	computer = random.randint(1, 3)
	result(player, computer)
	return (playAgain())

# move function
def move():
	while True:
		player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a Move:")
		try:
			player = int(player)
			if player in (1,2,3):
				return (player)
		except ValueError:
			pass
		print("Oops! Invalid input. Please Enter 1, 2 or 3")

# result function
def result(player, computer):
	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!!!")
	time.sleep(0.5)
	print("Computer threw {0}!".format(names[computer]))
	global playerScore, compScore
	if player == computer:
		print("Tie Game!")
	else:
		if rules[player] == computer:
			print("Take a Victory Lap :)")
			playerScore += 1
		else:
			print("Computer: HA-HA-HA! Better Luck Next Time!")
			compScore += 1

# play again function
def playAgain():
	answer = input("Would you like to Play Again? [Y/N]")
	if answer in ("y", "Y", "yes", "Yes", "YES"):
		return (answer)
	else:
		print("Thank You Very Much for Playing :) Next Time.")

# scores function
def scores():
	global playerScore, compScore
	print("==== HIGH SCORES ====")
	print("Player: ", playerScore)
	print("Compter: ", compScore)

if __name__ == "__main__":
	start()