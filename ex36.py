import random
from sys import argv, exit

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
		prompt = "The 2016 presidential election approches, you deicde to..."
		# [[choice1, response1, id#1], [choice2, reponse2, id#2]]
		choices_responses = [["vote in person", "you make plans to vote on election day, figureing out when and where ahead of time", 0],
		 ["vote early", "this is the best way to make sure your vote is counted", 1],
		 ["not vote", " ", 2]]

		chooser(prompt, choices_responses)
		#This is a fix to make the first two options equal (makes the code cleaner)
		if player_state == [1]:
			player_state = [0]

	# Choose a candidate
	elif player_state == [0]:
		prompt = "You decide to vote for..."
		choices_responses = [["Hillary", "After submitting your ballot you anxiously await election results...\n\"The Donald\" wins.", 0], 
		["Donald", "You know this country is acheing for change and you can't bear to see the liberals impose their version of America. You wait for the result to prove the pundits and mainstream media wrong...\n\"The Donald\" wins!", 1],
		["A Right Leaning 3rd Party Candidate", "You don't expect them to win but can't bring yourslef to vote for one of the major candidates... \nUltimately \'The Donald\' wins", 2],
		["A Left Leaning 3rd Party Candidate", "You don't expect them to win but can't bring yourslef to vote for one of the major candidates... \nUltimately \'The Donald\' wins", 3]]

		chooser(prompt, choices_responses)

	# Hillary vote
	elif player_state == [0,0]:
		prompt = "You spend the next few days in a state of shock and disbelief. Eventually you decide the only way to move foward is to..."
		choices_responses = [["Emerse yourself in reasearch", "You study the election results and spend weeks reading about what happend and the coalition of voters that put \"The Donald\" in The Whitehouse. Then just as you're beginning to get a grasp on this new reality you see the latest Trump news...", 0], 
		["Give up on society", "Your only interest is self preservation as you see the worlds cherished institutions collapse around you. You invest in bitcoin and begin reaserching technology, skills and gear that will help you in this hostile future", 1],
		["Refuse to accept this result", "Given all the collusion and bad behavior that went on during the campain you resolve to do anything to make sure \"The Donald\'s\" presidency is thwarted at every turn. He will never be your president!", 2],
		["Recognize that this is a moment and struggle that will define a generation", "You redouble your commitment to your core values. You organize, advocate, and run for office yourself. You know that The Donald may have won the battle but you refuse to let him win the war.", 3]]

		chooser(prompt, choices_responses)

	# trump vote
	elif player_state == [0,1]:
		prompt = "You are glad to see the election results but you know The Donald is not a conventional politican. With Inaguration Day a couple months away you..."
		choices_responses = [["Cautiously watch as the administration takes shape", "You hope he sticks to conventional conservative principals and controls his worst impulses", 0],
		["Recognize that this election has reshaped political power in this country", "Now politicians know they are answerable to voters and not the otherway around. You look foward to a more responsive and populist washington", 1],
		["Trust The Donald to do what is right for the country","You avoid thinking about politics most of the time", 2],
		["Relish the liberal consternation over the election results", "The Donald proves that SJWs and losers will not run america. You proudly wear your MAGA hat and always defend The Donald from fake news and liberal crap", 3]]

		chooser(prompt, choices_responses)

	# Civics
	elif player_state == [0,0,2] or player_state == [0,0,3] or player_state == [0,1,0] or player_state == [0,1,1]:
		prompt = "You learn a great deal about America's institutions, power structures and the depths of partisanship. Extreamists of all kinds are drawing more and more appeal. Longstanding american taboos are being broken, sometime for good reason. The administration's policies have been a grab bag, you find some abhorent, others worthwile, but nothing truly large-scale, elegant, or benifical. Scandals, embarassments and allegations are discussed constantly. What once promised to be a sharp break with the past seemed murkier by the day. \nThe Donald/Russia collusion investigation picks up steam. "
		choices_responses = [["Decide that The Donald's faliure is certain, now the most important issue is how to rebuild our country in the aftermath", "You seek out differing opinions, become more careful about what you read online, you begin to feel that despite what you had seen the arc of histroy bends twords justice. You always stand up for whats right but also find time to relax again.", 0],
		["Decide there's no time to wait! Do whatever it takes to be the loudest voice in the room.", "Months go by and the world gets crazier and crazier. You end up hateing most other Americans.", 1]]

		chooser(prompt, choices_responses)

	# Right Radical (Add another state for right leaning 3rd party)
	elif player_state == [0,1,3]:
		prompt = "Hate crimes, deportation, ...  ()"
		choices_responses = [["(Unfisnished", "", 0],
		["Unfinished","", 1]]

		chooser(prompt, choices_responses)


	# Win
	elif player_state[3] == 0 and player_state[0:3] != [0, 1, 3]:
		win = True


	# If player_state does not equal any predetermined value lose = true 	
	else:
		lose = True


# END GAME CONDITIONS
if lose == True:
	print("The world keeps turning, but things generally do not go the way you would have wanted... [END]")
	exit(0)
elif win == True:
	print("[WIN]")
else:
	print("[ERROR]")

