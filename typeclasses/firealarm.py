from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class pull(default_cmds.MuxCommand):
	key = "Pull Fire Alarm"
	aliases = ["Pull Fire alarm", "Pull fire Alarm", "pull Fire Alarm", "Pull fire alarm", "pull Fire Alarm", "pull Fire alarm", "pull fire Alarm", "pull fire alarm"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You pull the fire alarm, instantly sirens are blaring and lights are flashing.")
		self.caller.msg("A drenching rain pours down from the overhead sprinklers, knocking trash over, blocking the exits. You're trapped!!")
		self.caller.msg("The water rises quickly as you and the guards all panic and attempt to flee the room, but it's too late.|/A plastic straw lodges in your throat as you gasp for air above the rising waters.|/You die like so many sea turtles.")
		self.caller.msg("|/|rYOU ARE DEAD|n")
		results = search_object("#292")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class FireAlarmCmdSet(CmdSet):
	key = "FireAlarmCmdSet"
	def at_cmdset_creation(self):
		self.add(pull())

class firealarm(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A pull style fire alarm."
		self.cmdset.add_default(FireAlarmCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You can't take a fire alarm you knob head."