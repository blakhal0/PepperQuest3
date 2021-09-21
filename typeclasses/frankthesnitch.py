from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class talkfrank(default_cmds.MuxCommand):
	key = "talk frank"
	aliases = ["Talk Frank", "Talk frank", "talk Frank"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mFrank|n says: Things are a little different here. The snitches GIVE stitches.")
		self.caller.msg("Frank pulls out a shank and stabs you in the gut.")
		self.caller.msg("You lie there bleeding out as Frank runs around shouting.")
		self.caller.msg("|mFrank|n says: FRANK JUST STABBED SOMEONE!!! I LOVE SNITCHING!!!")
		results = search_object("#436")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)


class FrankCmdSet(CmdSet):
	key = "FrankCmdSet"
	def at_cmdset_creation(self):
		self.add(talkfrank())

class frank(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Frank the snitch twitches uncontrollably, like he's shaking waiting to say something."
		self.cmdset.add_default(FrankCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mFrank|n says: Did you hear the one about the person that got stabbed by a snitch in prison."