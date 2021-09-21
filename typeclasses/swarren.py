from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class south(default_cmds.MuxCommand):
	key = "south"
	aliases = ["South", "south", "s", "S"]
	auto_help = False
	def func(self):
		places = ["#2264", "#2411", "#2441", "#2292", "#2340", "#2387", "#2531", "#2519", "#2477"]
		phrases = ["|/A low rumble of tiny scurrying feet echos in the sewer.", "|/STOP! I am the Rat King and you have disturbed by domain, your life belongs to me!!", "|/Wander forever, but YOU'LL NEVER GET OUT HAHAHAHAHA.", "|/'Oh, hey look, cheese', you pick up the cheese.", "|/THERE THEY ARE, GET THEM MY FURRY MINIONS!!!", "|/Something tells me you're a very under-rat-ed person.", "|/Squeek, squeek squeek!!", "|/Cong-RAT-ulations!"]
		dest = random.choice(places)
		self.caller.msg(random.choice(phrases))
		self.caller.msg("You are swarmed by rats and carried off to their den.")
		results = search_object("%s" % (dest))
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class sWarrenCmdSet(CmdSet):
	key = "sWarrenCmdSet"
	def at_cmdset_creation(self):
		self.add(south())

class sexit(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(sWarrenCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialexit")