#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

class RPSGame(tk.Tk):
	def __init__(self):
		super().__init__()

		self.geometry()
		self.title("Rock, Paper, Scissors [DoobieVsDoom]")
		self.resizable(0, 0)

		# configure the grid
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=3)

		self.createGame()

		playerChoice = IntVar()
		compChoice = StringVar()
		resultSet = StringVar()
		playerChoice.set(1)
		playerScore = IntVar()
		compScore = IntVar()

	def createGame(self):
		rock = 1
		paper = 2
		scissors = 3

		names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
		rules = {rock: scissors, paper: rock, scissors:  paper}

		def start():
			while game():
				pass

		def game():
			player = playerChoice.get()
			comp = random.randint(1, 3)
			compChoice.set(names[comp])
			result(player, comp)

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

		playerLabel = ttk.Label(self, text='Player')
		playerLabel.grid(column=1, row=1, sticky=tk.W)