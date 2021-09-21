from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class giveupcmd(default_cmds.MuxCommand):
	"""
	Give Up.

	Usage:
	Give Up

	Leave the world of dreams and go back to where you entered from.
	"""
	key = "Give Up"
	auto_help = True
	def func(self):
		target = self.caller.search("giveup")
		self.caller.msg("Giving up eh? Quitter.|/No worries, the World of Dreams isn't the easiest of places.|/Next time you come back you'll start right where you left off.|/See you then....")
		self.caller.msg("|/|/The dream begins to fade and ripple, you feel as though you're falling through an endless abyss of pure color.")
		self.caller.msg("|/You wake startled and drenched in sweat.|/")
		place = self.caller.db.sendback
		results = search_object("%s" % (place))
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		self.caller.db.dreamreturn = target.db.returnto
		return

class GiveUpCmdSet(CmdSet):
	key = "GiveUpCmdSet"
	def at_cmdset_creation(self):
		self.add(giveupcmd())

class giveup(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(GiveUpCmdSet, permanent=True)
		self.db.returnto = "#178"
		self.locks.add("get:false()")
		self.locks.add("view:false()")