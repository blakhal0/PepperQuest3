from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class sleep(default_cmds.MuxCommand):
	"""
	Sleep.

	Usage:
	Sleep

	You've had a rough day, time to relax and catch some z's.
	"""
	key = "sleep"
	auto_help = True
	def func(self):
		target = self.caller.search("bed")
		if self.caller.search("Dream Spice", location=self.caller, quiet=True):
			for o in self.caller.contents:
				if o.key == "Dream Spice":
					o.delete()
			self.caller.msg("|/The dream spice glitters, reflecting rainbow hues. It makes little splashes as you dump it into some tea, dissolving instantly.|/Your mouth is on fire for just a few seconds as you swallow.|/You lay down on your bed and relax.|/As you begin to drift into sleep, you begin to dream...|/")
			yield 3
			self.caller.msg("You find yourself in a strange and confusing place in the world of dreams.")
			place = self.caller.db.mazelocation
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.db.sendback = target.db.sendback
			return
		else:
			self.caller.msg("|/You flop into bed and lay your weary head down.|/You think to yourself, 'I wonder what it'd be like to live and work up on the deathstar. To grow up inside a vast, corrupt, and evil empire...'")
			yield 3
			self.caller.msg("|/You wake up from your nap with vague memories of worrying dreams.|/")
			return

class SleepCmdSet(CmdSet):
	key = "SleepCmdSet"
	def at_cmdset_creation(self):
		self.add(sleep())
	
class bed(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A comfy inviting bed with Star Wars themed sheets.|/Maybe you should get some sleep."
		self.db.sendback = "#33"
		self.cmdset.add_default(SleepCmdSet, permanent=True)
		self.locks.add("get:false()")