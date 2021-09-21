from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk receptionist"
	aliases = ["Talk Receptionist", "Talk receptionist", "talk Receptionist" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mReceptionist|n says: Welcome Agent %s, there's been a lot of talk about you around the water cooler. You can't IMAGINE the gossip around here, being a security agency and all, information is what we do." % (self.caller.key))
		self.caller.msg("|mReceptionist|n says: You'll find the agent registration, Q Branch, and Armory down the hallway.")
		self.caller.msg("|mReceptionist|n says: At the end of the hallway is the elevator, you'll be wanting the 34th Floor, you're up with the bigwigs.")
		self.caller.msg("|mReceptionist|n says: Stay safe out in the field, those spiced up fiends are always right around the corner, just waiting to tear into us. Shoot one for me, will ya?")
		self.caller.msg("The receptionist|n gives you a wink as he picks up the phone.")
		self.caller.msg("|mReceptionist|n says: National Spice Agency, this is Steve, are you calling to rat out a friend or loved one?")
		return

class ReceptionistCmdSet(CmdSet):
	key = "ReceptionistCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class receptionist(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The receptionist is dutifully answering phones and typing out paperwork."
		self.cmdset.add_default(ReceptionistCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mReceptionist|n says: I'm sorry, but you're not allowed behind the desk, please step away."