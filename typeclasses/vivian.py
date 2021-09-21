from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk vivian"
	aliases = ["Talk Vivian", "Talk vivian", "talk Vivian"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("distributor"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
		if not self.caller.tags.get("conquerer"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/|mVivian|n says: It's time to get Pepperbot to the 9th Circle SpiceEasy, it's on the corner of 16th and Florida, look for the phone booth then just head in to |cThe 9th Circle|n. Pepperbot and I will meet you there!")
			return
		self.caller.msg("|/|mVivian|n says: DAMMIT!! Why the hell do you keep faulting??!?!?!")
		self.caller.msg("|mVivian|n says: Oh, hey %s, you know anything about electronics?" % (self.caller.key))
		self.caller.msg("|mVivian|n says: I'm trying to get Pepperbot ready for Bot Wars, but it keeps freaking faulting out on me, I need a smoke, take a look at it if you can |cFix Pepperbot|n.")
		self.caller.tags.add("botrepair")
		return

class vivianCmdSet(CmdSet):
	key = "vivianCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class vivian(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Vivian is working on an orange robot."
		self.cmdset.add_default(vivianCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:tag(distributor) and tag(conquerer)")
		self.db.get_err_msg = "|/Vivian stabs you with a screwdriver."
		self.db.nomacemsg = "|/|mVivian|n says: Please, I work around this stuff all day, that doesn't even phase me."