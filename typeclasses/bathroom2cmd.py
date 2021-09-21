from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class bathroom2cmd(default_cmds.MuxCommand):
	"""
	Use Bathroom.

	Usage:
	Use Bathroom

	Use the bathroom
	"""
	key = "Use Bathroom"
	auto_help = True
	def func(self):
		answer = yield("|/What would you like to do?|/Use the Toilet|/Wash your hands")
		if answer.lower() in ["use the toilet", "use toilet", "toilet"]:
			self.caller.msg("|/You step into an open stall and close the door.|/On the back of the door, someone has tagged 'PAM' in graffiti.|/The janitor reminds you to stay seated for the duration of the ride.")
			yield 5
			self.caller.msg("Ahhhhh, that's a relief.|/You finish up and exit the stall.")
			return
		elif answer.lower() in ["wash your hands", "wash hands", "wash"]:
			self.caller.msg("|/You turn the faucet handle, water begins to run.")
			self.caller.msg("You press the soap dispenser and wonderful smelling lavender foam squirts out.")
			self.caller.msg("With a swipe of the hand the air dryer kicks on, thoroughly drying your hands.")
			self.caller.msg("|/Seriously though, wash your damn hands, often and thoroughly. - Love, Peppercon.")
			return
		else:
			self.caller.msg("|/You stare into the mirror and examine your face.|/You look like an idiot that cannot choose one of the options provided to you.")
			return

class Bathroom2CmdSet(CmdSet):
	key = "Bathroom2CmdSet"
	def at_cmdset_creation(self):
		self.add(bathroom2cmd())

class bathroom2(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(Bathroom2CmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")