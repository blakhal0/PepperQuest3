from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu

class talkingluke(default_cmds.MuxCommand):
	key = "Talk Luke"
	aliases = ["Talk Luke", "talk luke", "Talk luke", "talk Luke"]
	auto_help = True

	def func(self):
		if self.caller.tags.get("holding"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
		EvMenu(self.caller, "typeclasses.talking_luke", startnode="menu_start_node")

def menu_start_node(caller):
	text = "Hey, what's up %s" % (caller.key)
	if caller.tags.get("noleave"):
		text = "Go to the window in the living room and check out what the hell that sound was."
		options = ({"desc": "Ok, ok, I'm going.",
			"goto": "silentexit"})
		return text, options
	elif caller.tags.get("sugardone"):
		if not caller.search('Ghost Peppers', location=caller, quiet=True):
			options = ({"desc": "Umm, apparently I screwed up big time and lost the peppers on the way back here...",
				"goto": "failure"})
		else:
			options = ({"desc": "Yo yo yo, I got the peppers!!",
				"goto": "raid"})
	elif caller.tags.get("sugarmission"):
			if caller.tags.get("sugarbaby"):
				options = ({"desc": "Sugar is a pain in the ass, I thought you said I just had to pick the stuff up!!",
					"goto": "runaround"})
			else:
				options = ({"desc": "What do I need to do again?",
					"goto": "reminder"})
	else:
		options = ({"desc": "Hey, Luke, smells awesome in here. Renee said you were looking for me, what's up?",
			"goto": "sugar"},
			{"desc": "What's on tap for today my culinary criminal?",
			"goto": "game"})
	return text, options

def game(caller):
	text = "Today, my fine and gentle spicehead, I am preparing a delicious, mouth scorching assortment of pre and mid game refreshments.|/Renee has been up all morning tuning in the rabbit ears just for the occasion.|/Which brings me to the predicament we find ourselves in currently..."
	options = ({"desc": "This sounds suspiciously like me doing something and not getting paid for it.",
		"goto": "sugar"},
		{"desc": "I'm not interested in running errands for you, do it yourself.",
		"goto": "beg"})
	return text, options

def sugar(caller):
	text = "Have you ever dreamed of being a hero to everyone important to you? Because I need you to be one today.|/I just got the call that Sugar got some product in and it's EXACTLY what I need to set off this bomb food for the game.|/I just need you to run over there and pick it up for me, don't worry about paying, I've already worked everything out with him.|/You just gotta pick it up and bring it back here.|/He lives at the end of Telegraph Ave, you can't miss the place."
	options = ({"desc": "Well it may not be every day that you puny mortals get asked to be the hero *stretch* but I'm used to it. I'm on the job.",
		"goto": "missionaccepted"},
		{"desc": "I don't really have time for all that right now. I'll get back to you later.",
		"goto": "beg"})
	return text, options

def beg(caller):
	text = "Oh come on, please, pretty please, with peppers on top?"
	options = ({"desc": "Fine, fine, geesh, I'll do it. Stop begging, it's beneath an artist of your caliber.",
		"goto": "missionaccepted"},
		{"desc": "I'm just not feeling it, I'll come back when I've got time for it.",
		"goto": "exit"})
	return text, options

def missionaccepted(caller):
	caller.tags.add("sugarmission")
	text = "There are many reasons I appreciates you, however, your willingness to perform menial tasks for free is paramount.|/End of Telegraph Ave, can't miss the house."
	options = ({"desc": "Oh, is THAT what you appreciate about me? I'll be back later.",
		"goto": "exit"})
	return text, options

def runaround(caller):
	text = "Yeah, about that, I may have not been 100% transparent on the details.|/Sorry man, I'd go but *Luke gestures to the food cooking*, I'm kinda tied up here. Just do what he asks, it can't be that bad."
	options = ({"desc": "You shoot Luke a scowl and swipe your finger through one of the dips, licking your finger. You point at him 'You owe me that at least for dealing with this.'",
		"goto": "exit"})
	return text, options

def reminder(caller):
	text = "I just got the call that Sugar got some product in and it's EXACTLY what I need to set off this bomb food for the game.|/I just need you to run over there and pick it up for me, don't worry about paying, I've already worked everything out with him.|/You just gotta pick it up and bring it back here.|/He lives at the end of Telegraph Ave, you can't miss the place."
	options = ({"desc": "You shoot Luke a scowl and swipe your finger through one of the dips, licking your finger. You point at him 'You owe me that at least for dealing with this.'",
		"goto": "exit"},
		{"desc": "What's on tap for today my culinary criminal?",
		"goto": "food"})
	return text, options

def food(caller):
	text = "Today, my fine and gentle spicehead, I am preparing a delicious, mouth scorching assortment of pre and mid game refreshments.|/Renee has been up all morning tuning in the rabbit ears just for the occasion.|/Just waiting on you to go get the good stuff from Sugar."
	options = ({"desc": "Yeah, yeah, I'm going, I'm going.",
		"goto": "exit"},
		{"desc": "Yeah about that, what exactly do I need to do again?",
		"goto": "reminder"})
	return text, options

def failure(caller):
	caller.tags.remove("sugardone")
	text = "Oh, yeah, you really dropped the ball here.|/Ok, I'll work some magic and give Sugar a call, truck it on over to the spot and pick up some more.|/You're KILLING me here smalls."
	options = ({"desc": "I'm really sorry, I'll head over there and get some more and I promise I won't screw it up again.",
		"goto": "exit"})
	return text, options

def raid(caller):
	caller.tags.remove("sugardone")
	caller.tags.remove("sugarbaby")
	caller.tags.remove("sugarmission")
	caller.tags.add("noleave")
	for o in caller.contents:
		if o.key == "Ghost Peppers":
			o.delete()
	text = "You toss Luke the peppers, his eyes light up.|/%s, you are simply a superior human to the rest of us!|/This is going to be perfect. THANK YOU!!|/*THUMP THUMP. THUMP*...Hey, what's that noise???" % (caller.key)
	options = ({"desc": "I'm not sure, I'll to take a look out the window.",
		"goto": "silentexit"})
	return text, options

def exit(caller):
	text = "Later tater."
	options = ()
	return text, options

def silentexit(caller):
	text = ""
	options = ()
	return text, options

class LukeCmdSet(CmdSet):
	key = "LukeCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingluke())

class luke(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Luke narrows his eyes and peeks over the edge of a cookbook at a pile of hardboiled eggs while slowly stirring a simmering sauce in a pan on the stove.|/A timer dings and he blindly reaches down and pulls a roast pan out of the oven swearing as he burns his hand."
		self.cmdset.add_default(LukeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(holding)")
		self.tags.add("evnpc")
		self.db.get_err_msg = "Heeey, that tickles, knock it off."