import syllables
import sys
from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class therapy(default_cmds.MuxCommand):
	key = "talk therapist"
	aliases = ["Talk Therapist", "Talk therapist", "talk Therapist"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("dayroom"):
			self.caller.msg("|/Group therapy is over. Thank you for participating!")
			return
		self.caller.tags.add("therapy")
		self.caller.msg("|/|mTherapist|n says: Hello, and welcome, I'm glad you decided to join us for group therapy today.")
		self.caller.msg("|mTherapist|n says: Today we're going to explore the soothing magic of the haiku form of poetry.")
		self.caller.msg("|mTherapist|n says: %s, why don't you go ahead and start us off. Use |cHaiku|n to start expressing your emotions. Remember the format is 5 syllables, 7 syllables, 5 syllables, we are sticklers for the rules here." % (self.caller.key)) 
		self.caller.msg("|mTherapist|n says: When you're done, we'll share it with the room.")
		return

class haiku(default_cmds.MuxCommand):
	key = "Haiku"
	aliases = ["haiku"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("dayroom"):
			self.caller.msg("|/Group therapy is over. Thank you for participating!")
			return
		line1 = yield("|/What's the first line of your Haiku?")
		line1 = ''.join(line1)
		if not syllables.estimate(line1) == 5:
			count = syllables.estimate(line1)
			self.caller.msg("|mTherapist|n says: Oh, sorry %s not the right number of syllables." % (count))
			return
		else:
			self.caller.msg("That's really great work!")
			line2 = yield("|/What's the second line of your Haiku?")
			line2 = ''.join(line2)
			if not syllables.estimate(line2) == 7:
				count = syllables.estimate(line2)
				self.caller.msg("|mTherapist|n says: Oh, sorry %s not the right number of syllables." % (count))
				return
			else:
				self.caller.msg("Very Imperssive!")
				line3 = yield("|/What's the third line of your Haiku?")
				line3 = ''.join(line3)
				if not syllables.estimate(line3) == 5:
					count = syllables.estimate(line3)
					self.caller.msg("|mTherapist|n says: Oh, sorry %s not the right number of syllables." % (count))
					return
				else:
					self.caller.msg("BRAVO, A MASTERPIECE!")
					finhaiku = "|/" + line1 + "|/" + line2 + "|/" + line3
					self.caller.msg("|/|mTherapist|n says: Your mastery of the 5-7-5 format is inspirational!!")
					self.caller.location.msg_contents("|mTherapist|n says: Attention everyone, %s has prepared a haiku to share with the group." % (self.caller.key))
					self.caller.location.msg_contents("%s" % (finhaiku))
					self.caller.tags.remove("therapy")
					self.caller.tags.add("dayroom")
					self.caller.msg("|/Therapist|n says: That is all for group therapy, I feel like we made some great progress today!!")
					self.caller.msg("Therapist|n says: You may continue to use the day room as you wish now.")
					return

class TherapistCmdSet(CmdSet):
	key = "TherapistCmdSet"
	def at_cmdset_creation(self):
		self.add(therapy())
		self.add(haiku())
	
class therapist(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The therapist sits at the head of a circle of chairs leading a group therapy session."
		self.cmdset.add_default(TherapistCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(dayroom)")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mTherapist|n says: We use our words in here."

