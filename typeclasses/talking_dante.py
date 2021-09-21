from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu
from evennia.prototypes.spawner import spawn
import random

class talkingdante(default_cmds.MuxCommand):
	key = "Talk Dante"
	aliases = ["talk dante", "Talk dante", "talk Dante"]
	auto_help = True

	def func(self):
		EvMenu(self.caller, "typeclasses.talking_dante", startnode="menu_start_node")

def menu_start_node(caller):
	openingline = ["Hey there, how's it going? I just can't get enough of this place!", "This place is really something else isn't it! I never want to leave!!", "I would drink a THOUSAND of these drinks if I could", "I NEED MORE!! MORE MORE MORE!!!", "I don't think I can fit another drop in me, but I just keep ordering drinks.", "These spicy drinks are AMAZING, I can't get enough!", "Oh, oh I'm sooo bloated, why do I keep drinking.", "If I was drowning in a sea of these Sizzling Sazerac, I would drink the sea dry."]
	firstoption = ["This place is really something isn't it?", "Wow, I've never been anywhere like this before!", "This is the best place ever!!", "I feel like I never want to leave this place", "After being here, who would go anywhere else?!?!"]
	text = random.choice(openingline)
	options = []
	options.append({"desc": "%s" % (random.choice(firstoption)), "goto": "randombs"})
	options.append({"desc": "So I was wondering if you might be holding a Package... for Sugar, the, uhhh, provider of spice on the other side of town? I was sent here to get it.", "goto": "package"})
	options.append({"desc": "Oh, you know what, I think I got you confused with someone else, my apologies.", "goto": "exit"})
	return text, options

def randombs(caller):
	text = "You got that right, this place it the cat's pajamas!"
	options = ({"desc": "Oh, by the way I was wondering...",
		"goto": "menu_start_node"})
	return text, options

def package(caller):
	text = "Well, that depends now doesn't it.|/Maybe I am, and maybe I'm not.|/See this here is my place so, everything in it is mine.|/And if someone's got a package, well that makes it my package doesn't it.|/Now, why would I want to give you anything? That's the question.|/I'll make you a deal, you answer this one question and I'll give you what you're looking for.|/Ready?|/I once knew a man named Virgil that brought a friend to take a tour of my house. On a scale of 1-9 I'm not all that bad, especially compared to my six older siblings. What am I?"
	options = {"key": "_default", "exec": check}
	return text, options

def check(caller, raw_string):
	answer = raw_string.strip()
	if answer.lower() in ["gluttony"]:
		return "award"
	else:
		return "fail"

def award(caller):
	package_proto = {
	"key": "Package",
	"typeclass": "typeclasses.objects.DefaultObject",
	"desc": "A nondescript package that smells a bit spicy.",
	"location": caller
	}
	if caller.search('Package', location=caller, quiet=True):
		caller.msg("That's the right answer, but you already have the Package.")
		text = ""
		options = ()
		return text, options
	else:
		spawn (package_proto)
		text = "Congratulations, you figured it out.|/I suppose I can trust you with this then.|/Dante hands you the Package.|/Don't go getting busted with that now, you don't want to owe me money."
		options = ()
		return text, options

def exit(caller):
	text = "Hey, enjoy the night, and gulp down a few of these drinks while you're here!! As many as you can!!!"
	options = ()
	return text, options

def fail(caller):
	text = "Sorry Charlie, but that's not the right answer.|/Take a walk around and give it a think, maybe a clue will light the way."
	options = ()
	return text, options

class DanteCmdSet(CmdSet):
	key = "DanteCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingdante())

class dante(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(DanteCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("evnpc")
		self.db.get_err_msg = "Kidnapping is a crime."