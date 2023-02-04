#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.geometry("400x200")
root.title("Rock, Paper, Scissors [DoobieVsDoom]")
root.resizable(0, 0)

rock = 1
paper = 2
scissors = 3
# rules of the game
names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}
# player and computer score
playerScore = 0
compScore = 0

def select(option):
	if option == 'Rock':
		player = 1
		comp = random.randint(1 , 3)
	elif option == 'Paper':
 		player = 2
 		comp = random.randint(1 , 3)
	elif option == 'Scissors':
		player = 3
		comp = random.randint(1 , 3)

	# compText function
	def compClass(comp):
		if comp == 1:
			compText = 'Rock'
		elif comp == 2:
			compText = 'Paper'
		elif comp == 3:
			compText = 'Scissors'
		return (compText)

	compLabel = ttk.Label(root, text='== COMPUTER ==')
	compLabel.grid(column=0, row=7, sticky=tk.N, padx=150)
	compTextBtn = ttk.Button(root, text=compClass(comp))
	compTextBtn.grid(column=0, row=8, sticky=tk.N, padx=150)

	global playerScore, compScore
	if player == comp:
		report = ttk.Label(root, text='==TIE GAME!==')
		report.grid(column=0, row=10, sticky=tk.N, padx=150)
	elif rules[player] == comp:
		report = ttk.Label(root, text="==VICTORY!!!==")
		report.grid(column=0, row=10, sticky=tk.N, padx=150)
		playerScore += 1
	else:
		report = ttk.Label(root, text='COMPUTER WINS')
		report.grid(column=0, row=10, sticky=tk.N, padx=150)
		compScore += 1

	psLabel = ttk.Label(root, text='PLAYER SCORE:')
	psLabel.grid(column=0, row=11, sticky=tk.SW, padx=15)
	psEntry = ttk.Label(root, text=playerScore)
	psEntry.grid(column=0, row=12, sticky=tk.SW, padx=5)

	csLabel = ttk.Label(root, text='COMPUTER SCORE:')
	csLabel.grid(column=0, row=11, sticky=tk.SE, padx=15)
	csEntry = ttk.Label(root, text=compScore)
	csEntry.grid(column=0, row=12, sticky=tk.SE, padx=5)

# Outside SELECT function
playerLabel = ttk.Label(root, text='== PLAYER ==')
playerLabel.grid(column=0, row=0, sticky=tk.N, padx=150)	

rBtn = ttk.Button(root, text='Rock', command=lambda: select('Rock'))
rBtn.grid(column=0, row=1, sticky=tk.N, padx=150)
pBtn = ttk.Button(root, text='Paper', command=lambda: select('Paper'))
pBtn.grid(column=0, row=2, sticky=tk.N, padx=150)
sBtn = ttk.Button(root, text='Scissors', command=lambda: select('Scissors'))
sBtn.grid(column=0, row=3, sticky=tk.N, padx=150)

root.mainloop()