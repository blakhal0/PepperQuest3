from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class talknick(default_cmds.MuxCommand):
	key = "talk nick"
	aliases = ["Talk Nick", "Talk nick", "talk Nick"]
	auto_help = True
	def func(self):
		if self.caller.search("Plastic", location=self.caller, quiet=True):
			self.caller.msg("|/|mNick|n whispers: Hey is that some plastic I see, that's just what I need to make some loaded dice.")
			dice_proto = {
			"key": "Loaded Dice",
			"typeclass": "typeclasses.objects.nodropobj",
			"desc": "A pair of loaded dice.",
			"location": self.caller
			}
			spawn(dice_proto)
			for o in self.caller.contents:
				if o.key == "Plastic":
					o.delete()
			self.caller.msg("Nick starts heating up and shaping a set of dice, occasionally tapping them on certain sides. They look exactly like the ones in the yard used for shooting dice.")
			self.caller.msg("|mNick|n whispers: Here, you should be able to roll for quite a while and win every time. Don't win too much, those inmates in the yard don't joke around.")
			return
		else:
			self.caller.msg("|mNick|n says: Stupid jerks, stealing all my stamps just because I'm good at dice, I'll get my revenge!")
			return

class NickCmdSet(CmdSet):
	key = "NickCmdSet"
	def at_cmdset_creation(self):
		self.add(talknick())

class nick(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Nick is standing in the showers, full dressed. His prickly name seems to mirror his demeanor."
		self.cmdset.add_default(NickCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mNick|n says: You do that again, and you're going to get busy dying real fast."


