from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk steve"
	aliases = ["Talk Steve", "Talk steve", "talk Steve"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("natalydead"):
			self.caller.msg("|/|mSteve|n says: Miguel and I took care of things. Good looking out.")
			return
		self.caller.msg("|/|mSteve|n says: 1, 2, 3, 4, and 5 makes 50. I need more rubber bands.")
		answer = yield("|mSteve|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mSteve|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		else:
			self.caller.msg("|/|mSteve|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class SteveCmdSet(CmdSet):
	key = "SteveCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class steve(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Steve is stacking and banding books of stamps, carefully double counting each stack."
		self.cmdset.add_default(SteveCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mSteve|n says: Just because you're one of us, don't think I won't throw you a beating."