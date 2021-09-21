from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import string
from random import randint
import random

class riddle(default_cmds.MuxCommand):
	key = "answer the riddle"
	auto_help = True

	def failed(self):
		if self.caller.db.riddlefail == 2:
			self.caller.tags.remove("youmaynotpass")
			self.caller.db.riddlefail = 0
			self.caller.msg("|/|mRat King|n says: You have failed my tests, your spirit shall wander forever and EVER!!|/The Rat King produces a small curved dagger with a large ruby on the hilt, glinting in the light.|/Before you can move to defend yourself he plants the dagger in your heart.|/|/|rYOU ARE DEAD.|n")
			place = "#1662"
			results = search_object(place)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.db.riddlefail += 1
			self.caller.msg("|/|mRat King|n says: That is not the correct answer, you fool.|/Use care, for I do not suffer great fools... Perhaps you need an easier question for your feeble mind. Try again.")
			return

	def correct(self):
		self.caller.msg("|/|mRat King|n says: You have solved my riddle, you may pass.|/The Rat King steps aside.")
		self.caller.db.riddlefail = 0
		self.caller.tags.remove("youmaynotpass")
		return

	def func(self):
		if not self.caller.tags.get("youmaynotpass"):
			self.caller.msg("You have no need to answer a riddle.")
			return
		openingwords = ["|/|mRat King|n says: Hold it right there, you must answer my question!", "|/|mRat King|n says: HALT!", "|/Thou shall not pass!! Unless you answer my question.", "|/Stop! Who would cross the Bridge of Death must answer me these questions five, (ahem, three sir), right, three, err, well I guess just the one actually, ere the other side ye see.|/You look around, there's no bridge here you old loon...|/JUST ANSWER THE QUESTION!!"]
		riddle = randint(1, 10)
		self.caller.msg(random.choice(openingwords))

		if riddle == 1:
			correctanswers = ["duck", "a duck"]
			self.caller.msg("|mRat King|n says: What animal looks like a duck, quacks like a duck, has feathers like a duck, and swims like a duck?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 2:
			correctanswers = ["baby tigers", "a baby tiger"]
			self.caller.msg("|mRat King|n says: What do tigers have that no other animals have?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 3:
			correctanswers = ["a match", "the match", "match"]
			self.caller.msg("|mRat King|n says: You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 4:
			correctanswers = ["night", "the night", "darkness", "the darkness", "fog", "the fog"]
			self.caller.msg("|mRat King|n says: The more of this there is, the less you see. What is it?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 5:
			correctanswers = ["a book", "book", "books"]
			self.caller.msg("|mRat King|n says: What has words, but never speaks?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 6:
			correctanswers = ["e", "the letter e", "letter e"]
			self.caller.msg("|mRat King|n says: I am the beginning of everything, the end of everywhere. I’m the beginning of eternity, the end of time and space. What am I?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 7:
			correctanswers = ["silence", "the silence"]
			self.caller.msg("|mRat King|n says: What is so fragile that saying its name breaks it?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 8:
			correctanswers = ["fire", "a fire"]
			self.caller.msg("|mRat King|n says: I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 9:
			correctanswers = ["hole", "a hole"]
			self.caller.msg("|mRat King|n says: What gets bigger the more you take away?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()

		if riddle == 10:
			correctanswers = ["secret", "a secret"]
			self.caller.msg("|mRat King|n says: If you have me, you will want to share me. If you share me, you will no longer have me. What am I?")
			answer = yield("Your answer: ")
			if answer.lower() in correctanswers:
				return self.correct()
			else:
				return self.failed()


class RiddleCmdSet(CmdSet):
	key = "RiddleCmdSet"
	def at_cmdset_creation(self):
		self.add(riddle())
	
class mazeriddle(DefaultObject):
	def at_object_creation(self):
		self.db.kickedout = "#1662"
		self.db.desc = ""
		self.cmdset.add_default(RiddleCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")