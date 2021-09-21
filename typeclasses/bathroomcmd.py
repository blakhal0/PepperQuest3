from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class bathroomcmd(default_cmds.MuxCommand):
	"""
	Use Bathroom.

	Usage:
	Use Bathroom

	Use the bathroom
	"""
	key = "Use Bathroom"
	auto_help = True
	def func(self):
		if self.caller.search('Match', location=self.caller, quiet=True):
			answer = yield("|/What would you like to do?|/Use the Toilet|/Wash your hands|/Start a fire")
			if answer.lower() in ["use the toilet", "use toilet", "toilet"]:
				self.caller.msg("|/You resist the urge to vomit and use the toilet...")
				yield 5
				self.caller.msg("Ahhhhh, that's a relief.")
				return
			elif answer.lower() in ["wash your hands", "wash hands", "wash"]:
				self.caller.msg("|/You turn the faucet handle with some effort, rusty water begins to run.")
				self.caller.msg("You press the soap dispenser with hope, but nothing comes out.")
				self.caller.msg("Reaching blindly for paper towels, you come up empty, the dispensers entire contents are in the garbage.")
				return
			elif answer.lower() in ["start a fire", "start fire", "fire"]:
				self.caller.tags.remove("oldtimers")
				self.caller.tags.add("fire")
				for o in self.caller.contents:
					if o.key == "Match":
						o.delete()
				self.caller.msg("|/The match bursts to life as you strike it on the wall.")
				self.caller.msg("Tossing the match into the garbage, the damp paper towels begin to smolder, quickly filling the room with smoke.")
				yield 5
				self.caller.msg("This should distract the clerk for a little while.")
				self.caller.msg("You yell 'HEY, THIS PLACE IS ON FIRE!!!'|/The clerk responds with a startled cry and you hear them come running.")
				yield 30
				self.caller.tags.remove("fire")
				self.caller.msg("The fire has been extinguished.")
				return
			else:
				self.caller.msg("|/You stare into the mirror and examine your face.|/You look like an idiot that cannot choose one of the options provided to you.")
				return
		else:
			answer = yield("|/What would you like to do?|/Use the Toilet|/Wash your hands")
			if answer.lower() in ["use the toilet", "use toilet", "toilet"]:
				self.caller.msg("|/You resist the urge to vomit and use the toilet...")
				yield 5
				self.caller.msg("Ahhhhh, that's a relief.")
				return
			elif answer.lower() in ["wash your hands", "wash hands", "wash"]:
				self.caller.msg("|/You turn the faucet handle with some effort, rusty water begins to run.")
				self.caller.msg("You press the soap dispenser with hope, but nothing comes out.")
				self.caller.msg("Reaching blindly for paper towels, you come up empty, the dispensers entire contents are in the garbage.")
				return
			else:
				self.caller.msg("|/You stare into the mirror and examine your face.|/You look like an idiot that cannot choose one of the options provided to you.")
				return

class BathroomCmdSet(CmdSet):
	key = "BathroomCmdSet"
	def at_cmdset_creation(self):
		self.add(bathroomcmd())

class bathroom(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(BathroomCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")