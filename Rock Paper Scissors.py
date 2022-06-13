from multiprocessing import RLock
import random
import time



# Set of instructions for Rock-Paper-Scissors
def rps_instructions():

	print()
	print("Instructions for Rock-Paper-Scissors : ")
	print()
	print("Rock beats Scissors")
	print("Paper beats Rock")
	print("Scissors beats Paper")
	print()


def rps():
	
	global rps_table
	global game_map
	global name

	# Game Loop for each game of Rock-Paper-Scissors
	while True:

		print("--------------------------------------")
		print("\t\tMenu")
		print("--------------------------------------")
		print("Enter \"help\" for instructions")
		print("Enter \"R\",\"P\",\"S\" to play")
		print("Enter \"exit\" to quit")
		print("--------------------------------------")

		print()

		# Player Input
		inp = input("Enter your move : ")

		if inp.lower() == "help":
		
			rps_instructions()
			continue

		elif inp.lower() == "exit":
	
			break
    

		elif inp.lower() == "r":
			player_move = 0

		elif inp.lower() == "p":
			player_move = 1		

		elif inp.lower() == "s":
			player_move = 2

		else:
		
			print("Wrong Input!")
			rps_instructions()	
			continue

		print("Computer making a move....")

		print()
		time.sleep(2)

		# Get the computer move randomly
		comp_move = random.randint(0, 2)

		# Print the computer move
		print("Computer chooses ", game_map[comp_move].upper())

		# Find the winner of the match
		winner = rps_table[player_move][comp_move]

		# Declare the winner 
		if winner == player_move:
			print(name, "WINS! YOU WIN!")
		elif winner == comp_move:
			print("COMPUTER WINS! YOU LOSE")
		else:
			print("ITS A TIE!")

		print()
		time.sleep(2)
	


# The main function
if __name__ == '__main__':

	# The mapping between moves and numbers
	game_map = {0:"r", 1:"p", 2:"s"}

	# Win-lose matrix for the game
	rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]


	name = input("Enter your name: ")

	# The GAME LOOP
	while True:

		# The Game Menu
		print()
		print("Let's Play!")
		
		print("Enter 1 to play Rock-Paper-Scissors")
		
		print("Enter 2 to quit")
		print()

		# Try block to handle the player choice 
		try:
			choice = int(input("Enter your choice = "))
		except ValueError:
		
			print("Wrong Choice")	
			continue

		# Play the game
		if choice == 1:
			rps()

		# Quit the GAME LOOP 	
		elif choice == 2:
			break

        
print("End of Game.")