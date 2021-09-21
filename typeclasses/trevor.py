from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk trevor"
	aliases = ["Talk Trevor", "Talk trevor", "talk Trevor" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mTrevor|n says: Oy, welcome to our humble abode, the game is on, have a seat.")
		answer = yield("|mTrevor|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.msg("|/|mTrevor|n says: ...Okay, that's good to know. Did you get hit in the head recently?")
			self.caller.msg("This person must not be the asset, but it sounds like they may be suspicious of you now.")
			return
		if answer.lower() in ["listen to the game", "listen game"]:
			self.caller.msg("|/|mTrevor|n says: A fan of the fine game of cricket? Absolutely, have a seat.")
			self.caller.msg("Trevor, Brinda, and you huddle around the staticy radio and enjoy the game, escaping the hell of this prison for a brief time.")
			return
		else:
			self.caller.msg("|/|mTrevor|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class TrevorCmdSet(CmdSet):
	key = "TrevorCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class trevor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Trevor is fiddling with a small radio pointing it in different directions, fine tuning the knob trying to get the best reception."
		self.cmdset.add_default(TrevorCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mTrevor|n says: Just because you're one of us, don't think I won't throw you a beating."