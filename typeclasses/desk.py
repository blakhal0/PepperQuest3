from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class blueprints(default_cmds.MuxCommand):
	key = "get blueprints"
	aliases = ["get Blueprints", "Get Blueprints", "Get blueprints"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("blueprints"):
			self.caller.msg("You already took the blueprints.")
			return
		else:
			self.caller.msg("|/You carefully pick up the blueprints and stuff them in your waistband.")
			prints_proto = {
			"key": "Blueprints",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "Blueprints of the prison.",
			"location": self.caller
			}
			spawn(prints_proto)
			self.caller.tags.add("blueprints")
			return

class DeskCmdSet(CmdSet):
	key = "DeskCmdSet"
	def at_cmdset_creation(self):
		self.add(blueprints())
	
class desk(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/The old wooden desk has seen better days.|/You clear off a pile of old papers and see some blueprints."
		self.cmdset.add_default(DeskCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/As you grab the corner of the desk to lift up it crumbles and falls apart."