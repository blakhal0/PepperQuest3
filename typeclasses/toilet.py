from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class waste(default_cmds.MuxCommand):
	"""
	Use Toilet

	Usage:
	Use Toilet

	Blast off into the wild blue yonder to explore the great questions of life.
	... just kidding, it's a toilet, you should know what happens when you use it.
	"""
	key = "Use Toilet"
	auto_help = True
	def func(self):
		self.caller.msg("You close the door behind you and use the toilet.")
		yield 3
		self.caller.msg("You finish up, flush the toilet, and wash your hands. You feel relieved.")
		return

class flush(default_cmds.MuxCommand):
	key = "flush the stash"
	auto_help = False
	def func(self):
		if not self.caller.tags.get("holding"):
			self.caller.msg("Command Flush the Stash is not available.")
			return
		else:
			if self.caller.tags.get("caught"):
				return
			self.caller.msg("You scramble madly into the bathroom and slam the door closed, fumbling wildly you open the baggy and start dumping the spice in the toilet and flushing the handle.")
			yield 2
			if self.caller.tags.get("caught"):
				return
			self.caller.tags.add("gotawayclean")
			self.caller.tags.remove("holding")
			self.caller.msg("All the spice swirls down the toilet, destroying the evidence.")
			return

class ToiletCmdSet(CmdSet):
	key = "ToiletCmdSet"
	def at_cmdset_creation(self):
		self.add(waste())
		self.add(flush())

class toilet(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A porcelain throne fit for a pauper."
		self.cmdset.add_default(ToiletCmdSet, permanent=True)
		self.locks.add("get:false()")