#!/usr/bin/env python

# Rock, Paper, Scissors Terminal Game
# DoobieVsDoom

# import statements
import random
import tkinter as tk
from tkinter import ttk

# function definitions
# GUI function; all game sub-functions
def gui():

	rock = 1
	paper = 2
	scissors = 3

	names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
	rules = {rock: scissors, paper: rock, scissors: paper}

	# start function, under GUI function
	def start():
		while game():
			pass

	# game function, under GUI function
	def game():
		player = playerChoice.get()
		comp = random.randint(1, 3)
		compChoice.set(names[comp])
		result(player, comp)

	# result function, under GUI function
	def result(player, comp):
		newScore = 0
		if player == comp:
			resultSet.set("Tie Game!")
		else:
			if rules[player] == comp:
				resultSet.set("Take a Victory Lap :)")
				newScore = playerScore.get()
				newScore += 1
				playerScore.set(newScore)
			else:
				resultSet.set("Computer: HA-HA-HA! Better Luck Next Time!")
				newScore += 1
				compScore.set(newScore)

	# window, under GUI function
	rpsFrame = tk.Tk()
	rpsFrame.title("Rock, Paper, Scissor [DoobieVsDoom]")

	playerChoice = int(1)
	compChoice = str("")
	resultSet = str("")
	playerScore = int(0)
	compScore = int(0)

	rpsFrame.geometry("800x500")
	rpsFrame.columnconfigure(0, weight = 1)
	rpsFrame.columnconfigure(1, weight = 3)

	ttk.Label(rpsFrame, text='Player').grid(row = 1, column = 1, sticky=tk.W)
	ttk.Radiobutton(rpsFrame, text='Rock', variable=playerChoice, value = 1).grid(column = 1, row = 2, sticky=tk.W)
	ttk.Radiobutton(rpsFrame, text='Paper', variable=playerChoice, value = 2).grid(column = 1, row = 3, sticky=tk.W)
	ttk.Radiobutton(rpsFrame, text='Scissors', variable=playerChoice, value = 4).grid(column = 1, row = 4, sticky=tk.W)

	ttk.Label(rpsFrame, text='Computer').grid(column = 3, row = 1, sticky=tk.W)
	ttk.Label(rpsFrame, textvariable=compChoice).grid(column = 3, row = 3, sticky=tk.W)

	ttk.Button(rpsFrame, text='PLAY', command = start).grid(column = 2, row = 2)

	ttk.Label(rpsFrame, text='Score').grid(column = 1, row = 5, sticky=tk.W)
	ttk.Label(rpsFrame, textvariable=playerScore).grid(column = 1, row = 6, sticky=tk.W)

	ttk.Label(rpsFrame, text='Score').grid(column = 3, row = 5, sticky=tk.W)
	ttk.Label(rpsFrame, textvariable=compScore).grid(column = 3, row = 6, sticky=tk.W)

	ttk.Label(rpsFrame, textvariable=resultSet).grid(column = 2, row = 7)

if __name__ == "__main__":
	gui()