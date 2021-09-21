from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk eduardo"
	aliases = ["Talk Eduardo", "Talk eduardo", "talk Eduardo"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/|mEduardo|n says: We've got to get Pepperbot to the 9th Circle SpiceEasy, it's on the corner of 16th and Florida. Meet you there? Great. Look for the phone booth then just head in to |cThe 9th Circle|n.")
			return
		if self.caller.tags.get("conquerer") and self.caller.tags.get("distributor"):
			self.caller.msg("|/|mEduardo|n says: Hey %s, Leia had to take off for a meeting or something at the SpiceEasy." % (self.caller.key))
			self.caller.msg("|mEduardo|n says: Vivian needs some help to get Pepperbot ready for Bot Wars.")
			self.caller.msg("|mEduardo|n says: What? You've never heard of Bot Wars, it's THE ultimate test of engineering, two bots enter, one bot leaves. You can make some nice money betting on them too.")
			return
		if self.caller.tags.get("conquerer") and not self.caller.tags.get("distributor"):
			self.caller.msg("|/|mEduardo|n says: I have to say, your talent with a paint can *MUAH* amazing.")
			self.caller.msg("|mEduardo|n says: You've ensured that everyone in this town knows who's in charge.")
			self.caller.msg("|mEduardo|n says: Natasha says she needs a reliable person to distribute product out to the street dealers, the last person got picked up by the NSA, so we're short a runner.")
			for o in self.caller.contents:
				if o.key == "Spray Paint":
					o.delete()
			return
		if self.caller.search("Spray Paint", location=self.caller, quiet=True):
			self.caller.msg("|/|mEduardo|n says: Let your artistic side run wild, go out there and |cClaim Territory|n on any place that has a Naga Vipers logo on it.")
			return
		self.caller.msg("|/|mEduardo|n says: Hello, my name is Eduardo Kobra.")
		self.caller.msg("|mEduardo|n says: We need to claim some territory now that the Naga Vipers have been wiped out.")
		self.caller.msg("|mEduardo|n says: Here's some Spray Paint, you're already familiar with our logo. Go find anything that's tagged with Naga Vipers stuff and paint over it.")
		self.caller.msg("|mEduardo|n says: We need to let EVERYONE know that we own this town.")
		self.caller.msg("|mEduardo|n says: When you find a Naga Vipers logo, just |cClaim Territory|n to take it over.")
		paint_proto = {
		"key": "Spray Paint",
		"typeclass": "typeclasses.spraypaint.spraypaint",
		"desc": "Rattle cans of paint in cartel colors.",
		"location": self.caller
		}
		spawn(paint_proto)
		return

class eduardoCmdSet(CmdSet):
	key = "eduardoCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class eduardo(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Eduardo is creating a massive pepper themed mural on one of the walls of the warehouse."
		self.cmdset.add_default(eduardoCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mEduardo|n says: With just a lighter, this paint can turns into a flame thrower."