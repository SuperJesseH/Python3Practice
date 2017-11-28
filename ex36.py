import random
from sys import argv

# This list will save the choices a player makes throught the game. I.e [a,b,c,d,dead]
player_state = []
# "lose" variable represents a negative "game over"
lose = False
# "win" variable represents a positive "game over"
win = False

file, debug = argv


# This function handles all the user input, printing, and changeing player_state
def chooser(promt, choices_responses):
	print(". . . . .")
	#Print prompt
	print(promt)
	# Shuffle order of choices
	random.shuffle(choices_responses)

	#set up for loop and lists to unpack choices_responses
	choices = []
	responses = []
	choiceID = []
	i = 0

	for choice in choices_responses:
		i += 1
		print(i, ") ", choice[0]) # print options
		choices.append(choice[0])
		responses.append(choice[1])
		choiceID.append(choice[2])

	chosen = input("> ")

	try:
		int(chosen) # make sure the input is valid 
	except:
		print("Enter a number!!!")
		chosen = 0

	if int(chosen) in range(1,len(choices)+1): 
		adjChosen = int(chosen) - 1
		print(responses[adjChosen])
		player_state.append(choiceID[adjChosen]) # change player_state to reflect choice 
	else:
		print("Not a valid response")


# Keep testing conditions unless the player wins or loses
while lose == False and win == False:
	if debug == "debug":
		print("player state = ", player_state)
	# beginning of game
	if player_state == []:
		promt = "The 2016 presidential election approches, you deicde to..."
		# [[choice1, response1, id#1], [choice2, reponse2, id#2]] ("FAIL" -> lose) in chooser()
		choices_responses = [["vote in person", "you make plans to vote on election day, figureing out when and where ahead of time", 0],
		 ["vote early", "this is the best way to make sure your vote is counted", 1]
		 , ["not vote", " ", 2]]

		chooser(promt, choices_responses)

	# If player_state does not equal any predetermined value lose = true 	
	else:
		lose = True


# END GAME CONDITIONS
if lose == True:
	print("The world keeps turning, but things dont generally go the way you would have wanted... [END]")
elif win == True:
	print("[WIN]")
else:
	print("[ERROR]")

