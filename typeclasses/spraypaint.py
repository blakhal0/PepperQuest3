from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class graffiti(default_cmds.MuxCommand):
	key = "claim territory"
	alases = ["Claim Territory", "Claim territory", "claim Territory"]
	auto_help = True
	def func(self):
		if not self.caller.location.db.graffitinum:
			self.caller.msg("|/This area is not disputed, there's no need to claim it.")
			return
		if not self.caller.tags.get(self.caller.location.db.graffitinum) == self.caller.location.db.graffitinum:
			self.caller.msg("|/Time to claim some territory! IN THE NAME OF SPAIN.. err THE GHOST REAPERS!!")
			self.caller.msg("You artfully craft your cartel's logo on the wall over top of the Naga Vipers graffiti.")
			self.caller.tags.add(self.caller.location.db.graffitinum)
			self.caller.db.claimed += 1
			if self.caller.db.claimed == 6:
				self.caller.msg("|/|rYou've done the Ghost Reapers proud and claimed all disputed territory.|n")
				self.caller.tags.add("conquerer")
			return
		if self.caller.tags.get(self.caller.location.db.graffitinum) == self.caller.location.db.graffitinum:
			self.caller.msg("|/You've already claimed this area, no need to do it again.")
			return

class GraffitiCmdSet(CmdSet):
	key = "GraffitiCmdSet"
	def at_cmdset_creation(self):
		self.add(graffiti())
	
class spraypaint(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An assortment of rattle cans in Reapers colors."
		self.cmdset.add_default(GraffitiCmdSet, permanent=True)
		self.locks.add("drop:false()")