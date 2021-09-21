from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk miguel"
	aliases = ["Talk Miguel", "Talk miguel", "talk Miguel" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("natalydead"):
			self.caller.msg("|/|mMiguel|n says: Steve and I took care of things. Good looking out.")
			return
		self.caller.msg("|/|mMiguel|n says: Could we start only taking bets from the inmates that can spell, yeesh, what even does this say??")
		answer = yield("|mMiguel|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mMiguel|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		else:
			self.caller.msg("|/|mMiguel|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class MiguelCmdSet(CmdSet):
	key = "MiguelCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class miguel(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Miguel is sorting betting sheets and marking a piece of paper keeping track of who owes and who needs paid."
		self.cmdset.add_default(MiguelCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mMiguel|n says: Just because you're one of us, don't think I won't throw you a beating."