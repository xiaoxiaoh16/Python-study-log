from sys import exit

# define function
def gold_room():
	
	print "This room is full of gold. How much do you take?"
	
	# get the input from user and following a ">"
	next = raw_input("> ")
	
	# why?
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
	
	# how_much < 50 then exit
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	
	# call function dead()
	else:
		dead("You greedy bastard!")


def bear_room():
	
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear? take honey? taunt bear? open door?" 

	bear_moved = False
	
	while True:

		# get input from user and following ">"
		next = raw_input("> ")

		# take honey then call function dead()
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")

		# taunt bear and bear not moved then you can go through it
		# why bear_moved = True
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True

		# taunt bear and bear moved then call function dead()
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")

		# open door and bear moved then call function gold_room()
		elif next == "open door" and bear_moved:
			gold_room()

		# others 
		else:
			print "I got no idea what that means."
						
def cthulhu_room():

	print "Here you see the great evil Cthulhu." 
	print "He, it, whatever stares at you and you go insane."						
	print "Do you flee for your life or eat your head?"

	# get input from user
	next = raw_input("> ")

	# flee then call function start
	if "flee" in next:
		start()
	
	# head then call function dead()
	elif "head" in next:
		dead("Well that was tasty!")
	
	# others then call function cthulhu_roo()
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)


def start():
	print "You are in a dark room."
	print "There is a door to your right and left." 
	print "Which one do you take?" 

	# get input from user
	next = raw_input("> ")

	# left then call function bear_room()
	if next == "left":
		bear_room()
	
	# right then call function cthulhu_room()
	elif next == "right":
		cthulhu_room() 

	else:
		dead("You stumble around the room until you starve.")

# begin with function start()
start()

