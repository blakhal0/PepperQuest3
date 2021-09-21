from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class windowview(default_cmds.MuxCommand):
	"""
	Look Window

	Usage:
	Look Window

	Look out the window.
	"""
	key = "Look Window"
	aliases = ["l window"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("noleave"):
			target = self.caller.search("Window")
			self.caller.tags.add("holding")
			self.caller.msg("|/You pull the curtain aside and look out the window.|/The street is swarming with heavily armored NSA agents!!!|/You give a yell and Luke and Renee are at your side immediately.")
			yield 5
			self.caller.msg("|/HOLY SHIT, THEY'RE RAIDING OUR APARTMENT!!! screams Luke.|/Luke shoves a baggy full of ground up peppers into your hands.")
			yield 5
			self.caller.msg("|/You look down at your hands holding a felony level amount of spice.|/An agent with a battering ram is charging towards the door with several other goons hot on their heels.|/...fuck")
			yield 7
			self.caller.msg("|/QUICK!! THE TOILET!! |bFlush the Stash|n!!")
			yield 5
			self.caller.msg("|/The front door explodes as the agents pour into the house, weapons leveled and screaming.")
			yield 4
			self.caller.msg("|/GET ON THE GOD DAMN GROUND NOW SHITBAGS!! HANDS!! SHOW ME HANDS!!!!|/YOU, YOU MOVE AGAIN AND I'LL SHOOT YOU IN THE FACE!!")
			if self.caller.tags.get("gotawayclean"):
				self.caller.msg("The agents kick open the bathroom door and throw you to the ground.|/As they're screaming orders and handcuffing you, a rifle butt smashes into your face. The world goes grey...")
				self.caller.msg("|/|rYou've been arrested, but at least you flushed the stash.|n|/")
				self.caller.tags.remove("noleave")
				self.caller.tags.remove("holding")
				place = target.db.jaillocation
				results = search_object("%s" % (place))
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			self.caller.msg("|/WE'VE GOT A RUNNER!! SOMEONE GET THAT SCUMBAG!")
			yield 4
			self.caller.msg("|/Where's the spice?? *SMASH* MAKE THIS EASY ON YOURSELVES!*SMASH CRASH*")
			if self.caller.tags.get("gotawayclean"):
				self.caller.msg("The agents kick open the bathroom door and throw you to the ground.|/As they're screaming orders and handcuffing you, a rifle butt smashes into your face. The world goes grey...")
				self.caller.msg("|/|rYou've been arrested, but at least you flushed the stash.|n|/")
				self.caller.tags.remove("noleave")
				self.caller.tags.remove("holding")
				place = target.db.jaillocation
				results = search_object("%s" % (place))
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			yield 3
			self.caller.msg("|/You hear Luke and Renee screaming and pleading as the NSA agents start smashing everything, searching the house.")
			if self.caller.tags.get("gotawayclean"):
				self.caller.msg("The agents kick open the bathroom door and throw you to the ground.|/As they're screaming orders and handcuffing you, a rifle butt smashes into your face. The world goes grey...")
				self.caller.msg("|/|rYou've been arrested, but at least you flushed the stash.|n|/")
				self.caller.tags.remove("noleave")
				self.caller.tags.remove("holding")
				place = target.db.jaillocation
				results = search_object("%s" % (place))
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			yield 3
			if self.caller.tags.get("gotawayclean"):
				self.caller.msg("|/The agents kick open the bathroom door and throw you to the ground.|/As they're screaming orders and handcuffing you, a rifle butt smashes into your face. The world goes grey...")
				self.caller.msg("|/|rYou've been arrested, but at least you flushed the stash.|n|/")
				self.caller.tags.remove("noleave")
				self.caller.tags.remove("holding")
				self.caller.tags.remove("bubsdone")
				place = target.db.jaillocation
				results = search_object("%s" % (place))
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			else:
				self.caller.tags.add("caught")
				self.caller.msg("|/A screaming mad agent tackles you with the spice still in your hands before you can flush it down the toilet.|/As more agents pile on top of you, a rifle butt smashes into your face. The world goes grey...")
				self.caller.msg("|/|rYou've been arrested with a felony amount of spice in your possession.|n|/")
				self.caller.tags.remove("noleave")
				self.caller.tags.remove("holding")
				self.caller.tags.remove("bubsdone")
				place = target.db.jaillocation
				results = search_object("%s" % (place))
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
		else:
			self.caller.msg("|/You pull the curtain aside and look out the window.|/The neighborhood is lively with the usual rabble.")
			return

class WindowCmdSet(CmdSet):
	key = "WindowCmdSet"
	def at_cmdset_creation(self):
		self.add(windowview())
	
class window(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.jaillocation = "#2"
		self.cmdset.add_default(WindowCmdSet, permanent=True)
		self.locks.add("get:false()")