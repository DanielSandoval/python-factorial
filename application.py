# Aqui escribe tu codigo

import os
import sys

def menu():
	print "FACTORIAL"
	print "EXIT"

def menu_option():
	option_menu = raw_input("Select the option you want: ")
	option_menu = option_menu.lower()
	return option_menu

def menu_decision(option_menu):
	if option_menu == "factorial":
		option_factorial()
	elif option_menu == "exit":
		exit()

def option_factorial():
	clean_screen()
	number = ask_number()
	number = factorial(number)
	print number
	message = raw_input("PRESS ENTER")

def factorial(number):
	if number > 1:
		number *= factorial(number - 1)
		return number
	else:
		return 1

def ask_number():
	number = "Enter only numbers"
	while number == "Enter only numbers":
		number = raw_input("Enter a number: ")
		number = verify_number(number)
	return number

def verify_number(number):
		try:
			number = int(number)
			return number
		except ValueError:
			print "Enter only numbers\n"
			return "Enter only numbers"

def clean_screen():
	os.system('reset')

def exit():
	clean_screen()
	sys.exit()

def my_application():
	while True:
		clean_screen()
		menu()
		option_menu = menu_option()
		menu_decision(option_menu)

my_application()
