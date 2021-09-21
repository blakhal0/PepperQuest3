from evennia import DefaultObject, default_cmds, CmdSet
from evennia.prototypes.spawner import spawn

class spwnsnacks(default_cmds.MuxCommand):
	key = "Get Spicy Panda Snacks"
	alias = ["get spicy panda snacks", "get snacks", "Get snacks", "get Snacks", "Get Snacks", "get panda snacks", "Get Panda Snacks"]
	auto_help = False
	def func(self):
		snacks_proto = {
			"key": "Spicy Panda Snacks",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A bag of tasty Spicy Panda Snacks.",
			"location": self.caller
			}
		if self.caller.search('Spicy Panda Snacks', location=self.caller, quiet=True):
			self.caller.msg("You already have the Spicy Panda Snacks.")
			return
		else:
			spawn (snacks_proto)
			self.caller.msg("You reach down and grab the Spicy Panda Snacks.")

class SpwnSnacksCmdSet(CmdSet):
	key = "SpwnSnacksCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(spwnsnacks())

class snacks(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "One package of Spicy Panda Snacks sits below the counter."
		self.locks.add("get:false()")
		self.locks.add("view:not holds(Spicy Panda Snacks)")
		self.cmdset.add_default(SpwnSnacksCmdSet, permanent=True)