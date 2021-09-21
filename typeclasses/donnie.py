from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk donnie"
	aliases = ["Talk Donnie", "Talk donnie", "talk Donnie" ]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("viewasset"):
			self.caller.msg("There's no one here by that name.")
			return
		self.caller.msg("|/|mDonnie|n says: I hear I have you to thank for getting my out of the hole. Thank you, I'm sure you know how horrible it is.")
		answer = yield("|mDonnie|n says: Is there something you want to ask me?")
		if answer.lower() in ["i have been sent by the penguin", "penguin"]:
			self.caller.tags.add("assetfound")
			self.caller.msg("|/|mDonnie|n says: Well, let's take a waddle then.")
			self.caller.msg("|mDonnie|n says: My names Brasco, Donnie Brasco.")
			self.caller.msg("|mDonnie|n says: It's about damn time you a-holes sent someone. Look, I got some seriously heavy info here.")
			self.caller.msg("|mDonnie|n says: I've managed to get a full map of the Ghost Reapers hierarchy and enough on the Naga Vipers to bring the entire cartel down.")
			self.caller.msg("|mDonnie|n says: Look, we gotta get this info out of here and into the right hands.")
			self.caller.msg("Donnie pulls out a small notebook and taps it.")
			self.caller.msg("|mDonnie|n says: You're bound to have a handler or contact or something, get to them now and get us a way out of here.")
			self.caller.msg("|/|rYou have identified the asset, you need to debrief.|n")
			return
		else:
			self.caller.msg("|/|mDonnie|n says: I don't really know about all that. Don't you have something else to be doing?")
			return

class pills(default_cmds.MuxCommand):
	key = "swallow pills"
	aliases = ["Swallow Pills", "swallow Pills", "Swallow pills" ]
	auto_help = False
	def func(self):
		if not self.caller.search("Poison Pills", location=self.caller, quiet=True):
			self.caller.msg("Command 'Poison Pills' is not available.")
			return
		if not self.caller.tags.get("ruckus"):
			self.caller.msg("|/If you take the pills now, no one will know you're 'dead' and you'll probably die for real.|/You need someone to make a ruckus on the second floor so that the guards will find your bodies.")
			return
		if self.caller.tags.get("ruckus"):
			self.caller.tags.remove("ruckus")
			for o in self.caller.contents:
				if o.key == "Poison Pills":
					o.delete()
				if o.key == "Shank":
					o.delete()
				if o.key == "Loaded Dice":
					o.delete()
				if o.key == "Prison Wallet":
					o.delete()
				if o.key == "Plastic":
					o.delete()
			self.caller.msg("|/|mDonnie|n says: You're sure about this? I've spent a lot of time getting this info and if I die before I get out of here, I'm going to be pissed.")
			self.caller.msg("|m%s|n says: I don't really see that we have a lot of choice." % (self.caller.key))
			self.caller.msg("Donnie nods and chuckles.")
			self.caller.msg("|mDonnie|n says: When you're right you're right.")
			self.caller.msg("Donnie and you lock eyes for a minute, cheers each other, and swallow the pills.")
			self.caller.msg("You both go pale, sag, and hit the floor, in your last seconds of consciousness you hear the guards come in and start yelling for help.")
			self.caller.msg("You come to on a cold stainless steel table in a dark and damp room.")
			self.caller.tags.remove("atroposdone")
			self.caller.tags.remove("assetfound")
			self.caller.tags.remove("butterfly")
			self.caller.tags.remove("dayroom")
			self.caller.tags.remove("doordash")
			self.caller.tags.remove("gotawayclean")
			self.caller.tags.remove("busted")
			self.caller.tags.remove("natalydone")
			self.caller.tags.remove("viewasset")
			results = search_object("#447")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class DonnieCmdSet(CmdSet):
	key = "DonnieCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(pills())

class donnie(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Donnie looks very nervous, pacing back and forth in the cell."
		self.cmdset.add_default(DonnieCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:tag(viewasset)")
		self.db.get_err_msg = "|/|mDonnie|n says: I just got out of the hole, don't make me go back."