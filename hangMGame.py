#!/usr/bin/env python

# Hang Man Terminal Game
# DoobieVsDoom

# import statements
from random import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.title("Hang Man [DoobieVsDoom]")
root.resizable(0, 0)

word = 0
wordLen = 0
clue = 0

# global variables
playerScore = 0
compScore = 0

def gui():
	global word, wordLen, clue
	dictionary = ["Egypt", "Congo", "Morocco", "Ethiopia", "Botswana", "Zambia", "Swaziland"]
	word = choice(dictionary)
	wordLen = len(word)
	clue = wordLen * ['_']
	tries = 6


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
		graphicSet = graphic[hangman]
		hm_graphic.set(graphicSet)

	def game():
		wrongLetters = incorrectGuesses.get()
		letter = guessLetter()
		firstIndex = word.find(letter)
		if firstIndex == -1:
			wrongLetters += 1
			incorrectGuesses.set(wrongLetters)
		else:
			for i in range(wordLen):
				if letter == word[i]:
					clue[i] = letter
		hangedman(wrongLetters)
		clueSet=" ".join(clue)
		wordOutput.set(clueSet)
		if wrongLetters == tries:
			resultText = "Game Over! The word was " + word
			resultSet.set(resultText)
			newScore = compScore.get()
			newScore += 1
			compScore.set(newScore)
		if "".join(clue) == word:
			resultText = "You Win! The was " + word
			resultSet.set(resultText)
			newScore = playerScore.get()
			newScore += 1
			playerScore.set(newScore)

	def guessLetter():
		letter = letterGuess.get()
		letter.strip()
		letter.lower()
		return letter

	def resetGame():
		global word, wordLen, clue
		incorrectGuesses.set(0)
		hangedman(0)
		resultSet.set("")
		letterGuess.set("")
		word = choice(dictionary)
		wordLen = len(word)
		clue = wordLen * ["_"]
		newClue = " ".join(clue)
		wordOutput.set(newClue)


if __name__ == "__main__":
	root.mainloop()