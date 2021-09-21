from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class debris(default_cmds.MuxCommand):
	key = "scatter debris"
	aliases = ["Scatter Debris", "scatter Debris", "Scatter debris"]
	auto_help = False
	def func(self):
		if self.caller.search("Debris", location=self.caller, quiet=True):
			for o in self.caller.contents:
				if o.key == "Debris":
					o.delete()
			self.caller.db.debris += 1
			self.caller.msg("|/You make your way around the yard slowly scattering bits of the broken concrete.")
			self.caller.msg("Shaking your pant leg, you dust off the last few bits of debris, you're ready to get back to work.")
			return
		else:
			self.caller.msg("You don't have any debris to get rid of.")
			return

class DropDebrisCmdSet(CmdSet):
	key = "DropDebrisCmdSet"
	def at_cmdset_creation(self):
		self.add(debris())
	
class disposal(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(DropDebrisCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")
