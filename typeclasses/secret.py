from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class welcome(default_cmds.MuxCommand):
	key = "Welcome"
	auto_help = False
	def func(self):
		self.caller.msg("Well la di da, you figured out a simple secret.")
		self.caller.msg("Aren't you a smart cookie.")
		answer = yield("Do you want to know a secret?")
		if answer.lower() in ["yes", "y"]:
			self.caller.msg("Later in the game, you'll be able to stab other players, if you can figure out who to ask for what.|/Rarely Ever Does Someone Have A Nasty Koala.")
			return
		if answer.lower() in ["no", "n"]:
			self.caller.msg("Well okay then, carry on with the game. Have fun!")
			return

class WelcomeCmdSet(CmdSet):
	key = "WelcomeCmdSet"
	def at_cmdset_creation(self):
		self.add(welcome())
	
class secret(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "no desc."
		self.cmdset.add_default(WelcomeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")