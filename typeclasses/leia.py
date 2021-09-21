from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk leia"
	aliases = ["Talk leia", "Talk leia", "talk leia"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("conquerer") and self.caller.tags.get("distributor"):
			self.caller.msg("There is no one here by that name to talk to.")
			return
		if self.caller.tags.get("conquerer"):
			self.caller.msg("|/|mLeia|n says: %s, good work on claiming that disputed territory, everyone will know we run things in this town now." % (self.caller.key))
			projects = "distribute spice to our street level dealers."
		if self.caller.tags.get("distributor"):
			self.caller.msg("|/|mLeia|n says: %s, good work on getting that product out to the dealers, the people of this fair city will have tasty food once again!" % (self.caller.key))
			projects = "make our claim on disputed territory."
		if not self.caller.tags.get("conquerer") and not self.caller.tags.get("distributor"):
			projects = "distribute spice to our street level dealers and make our claim on disputed territory."
		self.caller.msg("|/|mLeia|n says: Welcome %s, The Moose sent word you were coming down, although I'm not sure why, I have things well under control here, but another set of hands for work and another strong back never hurts." % (self.caller.key))
		self.caller.msg("|mLeia|n says: In case you haven't heard, while you were locked up, the entire Naga Viper cartel got busted.")
		self.caller.msg("|mLeia|n says: Since then, there's been a bit of a power vacuum and we're looking to fill that void.")
		self.caller.msg("|mLeia|n says: We could really use your help to move things along, we need to %s" % (projects))
		self.caller.msg("|mLeia|n says: Talk to Eduardo and Natasha, they'll fill you in on the details.")
		if not self.caller.search("Pepper Spray", location=self.caller, quiet=True):
			self.caller.msg("|mLeia|n says: Oh, you'll want to take this with you.")
			self.caller.msg("Leia hands you a pepper spray device")
			self.caller.msg("|mLeia|n says: In case anyone causes you problems, or if you just want to distribute some 'Free Product' *wink wink*")
			spray_proto = {
			"key": "Pepper Spray",
			"typeclass": "typeclasses.mace.mace",
			"location": self.caller
			}
			spawn(spray_proto)
		return

class leiaCmdSet(CmdSet):
	key = "leiaCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class leia(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Leia is watching over the entire operation like a hawk. A hawk with a clipboard. Leia is in charge of the cartel for the USA."
		self.cmdset.add_default(leiaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(conquerer) or not tag(distributor)")
		self.tags.add("specialnpc")
		self.db.nomacemsg = "|/|mLeia|n says: Ohhhhh, hell yeah, that's the good shit right there."
		self.db.get_err_msg = "|/|mLeia|n says: Hey, hey, you see all the boxes getting packaged and sent out of here, I've got plenty enough to send you out in them also."