from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk natasha"
	aliases = ["Talk Natasha", "Talk natasha", "talk Natasha"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/|mNatasha|n says: We've got to get Pepperbot to the 9th Circle SpiceEasy, it's on the corner of 16th and Florida. Meet you there? Great. Look for the phone booth then just head in to |cThe 9th Circle|n.")
			return
		if self.caller.tags.get("conquerer") and self.caller.tags.get("distributor"):
			self.caller.msg("|/|mNatasha|n says: Hey %s, Leia had to take off for a meeting or something at the SpiceEasy." % (self.caller.key))
			self.caller.msg("|mNatasha|n says: Vivian needs some help to get Pepperbot ready for Bot Wars.")
			self.caller.msg("|mNatasha|n says: What? You've never heard of Bot Wars, it's THE ultimate test of engineering, two bots enter, one bot leaves. You can make some nice money betting on them too.")
			return
		if self.caller.tags.get("distributor") and not self.caller.tags.get("conquerer"):
			self.caller.msg("|/|mNatasha|n says: Good job, you've been promoted to senior delivery person in training. Hahaha, just kidding.")
			self.caller.msg("|mNatasha|n says: You've ensured that everyone in this town will get spice if they want it.")
			self.caller.msg("|mNatasha|n says: Eduardo says he needs someone with artistic skill to claim territory out on the streets. Go see if you can give him a hand.")
			return
		if self.caller.search("Product", location=self.caller, quiet=True):
			self.caller.msg("|/|mNatasha|n says: Get out there and resupply the dealers. Find one of our people and |cDistribute|n to them. Make sure to call them by name so they know who you're talking to.")
			return
		self.caller.msg("|/|mNatasha|n says: Hello, my name is Natasha.")
		self.caller.msg("|mNatasha|n says: I handle logistics, packaging, all that.")
		self.caller.msg("|mNatasha|n says: We're short a runner, I need someone to go resupply the local dealers. Here, take this.")
		product_proto = {
		"key": "Product",
		"typeclass": "typeclasses.product.product",
		"location": self.caller
		}
		spawn(product_proto)
		self.caller.msg("Natasha hands you several packages of product.")
		self.caller.msg("|mNatasha|n says: We've got people on Belmont Way just west of 16th and just east of 14th, in Peluca Alley between the overpasses, in Foxstone Park, and just west of 16th on Florida Ave.")
		self.caller.msg("|mNatasha|n says: You'll know them when you see them, just |cDistribute|n to the dealer, so Distribute Paul, for example.")
		self.caller.msg("|mNatasha|n says: Well, get to it!")
		return

class natashaCmdSet(CmdSet):
	key = "natashaCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class natasha(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Natasha is checking packages, re-weighing, and checking items off of a list on a clipboard."
		self.cmdset.add_default(natashaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mNatasha|n says: Just don't."
		self.db.nomacemsg = "|/|mNatasha|n says: Hey, hey, you can't just go freely distributing product in here like that. Get your head out of your ass."