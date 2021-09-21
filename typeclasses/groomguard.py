from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk guard"
	aliases = ["Talk Guard", "Talk guard", "talk Guard"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("keymaker"):
			if self.caller.search("Key Impression", location=self.caller, quiet=True):
				self.caller.msg("|/|mGuard|n says: You caused enough of a ruckus in there last time, we'll get someone else to handle the cleaning.")
				return
			self.caller.msg("|/|mGuard|n says: Bout damned time your lazy ass got here to clean.")
			self.caller.msg("The guard unlocks the door and escorts you in.")
			self.caller.msg("|mGuard|n says: Get this place ship shape pronto.")
			results = search_object("#376")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		else:
			answer = yield("|/|mGuard|n says: You better have a reason for approaching the guard room inmate, well... what is it?")
			self.caller.msg("|/|mGuard|n says: I don't give a rats behind, get out of my face before I rearrange yours.")
			return

class GroomGuardCmdSet(CmdSet):
	key = "GroomGuardCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class groomguard(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A guard stands in front of the guard room doors, securing the entrance."
		self.cmdset.add_default(GroomGuardCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mGuard|n says: You keep that up, you'll be in the ICU."