from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk locke"
	aliases = ["Talk Locke", "Talk locke", "talk Locke" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("extract"):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s, great work on that scanning mission. You seem to be fitting in here nicely. Good talking to you." % (self.caller.key))
			return
		if not self.caller.tags.get("meetingdone"):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s, we're glad to have you on the team. I'm busy getting ready for the daily meeting, which you should be also, I'll see you in the meeting room." % (self.caller.key))
			return
		if self.caller.tags.get("scanned"):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s, how was your first foray into the field? Good? Excellent." % (self.caller.key))
			self.caller.msg("|mLocke|n says: So, there's a cartel member that's been hanging around Foxstone Park, interesting.")
			self.caller.msg("|mLocke|n says: Ok, well, let's roll on seeing if we can identify and possibly extract the target.")
			self.caller.msg("|mLocke|n says: I'll fill in Executive Director Lowe, he handles the 'personal touch' aspects of operations.")
			self.caller.msg("|mLocke|n says: Head down to her office and get a plan put together.")
			self.caller.msg("|mLocke|n says: Excellent work Agent %s, you're proving your worth quickly, the Director is taking notice." % (self.caller.key))
			self.caller.tags.add("extract")
			self.caller.tags.add("lockedone")
			return
		if self.caller.tags.get("qscan"):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s." % (self.caller.key))
			self.caller.msg("|mLocke|n says: Head on down to Q Branch and get the scanner, then put your walking shoes on and hit the streets.")
			self.caller.msg("|mLocke|n says: Q Branch will give you the details.")
			self.caller.msg("|mLocke|n says: Good luck, we're all pulling for you.")
			return
		if self.caller.search("Sweeper 9000", location=self.caller, quiet=True):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s." % (self.caller.key))
			self.caller.msg("|mLocke|n says: Head on down to Q Branch and get the scanner, then put your walking shoes on and hit the streets.")
			self.caller.msg("|mLocke|n says: Q Branch will give you the details.")
			self.caller.msg("|mLocke|n says: Good luck, we're all pulling for you.")
			return
		if self.caller.tags.get("lockedone"):
			self.caller.msg("|/|mLocke|n says: Hello Agent %s, you're doing great work, I'm hearing nothing but good things about you." % (self.caller.key))
			return
		self.caller.msg("|/|mLocke|n says: Hello Agent %s, are you ready to put in some field time? Great, I've got the perfect first time mission." % (self.caller.key))
		self.caller.msg("|mLocke|n says: As I covered in the meeting, we've gathered some good intel from the surveillance network around the city.")
		self.caller.msg("|mLocke|n says: But due to the spottiness of the uptime on their devices, we're going to need someone on foot in the city scanning.")
		self.caller.msg("|mLocke|n says: The big brains down in Q Branch have whipped up a hand held scanner, they've loaded all the relevant data into it.")
		self.caller.msg("|mLocke|n says: They tell me it's 'Agent Proof', don't prove them wrong please.")
		self.caller.msg("|mLocke|n says: Head on down to Q Branch and get the scanner, then put your walking shoes on and hit the streets.")
		self.caller.msg("|mLocke|n says: Q Branch will give you the details.")
		self.caller.tags.add("qscan")
		self.caller.msg("|mLocke|n says: Good luck, we're all pulling for you.")
		return

class LockeCmdSet(CmdSet):
	key = "LockeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class edlocke(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The glare from E.D. Locke's bald head is impressive, as is his mustache. He looks up from the data files on his desk and smiles, welcoming you to sit down."
		self.cmdset.add_default(LockeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.nostunmsg = "|/|mLocke|n says: I like your moxie kid, but if you don't put that weapon away, and I mean NOW, you'll be right back in that hellhole we dug you out of."
		self.db.get_err_msg = "|/|mLocke|n says: They will literally never find enough of you to identify."