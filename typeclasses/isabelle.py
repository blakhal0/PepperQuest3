from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk isabelle"
	aliases = ["Talk Isabelle", "Talk isabelle", "talk Isabelle"]
	auto_help = True
	def func(self):
		if self.caller.search("Blueprints", location=self.caller, quiet=True):
			for o in self.caller.contents:
				if o.key == "Blueprints" or o.key == "Maintenance Key":
					o.delete()
			self.caller.tags.remove("blueprints")
			self.caller.msg("|/You hand the blueprints to Isabelle.")
			self.caller.msg("|mIsabelle|n says: Give me that key too, you sure don't want to get caught with that on you.")
			self.caller.msg("You hand the Maintenance Key to Isabelle.")
			self.caller.msg("|mIsabelle|n says: This is perfect. Hummm, it looks like this place was originally intended to be three stories.")
			self.caller.msg("Isabelle taps the blueprints tracing a finger from one page to the other.")
			self.caller.msg("|mIsabelle|n says: And right here, looks like there's a big drain that connects to an old sewer in the morgue.")
			self.caller.msg("|mIsabelle|n says: I bet they never filled in the elevator shaft that was supposed to connect the second and third floor to the infirmary and morgue.")
			self.caller.msg("|mIsabelle|n says: ....and that shaft runs right behind cell 2B, that's your cell isn't it?")
			self.caller.msg("With a completely un-shocked look that normally comes from a plot reveal due to EXTREMELY LAZY AND RUSHED WRITING, you nod your head.")
			self.caller.msg("|mIsabelle|n says: So, if we can dig a hole in the back of your cell, we can get into the elevator shaft, into the elevator from the top access hatch, and then take it down to the morgue and into the sewer.")
			self.caller.msg("|m%s|n says: How the hell do you even know there's a way out of the sewer and it's not just some kind of hellscape of inexplicable traps and twisting turning maze like peril?" % (self.caller.key))
			self.caller.msg("|mIsabelle|n says: Sometimes you just gotta have faith.")
			self.caller.msg("|mIsabelle|n says: Ok, we're going to need a hammer to bust up the wall in your cell and a poster to cover up the hole, just like in shawshank. Go talk to Red request a hammer and a poster.")
			self.caller.msg("|mIsabelle|n says: Once you've got the Hammer and Poster you can start to |cBreak Out|n in your cell.")
			return
		if self.caller.tags.get("lucien") and self.caller.search("Maintenance Key", location=self.caller, quiet=True):
			self.caller.msg("|/|mIsabelle|n says: Hello %s, Jules says you're quite adept at obtaining difficult things." % (self.caller.key))
			self.caller.msg("|mIsabelle|n says: I need to know, are you any good at hide and seek?")
			self.caller.msg("|mIsabelle|n says: We need to get you and that info out of here and to home base in Montreal.")
			self.caller.msg("|mIsabelle|n says: I've got a plan, but I need a set of old blueprints to be sure.")
			self.caller.msg("|mIsabelle|n says: I've searched everywhere except the locked rooms.")
			self.caller.msg("|mIsabelle|n says: You happen to have a key to all those rooms.")
			self.caller.msg("|mIsabelle|n says: I need you to find those blueprints and bring them back to me to analyze for structural weaknesses.")
			self.caller.msg("|mIsabelle|n says: Well, what are you waiting for, go, seek, find.")
			return
		self.caller.msg("|/|mIsabelle|n says: Do not touch a thing, I'm a messy person, but flies are lucky.")
		return

class IsabelleCmdSet(CmdSet):
	key = "IsabelleCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class isabelle(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Despite her cell being an absolute trash heap, Isabelle herself is very sharply dressed, as much as one can be in an inmate uniform, with her hair neatly done in a complicated braid."
		self.cmdset.add_default(IsabelleCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mIsabelle|n says: DON'T SCARE MY FLIES AWAY!!!"