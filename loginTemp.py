#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.geometry("260x100")
		self.title('Login [DoobieVsDoom]')
		self.resizable(0, 0)

		# configure the grid
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=3)

		self.create_widgets()

	def create_widgets(self):
		# username
		usernameLabel = ttk.Label(self, text='Username:')
		usernameLabel.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)

		usernameEntry = ttk.Entry(self)
		usernameEntry.grid(column=0, row=0, sticky=tk.W, padx=80, pady=5)

		userPassword = ttk.Label(self, text='Password:')
		userPassword.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

		passwordEntry = ttk.Entry(self, show="*")
		passwordEntry.grid(column=0, row=1, sticky=tk.W, padx=80, pady=5)

		loginButton = ttk.Button(self, text='Login')
		loginButton.grid(column=0, row=2, sticky=tk.W, padx=100, pady=5)

if __name__=='__main__':
	app = App()
	app.mainloop()