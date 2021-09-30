# pip install random
import random

# Rule 
print("Winning Rules of the Rock paper scissor game as follows: \n"
	+"Rock vs paper->Rock wins \n"+ "Rock vs scissor->Scissor wins \n"+"paper vs scissor->Papper wins \n")

while 1:
	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
	
	# take user input
	choice = int(input("User turn: "))
	
	# check whether input is vaild or not
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	# Assign value to number
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	# print user and computer choice
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	comp_choice = random.randint(1, 3)
	
	# Making sure computer choice is not equal to the user choice
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	# condition for winning
	if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("scissor wins =>", end = "")
		result = "scissor"
	else:
		print("Rock wins =>", end = "")
		result = "Rock"

	# Printing the winner
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("Do you want quit? (Y/N)")
	ans = input()
	if ans == 'n' or ans == 'N':
		break
print("\nBye Bye")