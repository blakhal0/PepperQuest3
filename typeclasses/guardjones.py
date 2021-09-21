from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk guard jones"
	aliases = ["Talk Jones", "Talk jones", "talk Jones", "talk jones", "Talk Guard Jones", "Talk guard jones", "Talk Guard jones", "Talk guard Jones", "talk Guard jones", "talk guard Jones" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mGuard Jones|n says: You got about 10 seconds to leave my sight before I beat you bloody inmate.")
		return

class collect(default_cmds.MuxCommand):
	key = "collect"
	aliases = ["Collect"]
	auto_help = False
	def func(self):
		if not self.caller.tags.get("debtcollector"):
			self.caller.msg("Command 'collect' is not available.")
			return
		self.caller.msg("|/|m%s|n says: Guard Jones, I'm here to collect." % (self.caller.key))
		self.caller.msg("|mGuard Jones|n says: I don't know what you're talking about, get the hell out of my face, I don't owe the vipers a damn thing.")
		self.caller.msg("|m%s|n says: Oh, I'm pretty sure you do. See your name was in the book when I first got it, but the second time I saw it, yours was the only name missing." % (self.caller.key))
		self.caller.msg("|m%s|n says: Now I know you and Nataly have some kind of agreement setup, and I'm going to overlook that, as long as you let our member out of solitary."  % (self.caller.key))
		self.caller.msg("|mGuard Jones|n says: ...So, you'll keep your mouth shut and leave the debt erased as long as I let a scumbag out of solitary, deal.")
		self.caller.tags.remove("debtcollector")
		self.caller.tags.add("blackmail")
		self.caller.tags.add("viewasset")
		self.caller.msg("You got the cartel member out of solitary, report back to Atropos.")
		return

class JonesCmdSet(CmdSet):
	key = "JonesCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(collect())
	
class guardjones(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Guard Jones is standing in the hallway, watching the prisoners with great disdain."
		self.cmdset.add_default(JonesCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mGuard Jones|n says: Looking to spend some time in solitary?"