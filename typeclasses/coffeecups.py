from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class cleanupcups(default_cmds.MuxCommand):
	key = "Clean Up Cups"
	aliases = ["clean Up Cups", "clean Up cups", "clean up Cups", "clean up cups", "Clean Up cups", "Clean up Cups", "Clean up cups"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You pull out a garbage bag and toss the stack of cups in.")
		self.caller.msg("A waterfall of rancid old coffee splashes down on the control panel, electrocuting one of the guards.")
		self.caller.msg("The guards look at their compatriot and then at you.")
		self.caller.msg("You're not sure why they had jumper cables and a car battery in the guard room, but your charred nipples tell the rest of the story.")
		results = search_object("#436")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class CupsCmdSet(CmdSet):
	key = "CupsCmdSet"
	def at_cmdset_creation(self):
		self.add(cleanupcups())

class coffeecups(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A scale replica of the Leaning Tower is Pisa is perilously stacked on the edge of the control panel."
		self.cmdset.add_default(CupsCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "While it is an impressive stack of cups, perhaps you'd be better to |cClean Up Cups|n."