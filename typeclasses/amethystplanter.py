from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class obtain(default_cmds.MuxCommand):
	key = "Take Seed"
	aliases = ["take seed", "take Seed", "Take seed"]
	auto_help = True
	def func(self):
		if self.caller.search("Amethyst Seed", location=self.caller, quiet=True):
			self.caller.msg("|/You already have the amethyst seed.")
			return
		self.caller.msg("|/The Spiceronomicon begins to pulse and burn in the presence of the plant.")
		self.caller.msg("You reach out and take one of the seeds, a wave of burning pain runs through your body followed by a feeling of strength.")
		amethystseed_proto = {
		"key": "Amethyst Seed",
		"typeclass": "typeclasses.objects.nodropobj",
		"desc": "A glowing amethyst pepper seed.",
		"location": self.caller
		}
		spawn(amethystseed_proto)
		if self.caller.search("Emerald Seed", location=self.caller, quiet=True) and self.caller.search("Ruby Seed", location=self.caller, quiet=True) and self.caller.search("Citrine Seed", location=self.caller, quiet=True):
			self.caller.msg("|/You have gathered all of the sacred seeds.")
			return
		return

class ASeedCmdSet(CmdSet):
	key = "ASeedCmdSet"
	def at_cmdset_creation(self):
		self.add(obtain())
	
class amethystplanter(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/A tall marble planter stands in the middle of the room. A thriving plant with amethyst peppers stands thick and healthy in the planter.|/One of the peppers has split open, exposing the seeds.|/Having one of those seeds might come in handy."
		self.cmdset.add_default(ASeedCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You only need the seed, not the entire planter."