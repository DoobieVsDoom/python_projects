#!/usr/bin/env python

# Hang Man Terminal Game
# DoobieVsDoom

# import statements
from random import *

# global variables
playerScore = 0
compScore = 0

# function definitions
# hanged man graphic function
def hangedman(hangman):
	graphic = [""" 
		+-----------+
		|
		|
		|
		|
		|
		=================""","""
		+-----------+
		|	|
		|	O
		|
		|
		|
		================= """,""" 
	 	+-----------+
		|	|
		|	O
		|	|
		|
		|
		=================""","""
	 	+-----------+
		|	|
		|	O
		|	|-
		|
		|
		=================""",""" 
	 	+-----------+
		|	|
		|	O
		|      -|-
		|
		|
		=================""","""
	 	+-----------+
		|	|
		|	O
		|      -|-
		|      /
		|
		=================""","""
		+-----------+
		|	|
		|	O
		|      -|-
		|      / \\
		|
		================="""]
	print(graphic[hangman])
	return (0)

# start function
def start():
	print("Let's play a Game of Hang Man -- African Countries :)")
	while game():
		pass
	scores()

# game function
def game():
	dictionary = ["Egypt", "Congo", "Morocco", "Ethiopia", "Botswana", "Zambia", "Swaziland"]
	word = choice(dictionary)
	wordLen = len(word)
	clue = wordLen * ['_']
	print("Clue: ", clue)
	tries = 6
	triedLetters = ""
	guesses = 0
	rightLetters = 0
	wrongLetters = -1
	wL = 0 # parallel counter to wrongLetters
	global compScore, playerScore

	while (wrongLetters != tries) and ("".join(clue) != word):
		letter = guessLetter()
		if len(letter) == 1 and letter.isalpha():
			if triedLetters.find(letter) != -1:
				print("You've already picked ", letter)
			else:
				triedLetters = triedLetters + letter
				firstIndex = word.find(letter)
				if firstIndex == -1:
					wrongLetters += 1
					wL += 1
					print("Sorry, ",letter," isn't what we looking for.")
				else:
					print("Well Done! ",letter," is Correct :)")
					if wrongLetters == -1:
						wrongLetters = wL
					elif wrongLetters == 0:
						wL = wrongLetters
					for i in range(wordLen):
						if letter == word[i]:
							clue[i] = letter
		else:
			print("Choose Another Letter")

		hangedman(wrongLetters)
		print(" ".join(clue))
		print("Guesses: ", triedLetters)

		if wrongLetters == tries:
			print("Game Over.")
			print("The Word was ", word)
			compScore += 1
			break
		if "".join(clue) == word:
			print("YOU WIN!! :)")
			print("The Word was ", word)
			playerScore += 1
			break
	return (playAgain())

# letter guessing function
def guessLetter():
	letter = input("Take a Guess at the Mystery Word: ")
	letter.strip()
	letter.lower()
	return (letter)

# play again function
def playAgain():
	answer = input("Would you like to Play Again? [Y/N]: ")
	if answer in ("y", "Y", "yes", "Yes", "YES"):
		return (answer)
	else:
		print("Thank You very much for Playing :) Next Time.")

# scores function
def scores():
	global playerScore, compScore
	print("==== HIGH SCORES ====")
	print("Player: ", playerScore)
	print("Computer: ", compScore)

if __name__ == "__main__":
	start()