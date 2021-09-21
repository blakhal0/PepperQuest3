from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk joliet jake"
	aliases = ["Talk Jake", "Talk jake", "talk Jake", "talk jake", "Talk Joliet Jake", "Talk joliet jake", "Talk Joliet jake", "Talk joliet Jake", "talk Joliet jake", "talk joliet Jake" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mJoliet Jake|n says: We're on a mission from god.")
		return

class collect(default_cmds.MuxCommand):
	key = "collect jake"
	aliases = ["Collect Jake", "Collect jake", "collect Jake", "Collect Joliet Jake", "Collect Joliet jake", "Collect joliet Jake", "collect joliet jake", "collect Joliet Jake", "collect Joliet jake", "collect joliet Jake"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("debtcollector"):
			self.caller.msg("Command 'collect' is not available.")
			return
		if self.caller.tags.get("debtcollected"):
			self.caller.msg("You've already collected the debt.")
			return
		if self.caller.tags.get("jakecollected"):
			self.caller.msg("You've already collected the debt.")
			return
		self.caller.msg("|/|m%s|n says: Joliet Jake, I'm here to collect." % (self.caller.key))
		self.caller.msg("|mJoliet Jake|n says: I was gonna pay. Honest... I ran out of gas. I... I had a flat tire. I didn't have enough money for cab fare. My tux didn't come back from the cleaners. An old friend came in from out of town. Someone stole my car. There was an earthquake. A terrible flood. Locusts! IT WASN'T MY FAULT, I SWEAR TO GOD!")
		if self.caller.tags.get("elwoodcollected") and self.caller.tags.get("sarahcollected"):
			self.caller.tags.remove("debtcollector")
			self.caller.tags.remove("elwoodcollected")
			self.caller.tags.remove("sarahcollected")
			self.caller.tags.add("debtcollected")
			self.caller.msg("|/|rYou've collected all the debts, report back to Atropos.|n")
			return
		self.caller.tags.add("jakecollected")
		self.caller.msg("Jake hands you the stamps, his debt is paid.")
		return

class JakeCmdSet(CmdSet):
	key = "JakeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(collect())
	
class jolietjake(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Joliet Jake is adjusting his black glasses and hat as he stands near the pulpit next to his bother preparing to play some music."
		self.cmdset.add_default(JakeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mJoliet Jake|n says: Hey, look, these suits aren't cheap!!"