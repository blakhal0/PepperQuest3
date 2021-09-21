from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk elwood blues"
	aliases = ["Talk Elwood", "Talk elwood", "talk Elwood", "talk elwood", "Talk Elwood Blues", "Talk elwood blues", "Talk Elwood blues", "Talk elwood Blues", "talk Elwood blues", "talk elwood Blues" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mElwood Blues|n says: I traded in my Cadillac for this microphone.")
		answer = yield("Did you have something you want to ask Elwood?")
		if self.caller.tags.get("apostle"):
			if "cult" in answer or "order" in answer or "ring" in answer or "burning" in answer:
				self.caller.msg("|/|mElwood Blues|n says: If you seek knowledge, |cConfess|n to the minister.")
				return
		self.caller.msg("|mElwood Blues|n says: I have no idea what you're talking about kid. Beat it, we've got a gig.")
		return

class collect(default_cmds.MuxCommand):
	key = "collect elwood"
	aliases = ["Collect Elwood", "Collect elwood", "collect Elwood", "Collect Elwood Blues", "Collect Elwood blues", "Collect elwood Blues", "collect elwood blues", "collect Elwood Blues", "collect Elwood blues", "collect elwood Blues"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("debtcollector"):
			self.caller.msg("Command 'collect' is not available.")
			return
		if self.caller.tags.get("debtcollected"):
			self.caller.msg("You've already collected the debt.")
			return
		if self.caller.tags.get("elwoodcollected"):
			self.caller.msg("You've already collected the debt.")
			return
		self.caller.msg("|/|m%s|n says: Elwood Blues, I'm here to collect." % (self.caller.key))
		self.caller.msg("|mElwood Blues|n says: It's 106 miles to Chicago, we got a full tank of gas, half a pack of cigarettes, it's dark... and we're wearing sunglasses.")
		self.caller.msg("|m%s|n says: Yeah, that's great, just pay up." % (self.caller.key))
		if self.caller.tags.get("jakecollected") and self.caller.tags.get("sarahcollected"):
			self.caller.tags.remove("debtcollector")
			self.caller.tags.remove("jakecollected")
			self.caller.tags.remove("sarahcollected")
			self.caller.tags.add("debtcollected")
			self.caller.msg("|/|rYou've collected all the debts, report back to Atropos.|n")
			return
		self.caller.tags.add("elwoodcollected")
		self.caller.msg("Elwood hands you the stamps, his debt is paid.")
		return

class ElwoodCmdSet(CmdSet):
	key = "ElwoodCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(collect())
	
class elwoodblues(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Elwood Blues is finishing up a piece of dry white toast, no butter, no jam, just toasted white bread."
		self.cmdset.add_default(ElwoodCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mElwood Blues|n says: Ow, you fat penguin!"