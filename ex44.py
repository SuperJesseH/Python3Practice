# THE LOBBY: LOBBY FOR YOUR LIFE

class Room(object):

	#what happens when you enter room
	def enter(self):
		pass

	#for "move" options	
	def destinations(self):
		pass
	#for talk options
	def occumpants(self):
		pass






class Person(object):

	def ideology(self):
		pass

	def location(self):
		pass

	def greeting(self):
		pass

	def dialogue(self):
		pass

	def ability(self):
		pass


class Representative(Person):

	influencers = {
	"media" : [],
	"voters" : [],
	"celebritys" : []
	}

	def vote_choice(self):
		pass

	def influencers(self):
		pass


class Senators(Person):

	influencers = {
	"media" : [],
	"voters" : [],
	"celebritys" : []
	}

	def vote_choice(self):
		pass

	def influencers(self):
		pass

class media(Person):

	def opinion(self):
		pass

class Voters(Person):

	def opinion(self):
		pass

class Celebs(Person):

	def opinion(self):
		pass





class Player(object):

	bill_score = {
	"Populist_stateist" : 0,
	"conservative_progressive" : 0,
	"efficency_equity" : 0
	}

	level = 0


	def level_up(self):
		pass

	def location(self):
		pass

	# for "get Info" options
	def getInfo(self):
		pass

	#for "special actions"
	def specialActions(self):
		pass

	def talk(self):
		pass

	def move(self):
		pass

class Engine