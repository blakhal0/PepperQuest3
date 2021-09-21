from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class shiv(default_cmds.MuxCommand):
	"""
	Kill a fool

	Usage:
	Shank (player) i.e. Shank variableLabel

	Causes the player shanked to respawn in the infirmary.
	I really hope this doesn't cause a lot of problems.
	"""
	key = "shank"
	auto_help = True
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		if self.caller.tags.get("stabbing"):
			self.caller.msg("Your arm is tired from stabbing people, give it a few seconds.")
			return
		target = self.caller.search(self.item, candidates=self.caller.location.contents, quiet=True)
		if not target:
			self.caller.msg("%s is not in the same room as you." % (self.item))
			return
		if not target[0].has_account:
			self.caller.msg("Please only stab other players.")
			return
		self.caller.tags.add("stabbing")
		self.caller.db.shived += 1
		self.caller.location.msg_contents("|/|r%s just attacked %s.|n" % (self.caller.key, target[0].key))
		target[0].msg("|/|rSURPRISE MOTHER FUNKER!! You've just been shanked by %s.|/Welcome to prison.|n" % (self.caller.key))
		results = search_object("#436")
		target[0].move_to(results[0], quiet=True, move_hooks=False)
		yield 10
		self.caller.tags.remove("stabbing")

class ShivCmdSet(CmdSet):
	key = "ShivCmdSet"
	def at_cmdset_creation(self):
		self.add(shiv())

class stabby(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A sharpened piece of metal. See |cHelp Shank|n to learn how to use it."
		self.cmdset.add_default(ShivCmdSet, permanent=True)
		self.locks.add("drop:false()")