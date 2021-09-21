from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class press(default_cmds.MuxCommand):
	key = "Push"
	aliases = ["push", "push button", "Push button", "push Button", "Push Button"]
	auto_help = True
	def func(self):
		target = self.caller.search("Button")
		self.caller.db.spiceeasyanswer += "%s" % (target.db.letter)
		self.caller.msg("|/You press the button.|/A light mechanical voice states: Password updated.")
		return

class ButtonCmdSet(CmdSet):
	key = "ButtonCmdSet"
	def at_cmdset_creation(self):
		self.add(press())
	
class button(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A simple red button. Bet you want to give it a good ol |cPush|n, don't you."
		self.db.letter = ""
		self.cmdset.add_default(ButtonCmdSet, permanent=True)
		self.locks.add("get:false()")