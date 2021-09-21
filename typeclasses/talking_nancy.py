from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu
from evennia.prototypes.spawner import spawn

class talkingnancy(default_cmds.MuxCommand):
	key = "Talk Nancy"
	aliases = ["talk nancy", "Talk nancy", "talk Nancy"]
	auto_help = True

	def func(self):
		EvMenu(self.caller, "typeclasses.talking_nancy", startnode="menu_start_node")

def menu_start_node(caller):
	text = "Well hello there, I'm Saint Nancy, but everyone just calls me N.|/Welcome to the Dark Alley SpiceEasy. What can I get for you sweetheart?"
	options = ({"desc": "This place is amazing, how do you manage to not get shut down by the feds?",
		"goto": "feds"},
		{"desc": "I'm a little thirsty, what do you have to drink?",
		"goto": "drinks"},
		{"desc": "I'm in a bit of a spot here, I'm supposed to pick something up for someone, but I don't know who I'm supposed to get it from.",
		"goto": "caution"},
		{"desc": "Nothing for now, thanks, I'm just enjoying the atmosphere.",
		"goto": "exit"})
	return text, options

def feds(caller):
	text = "Whoa whoa whoa, you're going to want to watch it with the F word around here.|/People get spooked pretty easy.|/We have a bit of an agreement with the locals, the ones that matter, but the agents are always sniffing around trying to find us."
	options = ({"desc": "Ah, gotcha. My apologies.",
		"goto": "menu_start_node"})
	return text, options

def drinks(caller):
	text = "A little something to wet your whistle, sure thing, I don't get paid to stand here and hold the bar up you know.|/What's your poison?"
	options = ({"desc": "A shot of Hell Fire Whiskey, please.",
		"goto": "knockitback"},
		{"desc": "One Flaming Moe, please.",
		"goto": "knockitback"},
		{"desc": "Mix up a Sizzling Sazerac, please.",
		"goto": "knockitback"},
		{"desc": "Eternal Flame Martini, shaken, not stirred, please.",
		"goto": "knockitback"},
		{"desc": "Nothing for me, thanks.",
		"goto": "menu_start_node"})
	return text, options

def knockitback(caller):
	text = "Great call, one of my personal favorites.|/Saint N goes to work, you could almost swear there are small red-yellow flames surrounding her hands as she whirls and twirls the bottles and glasses.|/Before you know it theres a full drink glass on a marble coaster in front of you.|/A wicked smile crosses the bartenders face and her eyes flash, here you are, since you're new here this one's on the house."
	options = ({"desc": "Thanks!",
		"goto": "sip"})
	return text, options

def sip(caller):
	text = "You lift the glass to your nose and breath in deeply.|/There's a lot of spice in there, you tip the glass back and empty it in one go.|/Sinuses clear instantly as your forehead beads sweat, then the fire. You feel alive.|/All you want is more, a deep gnawing desire to have more, as much as you can get, to fill your stomach to bursting.|/The feeling passes quickly."
	options = ({"desc": "That was great, I would like another drink please.",
		"goto": "drinks"},
		{"desc": "That's enough for me, whooo.",
		"goto": "menu_start_node"})
	return text, options

def caution(caller):
	text = "Shhhh, keep it down.|/Look sweetie, that's the kind of question the Feds ask, that'll get you kicked out of here.|/The person that runs the place is who you're looking for, but what's the fun in me just telling you who they are.|/I will tell you that if you just go around asking everyone you're going to get tossed out pretty quick.|/If you get tossed out once, the bouncer will become a lot less patient with getting reports of you bothering people.|/Take in the vibe, you've got all the clues you need to figure it out.|/Good luck."
	options = ({"desc": "Well that's maddeningly unhelpful. Ok, I guess I'll just have to figure it out on my own.",
		"goto": "menu_start_node"})
	return text, options

def exit(caller):
	text = "Enjoy your time, and watch your manners. Hope you have a hell of a night."
	options = ()
	return text, options

class NancyCmdSet(CmdSet):
	key = "NancyCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingnancy())

class nancy(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A handsome, tall woman with a strong jaw stands behind the bar, mixing drinks. Her red sequined dress glitters as she works, small costume horns stick up from a matching red headband on top of her head."
		self.cmdset.add_default(NancyCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("evnpc")
		self.db.get_err_msg = "Oh, you absolutely can't handle this, I promise you."