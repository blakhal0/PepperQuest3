from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class pspray(default_cmds.MuxCommand):
	"""
	Distribute some free product.

	Usage:
	Spray (player or npc) i.e. Spray variableLabel

	Causes the player or NPC to be sprayed with Pepper Spray.
	"""
	key = "spray"
	auto_help = True
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		target = self.caller.search(self.item, candidates=self.caller.location.contents, quiet=True)
		if not target:
			self.caller.msg("|/You can't pepper spray that.")
			return
		if self.caller.tags.get("macing"):
			self.caller.msg("|/It takes 10 seconds to load a new pepper spray cartridge, please wait.")
			return
		if target[0].db.nomacemsg:
			self.caller.msg(target[0].db.nomacemsg)
			return
		if target[0].tags.get("talkative", category="npc") or target[0].tags.get("specialnpc") or target[0].has_account:
			self.caller.msg("|/You level your pepper spray at %s and let it rip." % (target[0].key))
			self.caller.msg("|m%s|n screams: WAwayayayayaaaaaaaaa! MY EYES!!!" % (target[0].key))
			self.caller.msg("%s hits the ground rubbing their eyes and vomiting." % (target[0].key))
			self.caller.db.maced += 1
			if target[0].has_account:
				target[0].msg("|/|rYou've just been pepper sprayed by %s, it's spicy!!|n" % (self.caller.key))
			self.caller.tags.add("macing")
			yield 10
			self.caller.tags.remove("macing")
			return
		self.caller.msg("Please only pepper spray other players and NPC's.")
		return

class MaceCmdSet(CmdSet):
	key = "aceCmdSet"
	def at_cmdset_creation(self):
		self.add(pspray())

class mace(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A compact compressed pepper spray device."
		self.cmdset.add_default(MaceCmdSet, permanent=True)
		self.locks.add("drop:false()")