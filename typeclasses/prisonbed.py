from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class sleep(default_cmds.MuxCommand):
	"""
	Sleep.

	Usage:
	Sleep

	Sleep lightly, you never know if someone will attack you in here.
	"""
	key = "sleep"
	auto_help = True
	def func(self):
		target = self.caller.search("bed")
		if self.caller.search("Dream Spice", location=self.caller, quiet=True):
			for o in self.caller.contents:
				if o.key == "Dream Spice":
					o.delete()
			self.caller.msg("|/The dream spice glitters, reflecting rainbow hues. It makes little splashes as you dump it into a paper cup of water, dissolving instantly.|/Your mouth is on fire for just a few seconds as you swallow.|/You lay down on your bunk and relax.|/As you begin to drift into sleep, you begin to dream...|/")
			yield 3
			self.caller.msg("You find yourself in a strange and confusing place in the world of dreams.")
			place = self.caller.db.dreamreturn
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.db.sendback = target.db.sendback
			return
		else:
			self.caller.msg("|/You climb into your bunk and try to calm your mind and get some shuteye.|/Finally you manage to shut your eyes and drift off.")
			yield 3
			self.caller.msg("|/You wake up in a panic and take a look around to make sure you're safe.|/")
			return

class SleepCmdSet(CmdSet):
	key = "SleepCmdSet"
	def at_cmdset_creation(self):
		self.add(sleep())
	
class prisonbed(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An uncomfortable and slightly too small bunk bed is bolted to one wall.|/That's going to hurt your back without a doubt."
		self.db.sendback = "#292"
		self.cmdset.add_default(SleepCmdSet, permanent=True)
		self.locks.add("get:false()")