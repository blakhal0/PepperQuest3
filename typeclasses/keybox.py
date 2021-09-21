from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class get(default_cmds.MuxCommand):
	key = "get key"
	aliases = ["Get Key", "Get key", "get Key"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("gdistract"):
			self.caller.msg("|/|mGuard|n shouts: DROP THAT KEY RIGHT NOW SCUMBAG!!!")
			self.caller.msg("The guards dog pile on you and beat the hell out of you.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.tags.add("holdskey")
			self.caller.msg("|/You deftly swipe the key from the keybox while no one is looking.")
			return

class impression(default_cmds.MuxCommand):
	key = "make impression"
	aliases = ["Make Impression", "Make impression", "make Impression"]
	auto_help = False
	def func(self):
		if not self.caller.search("Soap", location=self.caller, quiet=True):
			self.caller.tags.remove("holdskey")
			self.caller.msg("|/You somehow managed to drop the soap. Idiot. Go get another one.")
			return
		if not self.caller.tags.get("gdistract"):
			self.caller.tags.remove("holdskey")
			self.caller.msg("|/|mGuard|n shouts: DROP THAT KEY RIGHT NOW SCUMBAG!!!")
			self.caller.msg("The guards dog pile on you and beat the hell out of you.")
			for o in self.caller.contents:
				if o.key == "Soap":
					o.delete()
			self.caller.msg("The guards find the soap impression and confiscate it.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/You press the key into the soap, making a perfect impression.")
			return

class putback(default_cmds.MuxCommand):
	key = "return key"
	aliases = ["Return Key", "Return key", "return Key"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("gdistract"):
			self.caller.tags.remove("holdskey")
			self.caller.msg("|/|mGuard|n shouts: DROP THAT KEY RIGHT NOW SCUMBAG!!!")
			self.caller.msg("The guards dog pile on you and beat the hell out of you.")
			for o in self.caller.contents:
				if o.key == "Soap":
					o.delete()
			self.caller.msg("The guards find the soap impression and confiscate it.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.tags.remove("gdistract")
			self.caller.tags.remove("holdskey")
			self.caller.msg("|/You smoothly return the key to the keybox while no one is looking and take your leave of the guard room.")
			self.caller.msg("You have successfully made a mold of the key, take it back to Jules.")
			impression_proto = {
			"key": "Key Impression",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "An impression of a key in soap.",
			"location": self.caller
			}
			spawn(impression_proto)
			for o in self.caller.contents:
				if o.key == "Soap":
					o.delete()
			results = search_object("#359")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class KeyBoxCmdSet(CmdSet):
	key = "KeyBoxCmdSet"
	def at_cmdset_creation(self):
		self.add(get())
		self.add(impression())
		self.add(putback())

class keybox(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A keybox with a single key is hanging on the wall with the door wide open.|/Inside you can see a single key with an M on it."
		self.cmdset.add_default(KeyBoxCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You're going to want to be real careful taking things in here!!"