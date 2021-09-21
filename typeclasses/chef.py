from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class cook(default_cmds.MuxCommand):
	key = "talk chef"
	aliases = ["Talk Chef", "Talk chef", "talk Chef"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("doordash"):
			self.caller.msg("|/|mChef|n says: I'm busy cooking, you want to go back to eating the crap everyone else eats? Yeah, thought so. Leave me alone.")
			return
		if self.caller.tags.get("foodrace"):
			self.caller.msg("|/|mChef|n says: You're wasting time, I'd haul ass if I were you!!")
			return
		else:
			self.caller.msg("|/|mChef|n says: So you're the new recruit eh? I remember my first days here, killed 5 people to get this job.")
			self.caller.msg("|mChef|n says: And they never found the bodies. But those days are long past.")
			self.caller.msg("Chef flashes a grin.")
			self.caller.msg("|mChef|n says: You must be here to take food up to the boss? It's all ready to go.")
			food_proto = {
			"key": "Food",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A covered tray that smells better than anything you've had in weeks.",
			"location": self.caller
			}
			spawn(food_proto)
			self.caller.tags.add("foodrace")
			self.caller.msg("|mChef|n says: The boss gets pissed if the food is cold, I'd move like your life depends on it... because it might.")
			self.caller.msg("|mChef|n says: Atropos is in the middle cell on our side of the block, Cell 10B")
			self.caller.msg("Chef hands you the food, get it to the boss before it gets cold.")
			yield 30
			if not self.caller.tags.get("foodrace"):
				return
			else:
				self.caller.msg("|/|rThe food is getting cold, better move it!|n")
			yield 20
			if not self.caller.tags.get("foodrace"):
				return
			else:
				self.caller.msg("|/|rThe food is getting cold, better move it!|n")
			yield 15
			if not self.caller.tags.get("foodrace"):
				return
			else:
				self.caller.msg("|/|rThe food is cold, the boss is pissed, better go back and get a new tray.|n")
				self.caller.tags.remove("foodrace")
				for o in self.caller.contents:
					if o.key == "Food":
						o.delete()
				return

class ChefCmdSet(CmdSet):
	key = "ChefCmdSet"
	def at_cmdset_creation(self):
		self.add(cook())
	
class chef(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Chef is busy working over his personal area of the kitchen making food for the rest of the Naga Vipers.|/There's bound to be a lot of stories behind the scars on his face."
		self.cmdset.add_default(ChefCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "The other inmates would never notice a little soylent green in the meal."