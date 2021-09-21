from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk agents"
	aliases = ["Talk Agents", "Talk agents", "talk Agents" ]
	auto_help = True
	def func(self):
		if self.caller.db.faction == "cartel":
			self.caller.msg("There is no one here by that name to talk to.")
			return
		if not self.caller.tags.get("suv"):
			self.caller.msg("There is no one here by that name to talk to.")
			return
		if not self.caller.tags.get("donniedead"):
			self.caller.msg("|/Agents Artis and Nubar, according to their ID's, step out of the SUV and approach, sunglasses on.")
			self.caller.msg("|mAgent Artis|n says: We just picked you two up on satellite a minute ago, sorry it took so long, we were grabbing some luke warm water.")
			self.caller.msg("|mAgent Nubar|n says: Hope we didn't leave you worrying, that'd be a terrible last feeling to have.")
			self.caller.msg("A wicked sneer climbs across Nubar's face as he draws his weapon and fires two rounds into Donnie's chest.")
			self.caller.msg("Shock slams into you like a freight train, kneeling on the ground next to Donnie, you're sure you're about to hear two more shots. They never come.")
			self.caller.msg("|mDonnie|n says: %s, quick I have something to tell you." % (self.caller.key))
			self.caller.tags.add("donniedead")
			return
		if self.caller.tags.get("donniedead") and self.caller.tags.get("finalwords"):
			self.caller.msg("|/|mAgent Artis|n says: It was a damn shame, always tough to put a fellow agent down.")
			self.caller.msg("|mAgent Artis|n says: We had confirmed intel that he had flipped sides and was working for the Vipers to pay for his spice addiction.")
			self.caller.msg("|mAgent Nubar|n says: Sad bastard was eating 2-3 ghost peppers a day like it was nothing.")
			self.caller.msg("|mAgent Artis|n says: Sorry about the run around on having you get him out, but a dead body in prison that had no record of being sent to prison raises flags, much cleaner this way.")
			self.caller.msg("|mAgent Nubar|n says: What the hell took you two so long to get here, you've been gone for like a month.")
			self.caller.msg("|mAgent Artis|n says: To catch you up, we finally got enough info to completely dismantle the Vipers, the coordinated raid happened last week.")
			self.caller.msg("|mAgent Artis|n says: Every last one of them, root to tip, in one fell swoop.")
			self.caller.msg("|mAgent Nubar|n says: There's talk of making it a national holiday.")
			self.caller.msg("|mAgent Nubar|n says: Well, standing here staring at a corpse ain't gonna keep this country spice free, let's get going, it's a long way back to HQ. Let's go get you your badge!")
			self.caller.msg("The blights blink and the SUV goes bleep bleep as it unlocks.")
			self.caller.tags.add("suvunlocked")
			return

class Agents2CmdSet(CmdSet):
	key = "Agents2CmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class agents2(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(Agents2CmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:attr(faction, fed) and tag(suv)")
		self.db.get_err_msg = "An empty field in the middle of nowhere, you're an escaped convict? Best keep your hands to yourself until you get your badge."