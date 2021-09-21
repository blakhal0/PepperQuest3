from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk reggie"
	aliases = ["Talk Reggie", "Talk reggie", "talk Reggie" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mReggie|n says: Ever since my cellmate got thrown in solitary the guards have been tossing my cell on the regular.")
		answer = yield("|mReggie|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mReggie|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		else:
			self.caller.msg("|/|mReggie|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class ReggieCmdSet(CmdSet):
	key = "ReggieCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class reggie(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Reggie is straightening out the contents of his cell."
		self.cmdset.add_default(ReggieCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mReggie|n says: Just because you're one of us, don't think I won't throw you a beating."