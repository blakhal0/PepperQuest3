from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk donnie"
	aliases = ["Talk Donnie", "Talk donnie", "talk Donnie" ]
	auto_help = True
	def func(self):
		if self.caller.db.faction == "cartel":
			self.caller.msg("There is no one here by that name to talk to.")
			return
		if self.caller.tags.get("finalwords"):
			self.caller.msg("|/You pull out a Ouija board and attempt to contact Donnie's spirit.")
			self.caller.msg("Not really, he's dead. Better to talk to the living.")
			return
		if not self.caller.tags.get("donniedead"):
			self.caller.msg("|/|mDonnie|n says: Wow, I can't believe we made it out of there.")
			self.caller.msg("|mDonnie|n says: There's no one here, I'm a bit relieved, look before anyone else gets here, I need to tell you something, just in case something happens to me.")
			self.caller.msg("|mDonnie|n says: I'm certain that either the Ghost Reapers have infiltrated the NSA, or we have a traitor.")
			self.caller.msg("|mDonnie|n says: I don't know who, but it has to be someone near the top. I'm pretty sure they killed my handler and was hoping that everyone would just forget about me in there.")
			self.caller.msg("|mDonnie|n says: There were are few more attempts on my life than normal the last couple of months from non cartel members.")
			self.caller.msg("|mDonnie|n says: Look, I imagine they kind of strong armed you into this, but if you want out I can....... a large black SUV pulls up and two agents step out.")
			self.caller.tags.add("suv")
			return
		else:
			self.caller.msg("|mDonnie|n coughs wheezes: Watch your back. My notebook, don't let them get it.")
			self.caller.msg("Donnie closes his eyes as his body goes limp.")
			self.caller.msg("You search Donnie's corpse for the notebook he had.")
			self.caller.msg("Blood soaked rice paper pages tear and fall apart as you carefully try to flip though.")
			self.caller.msg("You manage to view the writing on one page before it's destroyed 'The petrified fox does not fear trolls.'")
			self.caller.msg("|mAgent Nubar|n says: Hehe, look, the newby is gonna toss their cookies. Let us fill you in on what you don't know.")
			self.caller.tags.add("finalwords")
			return

class Donnie2CmdSet(CmdSet):
	key = "Donnie2CmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class donnie2(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(Donnie2CmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:attr(faction, fed)")
		self.db.get_err_msg = "You cannot get Donnie, he's too heavy."