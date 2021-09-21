from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk zoe"
	aliases = ["Talk Zoe", "Talk zoe", "talk Zoe" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("zoedone"):
			self.caller.msg("Zoe has already left to hop the next train.")
			return
		self.caller.msg("|/|mZoe|n says: Welcome to Montreal %s, you'll find many friends here." % (self.caller.key))
		self.caller.msg("|mZoe|n says: You need to get that information to The Moose, the leader of the cartel.")
		self.caller.msg("|mZoe|n says: Our headquarters are the FMB Exports office, it's north and west from here.")
		self.caller.msg("|mZoe|n says: I have to go, the next train I need to hop is leaving very soon. Don't delay, unless it's for a dish of poutine.")
		self.caller.msg("|mZoe|n says: I've ordered up a cab for you, it'll drop you off right out front.")
		self.caller.msg("|mZoe|n says: I hope to see you again, so I will not say adieu, SALUT!")
		self.caller.msg("Zoe takes off in a sort of skipping run.")
		self.caller.msg("You're on your own, best get to headquarters.")
		self.caller.tags.add("zoedone")

class ZoeCmdSet(CmdSet):
	key = "ZoeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class zoemon(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Zoe stands in the train yard, studying a map and a schedule."
		self.cmdset.add_default(ZoeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:not tag(zoedone)")
		self.db.get_err_msg = "|/|mZoe|n says: I can just as easily say you never made it out of the sewers..."