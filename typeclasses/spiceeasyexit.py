from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class enter(default_cmds.MuxCommand):
	key = "door"
	aliases = ["Door"]
	auto_help = False
	def func(self):
		target = self.caller.search("door")
		self.caller.msg("|/You stroll up to the door and knock|/A small metal shade slides open.")
		response = yield("Password? ")
		if response.lower() == "hand of glory":
			self.caller.msg("|/The metal shade slams shut.")
			yield 3
			self.caller.msg("*Shick, rattle, TONK, beep-beepbeep-beep, bttttz*")
			yield 3
			self.caller.msg("|/Finally the door opens.|/Welcome to the one and only Dark Alley Spice Easy, enjoy your time here.|/You walk in.")
			place = target.db.spiceeasy
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/The metal shade slams shut.")
			yield 3
			self.caller.msg("|/A slight smile cracks on the rocky features of the goon standing by the door as he grabs you.|/I bet I can throw you allll the way to the street.")
			self.caller.msg("A breeze ruffles your hair as you fly through the air landing harshly in the street.")
			place = target.db.street
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class EnterCmdSet(CmdSet):
	key = "EnterCmdSet"
	def at_cmdset_creation(self):
		self.add(enter())
	
class spiceeasyexit(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A heavy looking metal door with a small metal shade that slides open from the inside."
		self.db.spiceeasy = "#138"
		self.db.street = "#113"
		self.cmdset.add_default(EnterCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialexit")