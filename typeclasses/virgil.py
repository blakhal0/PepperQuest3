from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk Virgil"
	aliases = ["Talk Virgil", "Talk Virgil", "talk Virgil" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("endoftheworld"):
			self.caller.msg("|/|mVirgil|n says: Oh man, these matches are BRUTAL, this is amazing!!!!")
			return
		if not self.caller.tags.get("acolyte"):
			self.caller.msg("|/|mVirgil|n says: Oh man, these matches are BRUTAL, this is amazing!!!!")
			return
		if self.caller.tags.get("acolyte"):
			self.caller.msg("|/|mVirgil|n says: Greetings fellow Acolyte, if you are who I think you are, you're looking for the roof, it's up the back stairs.")
			self.caller.tags.add("endoftheworld")
			return

class VirgilCmdSet(CmdSet):
	key = "VirgilCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class virgil(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Virgil is screaming and yelling watching the wrestling matches. You can see the edge of a tattoo on his arm, it looks like a star of peppers."
		self.cmdset.add_default(VirgilCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.nostunmsg = "|/|mVirgil|n says: I am prepared for the day of reckoning! I've made peace with my gods."
		self.db.nomacemsg = "|/|mVirgil|n says: Oh what sweet pleasure!!!"
		self.db.get_err_msg = "|/|mVirgil|n says: I am prepared for the day of reckoning! I've made peace with my gods, can you say the same?"
