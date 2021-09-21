from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint

class workout(default_cmds.MuxCommand):
	key = "Workout"
	auto_help = True
	def func(self):
		luck = randint(1, 4)
		if luck in [2, 4]:
			self.caller.msg("|/You're feeling strong, you load up the bar and start doing some presses.")
			yield 3
			self.caller.msg("|/Oh, yeah, 4, 5, 6, woooo!! FEELING THE BURN!!!")
			yield 3
			self.caller.msg("|/7, 8, 9, 10. YEAH! You jump up and howl and flex!! 10 reps of 35 lbs, BEEFCAKE!!!")
			self.caller.msg("You strut around being swoll and showing off 'the guns'.")
			return
		else:
			self.caller.msg("|/You're feeling strong, you load up the bar and start doing some presses.")
			yield 3
			self.caller.msg("|/Oh, yeah, 4, 5, 6, woooo!! FEELING THE BURN!!!")
			yield 3
			self.caller.msg("|/OH GOD!! ARM CRAMP!!!")
			self.caller.msg("You drop the weights which come crashing down onto your throat, the other inmates stand around and laugh as you gasp for breath and flail helplessly.")
			self.caller.msg("Everything fades to grey.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class WeightCmdSet(CmdSet):
	key = "WeightCmdSet"
	def at_cmdset_creation(self):
		self.add(workout())

class weightbench(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A weight bench is open, you could use some muscles if you're going to stay alive in here. Maybe |cWorkout|n a little?"
		self.cmdset.add_default(WeightCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialobj")
		self.db.get_err_msg = "|/Taking the weights is just a different form of lifting them..."