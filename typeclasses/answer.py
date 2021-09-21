from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class answercmd(default_cmds.MuxCommand):
	"""
	Answer.

	Usage:
	Answer

	Gives you a way to attempt to answer the puzzle for this room.
	"""
	key = "answer"
	auto_help = True
	def func(self):
		answer = yield("Your Answer: ")
		target = self.caller.search("answer")
		if answer.lower() in target.db.answer:
			self.caller.msg(target.db.congrats)
			place = target.db.next
			self.caller.db.mazelocation = target.db.next
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		else:
			self.caller.msg(target.db.fail)
			return

class AnswerCmdSet(CmdSet):
	key = "AnswerCmdSet"
	def at_cmdset_creation(self):
		self.add(answercmd())

class answer(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Type in |cAnswer|n to input your answer."
		self.db.answer = []
		self.db.next = ""
		self.db.congrats = "|/|rYou answered correctly. You are now being moved to the next step.|n|/"
		self.db.fail = "|/Wah-wah-wahhhhh.|/Oh, sorry that's not the right answer.|/Try again.|/"
		self.cmdset.add_default(AnswerCmdSet, permanent=True)
		self.locks.add("get:false()")