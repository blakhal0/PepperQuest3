from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk nataly"
	aliases = ["Talk Nataly", "Talk nataly", "talk Nataly" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("natalydead"):
			self.caller.msg("There's a small stain on Nataly's bed. Apparently Atropos doesn't mess around.")
			return
		self.caller.msg("|/|mNataly|n says: Hey, good to see you're still alive. What's up?")
		answer = yield("|mNataly|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mNataly|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		else:
			self.caller.msg("|/|mNataly|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class Nataly2CmdSet(CmdSet):
	key = "Nataly2CmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class nataly2(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Nataly is counting books of stamps and sorting pieces of paper."
		self.cmdset.add_default(Nataly2CmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(natalydead)")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mNataly|n says: Just because you're one of us, don't think I won't throw you a beating."