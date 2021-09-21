from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class sleep(default_cmds.MuxCommand):
	"""
	Dream Door.

	Usage:
	Dream Door

	Enter the World of Dreams Mini Challenge.
	"""
	key = "Dream Door"
	aliases = ["dream door", "Dream door", "dream Door"]
	auto_help = True
	def func(self):
		self.caller.msg("You find yourself in a strange and confusing place in the world of dreams.")
		place = self.caller.db.dreamreturn
		results = search_object("%s" % (place))
		self.caller.move_to(results[0], quiet=True, move_hooks=True)
		self.caller.db.sendback = "#2"
		return

class DreamCmdSet(CmdSet):
	key = "DreamCmdSet"
	def at_cmdset_creation(self):
		self.add(sleep())
	
class ddoor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An entrance to the World of Dreams. Type |cDream Door|n to enter."
		self.cmdset.add_default(DreamCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialexit")