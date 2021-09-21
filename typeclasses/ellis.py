from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class elliscmd(default_cmds.MuxCommand):
	key = "ellis"
	auto_help = True
	def func(self):
		self.caller.msg("|/I see you know your spy history. This park is loosely modeled after the park where Agent Robert Hanssen would signal a drop has been made at a nearby bridge for his soviet spy handler.")
		self.caller.msg("A new opportunity for the end of the game has been made available to you.")
		self.caller.tags.add("doubleagent")
		return

class EllisCmdSet(CmdSet):
	key = "EllisCmdSet"
	def at_cmdset_creation(self):
		self.add(elliscmd())
	
class ellis(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(EllisCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")