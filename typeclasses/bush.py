from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class butterfly(default_cmds.MuxCommand):
	key = "Catch Butterfly"
	aliases = ["catch butterfly", "Catch butterfly", "catch Butterfly"]
	auto_help = False
	def func(self):
		if self.caller.tags.get("butterfly"):
			self.caller.msg("You already caught a butterfly, what, you starting a collection or something?")
			return
		butterfly_proto = {
		"key": "Butterfly",
		"typeclass": "typeclasses.objects.DefaultObject",
		"desc": "A beautiful Blue Morpho Butterfly.",
		"location": self.caller
		}
		spawn(butterfly_proto)
		self.caller.msg("|/You carefully catch the butterfly and tuck it under your shirt. Oohhhh, that tickles.")
		self.caller.tags.add("butterfly")
		return

class ButterflyCmdSet(CmdSet):
	key = "ButterflyCmdSet"
	def at_cmdset_creation(self):
		self.add(butterfly())

class bush(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A small well manicured bush is growing near the yard wall.|/Several pretty butterflies flutter around the bush.|/They're so pretty."
		self.cmdset.add_default(ButterflyCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialobj")
		self.db.get_err_msg = "Wouldn't you rather |cCatch Butterfly|n as opposed to take a bush?"