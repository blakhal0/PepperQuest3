from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk clerk"
	aliases = ["Talk Clerk", "Talk clerk", "talk Clerk" ]
	auto_help = True
	def func(self):
		if not self.caller.search("NSA Badge", location=self.caller, quiet=True):
			if self.caller.tags.get("donniedead"):
				self.caller.tags.remove("donniedead")
			if self.caller.tags.get("finalwords"):
				self.caller.tags.remove("finalwords")
			if self.caller.tags.get("suv"):
				self.caller.tags.remove("suv")
			if self.caller.tags.get("suvunlocked"):
				self.caller.tags.remove("suvunlocked")
			self.caller.msg("|/|mClerk|n says: Welcome Agent %s, let's get you squared away." % (self.caller.key))
			self.caller.msg("|mClerk|n says: One pair of sunglasses, black.")
			self.caller.msg("|mClerk|n says: One standard suit, black.")
			self.caller.msg("|mClerk|n says: One pair of shoes, black.")
			self.caller.msg("|mClerk|n says: Please step over here.... and don't smile... hold that. *click* *whrrrrr* not the most photogenic eh? I've seen worse, this'll work for your ID.")
			self.caller.msg("|mClerk|n says: One NSA ID badge and shield.")
			self.caller.msg("The clerk hands you the stack of items that makes up your uniform.")
			badge_proto = {
			"key": "NSA Badge",
			"typeclass": "typeclasses.objects.nodropobj",
			"location": self.caller,
			"desc": "Agent %s National Spice Agency." % (self.caller.key)
			}
			spawn(badge_proto)
			self.caller.msg("You step into a changing room and put on the last suit you'll ever wear and emerge... %s, agent of the National Spice Agency." % (self.caller.key))
		else:
			self.caller.msg("|/|mClerk|n says: Agent %s, you've already received your suit, shoes, sunglasses, and badge. Get out there and help keep the country safe!" % (self.caller.key))
			return

class ClerkCmdSet(CmdSet):
	key = "ClerkCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class nsaclerk(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The clerk waits patiently, tapping a pen on a clipboard."
		self.cmdset.add_default(ClerkCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mClerk|n says: I'm sorry, but you're not allowed behind the desk, please step away."