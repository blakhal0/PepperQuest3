from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class press(default_cmds.MuxCommand):
	key = "Push"
	aliases = ["push", "push button", "Push button", "push Button", "Push Button"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("passaccepted"):
			self.caller.msg("Hello %s, and welcome back to The 9th Circle SpiceEasy!" % (self.caller.key))
			results = search_object("#2905")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		if self.caller.db.spiceeasyanswer == "VIOLENCE":
			self.caller.msg("|/Password accepted.|/Welcome to The 9th Circle SpiceEasy!")
			self.caller.tags.add("passaccepted")
			results = search_object("#2905")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			if self.caller.db.spiceeasyanswer == "":
				self.caller.msg("|/You've attempted to enter a blank password.|/Password not accepted.")
			else:
				self.caller.msg("|/I'm sorry, %s is not the correct password.|/Password cleared.|/Please try again." % (self.caller.db.spiceeasyanswer))
			self.caller.db.spiceeasyanswer = ""
			return

class ButtonCmdSet(CmdSet):
	key = "ButtonCmdSet"
	def at_cmdset_creation(self):
		self.add(press())
	
class ninthbutton(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Push the button for entrance."
		self.cmdset.add_default(ButtonCmdSet, permanent=True)
		self.locks.add("get:false()")