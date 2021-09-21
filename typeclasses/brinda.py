from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk brinda"
	aliases = ["Talk Brinda", "Talk brinda", "talk Brinda" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mBrinda|n says: There's nothing like a nice cup of Bangalore Torpedo Chili tea.")
		answer = yield("|mBrinda|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mBrinda|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		if answer.lower() in ["can i have a cup of tea", "cup of tea", "tea"]:
			self.caller.msg("|/|mBrinda|n says: Of course, have a seat.")
			self.caller.msg("You take a seat and enjoy a nice cup of spicy tea. YAHHHOOOO! That's the high octane stuff!!")
			return
		else:
			self.caller.msg("|/|mBrinda|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class BrindaCmdSet(CmdSet):
	key = "BrindaCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class brinda(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Brinda is standing over a bowl using a stinger to heat up water."
		self.cmdset.add_default(BrindaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mBrinda|n says: Just because you're one of us, don't think I won't throw you a beating."