from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk guard"
	aliases = ["Talk Guard", "Talk guard", "talk Guard"]
	auto_help = True
	def func(self):
		answer = yield("|/|mGuard|n says: Well, what are you belly aching about? You need something from the infirmary or something?|/What do you need?")
		if answer.lower() in ["i need to have bloodwork done", "bloodwork"]:
			self.caller.msg("|/|mGuard|n says: Alright, I'll escort you in.")
			self.caller.msg("The guard escorts you into the infirmary and directs you to an exam table.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		else:
			self.caller.msg("|/|mGuard|n says: I don't give a rats behind, quit your whining and get out of my face before I rearrange yours.")
			return

class InfGuardCmdSet(CmdSet):
	key = "InfGuardCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class infguard(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A guard stands in front of the infirmary doors, blocking the entrance."
		self.cmdset.add_default(InfGuardCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "You keep that up, you'll be in the ICU."