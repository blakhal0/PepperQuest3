from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "attend meeting"
	aliases = ["Attend Meeting", "Attend meeting", "attend Meeting" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("meetingdone"):
			self.caller.msg("|/The meeting is over, if you haven't already, make sure to report to Executive Director Lock.")
			return
		self.caller.msg("|/The Agents all file into the room and take their seats.|/Executive Directors Locke and Lowe take seats at the head of the table, followed by Director Keye.")
		self.caller.msg("|mDirector Keye|n says: Welcome everyone, and especially to our newest recruit, Agent %s." % (self.caller.key))
		self.caller.msg("|mDirector Keye|n says: I'll keep this as brief as possible.")
		self.caller.msg("|mDirector Keye|n says: With our outstanding raid on the Naga Vipers, they have effectively been eliminated from the spice smuggling game.")
		self.caller.msg("|mDirector Keye|n says: This leaves us with only one player left on the field, the Faucheurs Fantomes or Ghost Reapers.")
		self.caller.msg("|mDirector Keye|n says: E.D. Locke will fill us in on the details.")
		self.caller.msg("|mE.D. Locke|n says: Thanks Director. This is going to be dubbed Operation Ghostbusters. We have credible intel that the main American operations of the Cartel has moved their HQ right here into DC.")
		self.caller.msg("|mE.D. Locke|n says: It looks like they're expanding operations into the territory formerly controlled by the Vipers. We've seen increased chatter as well as new graffiti marking territory.")
		self.caller.msg("|mE.D. Locke|n says: Our surveillance system has managed to gather several of their cell phone IMSI and MAC address numbers and we've been tracking them, but it appears they're shutting their phones off regularly, disrupting attempts to install monitoring software on the devices.")
		self.caller.msg("|mE.D. Locke|n says: We're going to need boots on the ground for this one, and I can't think of a better agent to assign this to than Agent %s, please come to my office after the meeting." % (self.caller.key))
		self.caller.msg("|mE.D. Locke|n says: As for the rest of you lot, keep up the pressure, we've got the technology and the wildly loose restraint to use it as we see fit.")
		self.caller.msg("|mDirector Keye|n says: Thank you E.D. Locke. Alright everyone, let's get out there and keep our country safe. Meeting adjourned.")
		self.caller.tags.add("meetingdone")
		return

class MeetingCmdSet(CmdSet):
	key = "MeetingCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class meeting(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(MeetingCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")