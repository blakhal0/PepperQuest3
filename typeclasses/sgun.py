from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class stun(default_cmds.MuxCommand):
	"""
	Shoot someone with a Stun Gun

	Usage:
	Stun (player or npc) i.e. Stun variableLabel

	Causes the player or NPC to be tased.
	"""
	key = "stun"
	auto_help = True
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		target = self.caller.search(self.item, candidates=self.caller.location.contents, quiet=True)
		if not target:
			self.caller.msg("|/%s is not in the same room as you." % (self.item))
			return
		if self.caller.tags.get("stunning"):
			self.caller.msg("|/The stun gun has a 10 second recharge time, please wait.")
			return
		if target[0].db.nostunmsg:
			self.caller.msg(target[0].db.nostunmsg)
			return
		if target[0].tags.get("talkative", category="npc") or target[0].tags.get("specialnpc") or target[0].has_account:
			self.caller.msg("|/You level your stun gun at %s and let it rip." % (target[0].key))
			self.caller.msg("|m%s|n screams: WAwayayayayaaaaaaaaa!" % (target[0].key))
			self.caller.msg("%s hits the ground twitching and pees their pants." % (target[0].key))
			self.caller.db.stunned += 1
			if target[0].has_account:
				target.msg("|/|rYou've just been tasered by %s, it tickled.|n" % (self.caller.key))
			self.caller.tags.add("stunning")
			yield 10
			self.caller.tags.remove("stunning")
			return
		self.caller.msg("Please only stun other players and NPC's.")
		return

class StunCmdSet(CmdSet):
	key = "StunCmdSet"
	def at_cmdset_creation(self):
		self.add(stun())

class sgun(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "."
		self.cmdset.add_default(StunCmdSet, permanent=True)
		self.locks.add("drop:false()")