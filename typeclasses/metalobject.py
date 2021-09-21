from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class metal(default_cmds.MuxCommand):
	key = "Get Metal"
	aliases = ["get metal", "Get metal", "get Metal"]
	auto_help = False
	def func(self):
		if self.caller.tags.get("metal"):
			self.caller.msg("You already have the metal.")
			return
		metal_proto = {
		"key": "Metal",
		"typeclass": "typeclasses.objects.DefaultObject",
		"desc": "A thin, short metal rod.",
		"location": self.caller
		}
		spawn(metal_proto)
		self.caller.msg("|/You pick up the metal and slide it into your waistband.")
		self.caller.tags.add("metal")
		return

class MetalCmdSet(CmdSet):
	key = "MetalCmdSet"
	def at_cmdset_creation(self):
		self.add(metal())

class metalobject(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A thin, short metal rod that comes to a sharpened point."
		self.cmdset.add_default(MetalCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(metal) and tag(lookedbin)")
		self.tags.add("specialobj")
		self.db.get_err_msg = "Maybe try |cGet Metal|n."