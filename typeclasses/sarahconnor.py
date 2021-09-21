from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk sarah connor"
	aliases = ["Talk Sarah", "Talk sarah", "talk Sarah", "talk sarah", "Talk Sarah Connor", "Talk sarah connor", "Talk Sarah connor", "Talk sarah Connor", "talk sarah connor", "talk sarah Connor" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mSarah Connor|n says: JUDGEMENT DAY IS COMING!! THE ROOMBA'S ARE TRYING TO CLEAN THE FACE OF THE EARTH OF HUMANS! WE MUST STOP MEDICAL MECHANICA!")
		return

class collect(default_cmds.MuxCommand):
	key = "collect sarah"
	aliases = ["Collect Sarah", "Collect sarah", "collect Sarah", "Collect Sarah Connor", "Collect Sarah connor", "Collect sarah Connor", "collect sarah connor", "collect Sarah Connor", "collect Sarah connor", "collect sarah Connor"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("debtcollector"):
			self.caller.msg("Command 'collect' is not available.")
			return
		if self.caller.tags.get("debtcollected"):
			self.caller.msg("You've already collected the debt.")
			return
		if self.caller.tags.get("sarahcollected"):
			self.caller.msg("You've already collected the debt.")
			return
		self.caller.msg("|/|m%s|n says: Sarah Connor, I'm here to collect." % (self.caller.key))
		self.caller.msg("|mSarah Connor|n says: None of this will matter. You think some stamps are going to stop the robot apocalypse??")
		self.caller.msg("Sarah laughs wildly.")
		self.caller.msg("|m%s|n says: I'll make sure to unplug my toaster before I go to bed, just pay up." % (self.caller.key))
		if self.caller.tags.get("elwoodcollected") and self.caller.tags.get("jakecollected"):
			self.caller.tags.remove("debtcollector")
			self.caller.tags.remove("elwoodcollected")
			self.caller.tags.remove("jakecollected")
			self.caller.tags.add("debtcollected")
			self.caller.msg("|/|rYou've collected all the debts, report back to Atropos.|n")
			return
		self.caller.tags.add("sarahcollected")
		self.caller.msg("Sarah struggles and fights trying to reach her pocket while restrained but eventually manages to get you the stamps, her debt is paid.")
		return

class SarahCmdSet(CmdSet):
	key = "SarahCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(collect())
	
class sarahconnor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Sarah Connor is strapped to a hospital bed. Wild eyed, she thrashes and fights the straps muttering about robots."
		self.cmdset.add_default(SarahCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mSarah Connor|n says: I've destroyed killer robots from the future and I'LL KILL YOU TOO!!"