from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu
from evennia.prototypes.spawner import spawn

class talkingclerk(default_cmds.MuxCommand):
	key = "Talk Clerk"
	aliases = ["talk clerk", "Talk clerk", "talk Clerk"]
	auto_help = True

	def func(self):
		if self.caller.tags.get("fire"):
			self.caller.msg("The clerk is currently panicing trying to put out a fire, they don't have time to talk to you.")
			return
		EvMenu(self.caller, "typeclasses.talking_clerk", startnode="menu_start_node")

def menu_start_node(caller):
	text = "Welcome to Uncle Harry's Five and Dime, how can I help you?"
	options = ({"desc": "Can I use the bathroom, I really have to go.", 
		"goto": "bathroom"},
		{"desc": "I'm looking for Spicy Panda Snacks, you uhhh, you got anything like that here?",
		"goto": "busted"},
		{"desc": "Nevermind, I'm just going to look around.",
		"goto": "exit"})
	return text, options

def busted(caller):
	text = "The clerk looks around, reaches under the counter and pulls out a package of spicy panda snacks.|/Is this what you're asking me for?"
	options = ({"desc": "Yes.",
		"exec": reeducation},
		{"desc": "No.",
		"goto": "menu_start_node"})
	return text, options

def reeducation(caller):
	caller.msg("______________________________________________________________________________")
	caller.msg("|/")
	caller.msg("Ok, sure thing... Uhh just one moment while I, uhh, ring this up for you.|/You hear a button clicking rapidly.")
	caller.msg("______________________________________________________________________________")
	caller.msg("|/")
	caller.msg("Federal Agents burst through the door screaming and tackle you to the ground.|/Before you have a chance to react, you're handcuffed and a black bag is thrown over your head.|/You hear a vehicle door open and shut as you're thrown roughly into the vehicle.")
	if caller.tags.get("toilet"):
		caller.tags.remove("toilet")
	send_to = "#219"
	results = search_object(send_to)
	caller.move_to(results[0], quiet=True, move_hooks=False)
	return "silentexit"

def bathroom(caller):
	if caller.tags.get("toilet"):
		text = "How many times you want me to press the buzzer?? Just go already, don't pee on my floor."
	else:
		caller.tags.add("toilet")
		text = "*Sigh*, Yeah, it's a buzz in door, hold on. *BZZZERT* Don't go making a mess in there."
	options = ({"desc": "Thanks, I really appreciate it.",
		"goto": "menu_start_node"})
	return text, options

def exit(caller):
	text = "Thank you, come again"
	options = ()
	return text, options

def silentexit(caller):
	text = ""
	options = ()
	return text, options

class ClerkCmdSet(CmdSet):
	key = "ClerkCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingclerk())

class clerk(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A bored clerk stands behind bulletproof glass, idly flipping through a magazine."
		self.cmdset.add_default(ClerkCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(fire)")
		self.tags.add("evnpc")
		self.db.get_err_msg = "You scramble wildly trying to reach the clerk, but they're behind bulletproof glass."