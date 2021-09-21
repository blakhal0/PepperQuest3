from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk keye"
	aliases = ["Talk Keye", "Talk keye", "talk Keye" ]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("lowedone") or not self.caller.tags.get("lockedone"):
			self.caller.msg("|/|mKeye|n says: Hello Agent %s, welcome to the NSA. I'm very proud of what we've established here, and we're glad you're here for the next stages." % (self.caller.key))
			return
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/|mKeye|n says: Hello Agent %s, I hear you have a talent for interrogation.")
			self.caller.msg("|mKeye|n says: You're free to act on whatever information you gained, with the full backing of the National Spice Agency.")
			return
		if self.caller.tags.get("interrogate"):
			self.caller.msg("|/|mKeye|n says: Hello Agent %s, I've approved the request for enhanced interrogation techniques." % (self.caller.key))
			self.caller.msg("|mKeye|n says: Our interrogation room is in the basement, go out of the building, into the alley, and behind the building.")
			self.caller.msg("|mKeye|n says: You've been added to the authorized list to access the basement.")
			self.caller.msg("|mKeye|n says: Go get that info, do whatever you need to and follow up on any info you get.")
			return
		if self.caller.tags.get("lowedone") and self.caller.tags.get("lockedone"):
			self.caller.msg("|/|mKeye|n says: I have to say, we're all really impressed with the progress you're making on Operation Ghost Busters.")
			self.caller.msg("Keye takes out a handkerchief and dabs his sweating forehead.")
			self.caller.msg("|mKeye|n says: I understand we have a subject in custody but they're resisting interrogation.")
			self.caller.msg("|mKeye|n says: I'm going to go ahead and authorize the enhanced techniques, there's a stack of pre-signed papers over there, in the future if you need one, just grab it.")
			self.caller.msg("|mKeye|n says: Our interrogation room is in the basement, go out of the building, into the alley, and behind the building.")
			self.caller.msg("|mKeye|n says: You've been added to the authorized list to access the basement.")
			self.caller.msg("|mKeye|n says: Go get that info, do whatever you need to and follow up on any info you get.")
			self.caller.tags.add("interrogate")
			return
		self.caller.msg("|/|mKeye|n says: AMAZING work, agent, I sense a promotion in your future!")
		return

class KeyeCmdSet(CmdSet):
	key = "KeyeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class dkeye(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Director Keye sits behind a massive desk.|/You can see sweat beading up on his forehead and his face is flushed."
		self.cmdset.add_default(KeyeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.nostunmsg = "|/Keye just stares you down and grins."
		self.db.get_err_msg = "|/|mKeye|n says: I can make it so that you literally never existed."