from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk lowe"
	aliases = ["Talk Lowe", "Talk lowe", "talk Lowe" ]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("meetingdone"):
			self.caller.msg("|/|mLowe|n says: Hello Agent %s, we're glad to have you on the team. I'm busy getting ready for the daily meeting, which you should be also, I'll see you in the meeting room." % (self.caller.key))
			return
		if self.caller.tags.get("extract"):
			self.caller.msg("|/|mLowe|n says: Hello Agent %s, Executive Director Locke says you've identified a possible target location that may need an extraction, well you've come to the right place." % (self.caller.key))
			self.caller.msg("|mLowe|n says: My team and I are essentially shadows with nice sunglasses.")
			self.caller.msg("|mLowe|n says: Head down to Mad Scientist laboratory and pick up an ear piece. Watch the park and observe the possible targets, when you've located your target just let us know and we'll handle the extraction.")
			self.caller.tags.remove("extract")
			self.caller.tags.add("earwig")
			return
		if self.caller.tags.get("earwig"):
			self.caller.msg("|/|mLowe|n says: Head down to Mad Scientist laboratory and pick up an ear piece. Watch the park and observe the possible targets, when you've located your target just let us know and we'll handle the extraction.")
			return
		if self.caller.tags.get("subjectextracted"):
			self.caller.msg("|/|mLowe|n says: Excellent work on identifying the target.")
			self.caller.msg("|mLowe|n says: They're cooling their heels in a safe location, being questioned.")
			self.caller.msg("|mLowe|n says: Reports say that the subject is quite uncooperative, we might have to use some 'enhanced' techniques.")
			self.caller.msg("|mLowe|n says: Only the Director can authorize that, go talk to Director Keye and get the go ahead, we'll find out everything they know. And I mean everything.")
			self.caller.tags.remove("subjectextracted")
			self.caller.tags.add("lowedone")
			return
		if self.caller.tags.get("lowedone"):
			self.caller.msg("|/|mLowe|n says: Hello Agent %s, you're work speaks for itself, even when it says nothing. Glad to have you on our side." % (self.caller.key))
			return
		self.caller.msg("|/|mLowe|n says: Hello Agent %s, welcome to the NSA, we're excited to see where your career takes you." % (self.caller.key))
		return

class LoweCmdSet(CmdSet):
	key = "LoweCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class edlowe(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Executive Director Lowe sits behind her desk, watching grainy night vision videos of long distance sniper shots."
		self.cmdset.add_default(LoweCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.nostunmsg = "|/Lowe swiftly pulls a small weapon and fires, you feel a pin prick in your neck right before your entire body goes numb and you hit the ground."
		self.db.get_err_msg = "|/|mLowe|n says: I've disappeared much higher profile targets then you."