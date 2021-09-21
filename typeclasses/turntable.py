from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class listen(default_cmds.MuxCommand):
	"""
	Use Turntable

	Usage:
	Use Turntable

	Listen to your favorite track on one of your records.
	"""
	key = "Use Turntable"
	auto_help = True
	def func(self):
		self.caller.msg("|/What record do you want to listen to?|/Tom Jones - Reload|/The Most Wonderful People Ever - A Call to Arms|/The Pimps - The Evening in Question|/Tool - Lateralus|/Rage Against the Machine - Rage Against the Machine")
		answer = yield("Pick an artist or record: ")
		if answer.lower() in ["tom jones", "reload", "tom jones - reload"]:
			self.caller.msg("|/You carefully take the record out, place it on the turntable, and move the needle to your favorite track - Sex Bomb.|/https://www.youtube.com/watch?v=3qC0203lh8c")
			yield 4
			self.caller.msg("|/The song ends as you think to yourself, 'Wow, what a great song!'")
			return
		elif answer.lower() in ["the most wonderful people ever - a call to arms", "the most wonderful people ever", "a call to arms"]:
			self.caller.msg("|/You carefully take the record out, place it on the turntable, and move the needle to your favorite track - A Call to Arms.|/https://soundcloud.com/bst3r/a-call-to-arms?in=bst3r/sets/the-most-wonderful-people-ever")
			yield 4
			self.caller.msg("|/The song ends as you think to yourself, 'Wow, what a great song!'")
			return
		elif answer.lower() in ["the pimps - the evening in question", "the pimps", "pimps", "the evening in question"]:
			self.caller.msg("|/You carefully take the record out, place it on the turntable, and move the needle to your favorite track - Someone's Trying to Kill Me MAN!|/https://www.youtube.com/watch?v=tL4eYEWAAus")
			yield 4
			self.caller.msg("|/The song ends as you think to yourself, 'Wow, what a great song!'")
			return
		elif answer.lower() in ["tool - lateralus", "tool", "lateralus"]:
			self.caller.msg("|/You carefully take the record out, place it on the turntable, and move the needle to your favorite track - Schism|/https://www.youtube.com/watch?v=MM62wjLrgmA")
			yield 4
			self.caller.msg("|/The song ends as you think to yourself, 'Wow, what a great song!'")
			return
		elif answer.lower() in ["rage against the machine - rage against the machine", "rage against the machine"]:
			self.caller.msg("|/You carefully take the record out, place it on the turntable, and move the needle to your favorite track - Killing in the Name|/https://www.youtube.com/watch?v=bWXazVhlyxQ")
			yield 4
			self.caller.msg("|/The song ends as you think to yourself, 'Wow, what a great song!'")
			return
		else:
			self.caller.msg("You don't seem to have that particular record, maybe try something else.")
			return


class TTCmdSet(CmdSet):
	key = "TTCmdSet"
	def at_cmdset_creation(self):
		self.add(listen())
	
class turntable(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A standalone turntable, in the shape of a large red die.|/If you want, you can |cUse Turntable|n to listen to music."
		self.cmdset.add_default(TTCmdSet, permanent=True)
		self.locks.add("get:false()")