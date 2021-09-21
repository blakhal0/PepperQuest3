from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk fahad"
	aliases = ["Talk Fahad", "Talk fahad", "talk Fahad"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("fahad"):
			self.caller.msg("|mFahad|n says: Now that you have ze funds, talk to Lucien in 5B, he's ze leader of the Faucheurs Fantomes in zis place.")
			return
		if self.caller.search("Heist Loot", location=self.caller, quiet=True):
			self.caller.msg("|/|mFahad|n says: You mock Fahad and ze plan, now Fahad does the laughing!!")
			self.caller.msg("|mFahad|n says: Give me ze invention and ze loot. Here, you get half, 20 books of stamps.")
			for o in self.caller.contents:
				if o.key == "Heist Loot":
					o.delete()
				if o.key == "Sticky Hand":
					o.delete()
			self.caller.db.stamps += 20
			self.caller.tags.add("fahad")
			self.caller.msg("|mFahad|n says: Now that you have ze funds, talk to Lucien in 5B, he's ze leader of the Faucheurs Fantomes in zis place.")
			return
		if self.caller.search("Sticky Hand", location=self.caller, quiet=True):
			self.caller.msg("|/|mFahad|n says: You have ze sticky hand, go go go, go perform ze heist!")
			return
		self.caller.msg("|/|mFahad|n says: I really like ze old movies, especially heist films.")
		self.caller.msg("Fahad takes a long drag on his cigarette.")
		self.caller.msg("|mFahad|n says: Zis is how I end up in zis hole of the shit.")
		self.caller.msg("|mFahad|n says: I work with zome maybe not reliable peoplez. Ze heist goes bad, zey all turn on Fahad.")
		if not self.caller.tags.get("jules"):
			self.caller.msg("|mFahad|n says: Zo, now I only work with peoples that are reliable. I do not know you are reliable.")
			self.caller.msg("|mFahad|n says: Go prove you are reliable, then come work with Fahad and we will do a great heist.")
			return
		self.caller.msg("Fahad pulls you close.")
		self.caller.msg("|mFahad|n says: You are one of us, zo you are reliable.")
		self.caller.msg("|mFahad|n says: Zis is my plan for ze grand heist.")
		self.caller.msg("|mFahad|n says: Ze Naga Vipers are lazy and sloppy with their stamps zey keep in Cell 1B and we will steal zem.")
		self.caller.msg("|mFahad|n says: I have been working on zis invention for a long time, I call them ze Sticky Hand.")
		self.caller.msg("|m%s|n says: Wait, you want me use one of those little toy stretchy sticky hands? THAT'S your great plan??" % (self.caller.key))
		self.caller.msg("|m%s|n says: So, I get the sticky hand, then... then what, just snipe it though the cell door and use it to |cSteal|n the stamps?" % (self.caller.key))
		self.caller.msg("|mFahad|n says: ....yes. Zis is ze plan, it is a good and simple plan. I've worked on zis for many many yearz.")
		self.caller.msg("|m%s|n says: *sigh* Ok Fahad, I think I know how you ended up in here. Give me the sticky hand." % (self.caller.key))
		hand_proto = {
		"key": "Sticky Hand",
		"typeclass": "typeclasses.objects.nodropobj",
		"desc": "A sticky hand, like from the toy vending machines.",
		"location": self.caller
		}
		spawn(hand_proto)
		self.caller.msg("Fahad hands you the Sticky Hand. Go |cSteal|n the stamps from the Naga Vipers in 1B.")
		return

class FahadCmdSet(CmdSet):
	key = "FahadCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class fahad(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Fahad looks up at you through a cloud of cigarette smoke, 'You need stamps, I have a plan'."
		self.cmdset.add_default(FahadCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/Fahad says nothing, just stares at you with ice cold eyes."