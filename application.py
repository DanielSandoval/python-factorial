# Aqui escribe tu codigo

import os
import sys

def factorial(number):
	if number > 1:
		number *= factorial(number - 1)
		return number
	else:
		return 1

def verify_number():
	number = ""
	while number.isdigit() == False:
		try:
			number = raw_input("Enter a number: ")
			number = int(number)
			return number
		except ValueError:
			print "Enter only numbers\n"

def clean_screen():
	os.system('reset')

def exit():
	sys.exit()

def my_application():
	while True:
		clean_screen()
		number = verify_number()
		print factorial(number)
		message = raw_input("PRESS ENTER")

my_application()
