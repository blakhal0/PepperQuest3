from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class talkcactus(default_cmds.MuxCommand):
	key = "talk cactus"
	aliases = ["Talk Cactus", "Talk cactus", "talk Cactus"]
	auto_help = True
	def func(self):
		if self.caller.key.lower() in ["heckseven", "heck7even", "heck7", "variablelabel", "gimp"]:
			self.caller.msg("|/Cactus motions for you to come over, you join him under the running shower, getting drenched.")
			self.caller.msg("|mCactus|n whispers: The Lanister's and Blakhal0 send their regards.")
			self.caller.msg("Cactus begins to stab you repeatedly in the neck, the showers are quickly awash in blood.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|mCactus|n whispers: Usually a cactus doesn't need much water, that's why I hide in here, they'd never think to look here.")
			return

class CactusCmdSet(CmdSet):
	key = "CactusCmdSet"
	def at_cmdset_creation(self):
		self.add(talkcactus())

class cactus(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Cactus is standing in the showers, full dressed. His prickly name seems to mirror his demeanor."
		self.cmdset.add_default(CactusCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mCactus|n says: You do that again, and you're going to get busy dying real fast."