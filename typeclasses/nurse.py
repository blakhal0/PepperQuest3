from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "Talk Nurse"
	aliases = ["Talk nurse", "talk nurse", "talk Nurse"]
	auto_help = True
	def func(self):
		if self.caller.db.faction == "fed":
			self.caller.msg("|/|mNurse|n whispers: We have some mutual friends in DC. If you've got something to report, you need to |cDebrief|n.")
			self.caller.msg("|mNurse|n says: Ok inmate, you're all patched up. Get out of here and try to stay out of trouble.")
			return
		else:
			self.caller.msg("|/The nurse looks you over, getting you all fixed up.|/|mNurse|n says: Ok inmate, you're all patched up. Get out of here and try to stay out of trouble.")
			return

class debrief(default_cmds.MuxCommand):
	key = "debrief"
	auto_help = False
	def func(self):
		if not self.caller.db.faction == "fed":
			self.caller.msg("|/|mNurse|n says: I'm not sure I know what you're talking about? Perhaps you hit your head on your way here?")
			return
		if self.caller.db.faction == "fed":
			self.caller.msg("|/The Nurse pulls the curtain divider closed.")
			if self.caller.tags.get("gracedone"):
				self.caller.msg("|mNurse|n says: Greetings agent, I'm here on behalf of the National Spice Agency.")
				self.caller.msg("|mNurse|n says: I'll be your direct contact to debrief and request help.")
				self.caller.msg("|mNurse|n says: Now, obviously there's only so much I can do, but I'll help out if I can.")
				self.caller.msg("|mNurse|n says: Rumor is that fight in the cafeteria caught the eye of several of the Naga Vipers members, keep an eye out, they'll probably be reaching out to recruit you.")
				self.caller.msg("|mNurse|n says: Don't forget your mission, infiltrate the Naga Vipers, gather info on the Ghost Reapers if you can, but most importantly is to identify and communicate with our asset within the Naga Vipers organization.")
				self.caller.msg("|mNurse|n says: Report back here to debrief once you've been recruited.")
				self.caller.msg("|mNurse|n says: Now, you can't just walk in here, so when you need to debrief tell the guard outside that 'I need to have bloodwork done', or just 'bloodwork' if you're not the talkative type, and you'll be allowed in.")
				self.caller.msg("|mNurse|n says: Keep your eyes and ears peeled, completing your mission is the only way you'll ever get out of this prison alive.")
				return
			if self.caller.db.cartel == "vipers":
				if self.caller.tags.get("assetfound"):
					if self.caller.search("Poison Pills", location=self.caller, quiet=True):
						self.caller.msg("|mNurse|n says: You've already got the poison pills, trust me, one for each of you is enough.")
						self.caller.msg("|mNurse|n says: Take the pills back to the asset and |cSwallow Pills|n. It's not going to feel good, but it's the only way out of here.")
						self.caller.msg("|mNurse|n says: Now pay attention, you're going to want to have someone make a ruckus up on the second floor before you take the pills, if the guards don't find you fast enough, you'll die for real.")
						return
					self.caller.msg("|mNurse|n says: Greetings agent, excellent work on making contact with the asset.")
					self.caller.msg("|mNurse|n says: I've received orders that the info the asset has is too important to just relay, the higher ups want it straight from the horses mouth.")
					self.caller.msg("|mNurse|n says: So, we've got to get you two out of here and to headquarters.")
					self.caller.msg("|mNurse|n says: The good news is it's time to get you out of here.")
					self.caller.msg("|mNurse|n says: The bad news is no one gets out of here alive.")
					self.caller.msg("|mNurse|n says: So we're going to need you to fake your death.")
					self.caller.msg("|mNurse|n says: Here, take these.")
					poison_proto = {
					"key": "Poison Pills",
					"typeclass": "typeclasses.objects.DefaultObject",
					"desc": "Two poison pills.",
					"location": self.caller
					}
					spawn(poison_proto)
					self.caller.msg("|mNurse|n says: The poison pills will slow your vitals to an undetectable level, you'll be taken down to the morgue while they're waiting to cremate your bodies.")
					self.caller.msg("|mNurse|n says: I'll inject you with the antidote once you've been declared deceased, you should wake up after a few minutes in the morgue.")
					self.caller.msg("|mNurse|n says: In the morgue is a drain pipe opening that leads into an old sewer system, we haven't been able to locate accurate blue prints, but we know it leads out to a storm drain entrance outside the prison walls, we'll be waiting there to evac the both of you.")
					self.caller.msg("|mNurse|n says: Take the pills back to the asset and |cSwallow Pills|n. It's not going to feel good, but it's the only way out of here.")
					self.caller.msg("|mNurse|n says: Now pay attention, you're going to want to have someone make a ruckus up on the second floor before you take the pills, if the guards don't find you fast enough, you'll die for real.")
					self.caller.msg("|mNurse|n says: I'll see you on the outside agent, excellent work, everyone at headquarters is very impressed with your work so far.")
					return
				else:
					self.caller.msg("|mNurse|n says: Greetings agent, excellent work on getting inducted to the Naga Vipers cartel.")
					self.caller.msg("You tell the nurse all the info you've gathered so far.")
					self.caller.msg("|mNurse|n says: Very good, that aligns with the other intel we've gathered. We had a small breakthrough with the encrypted files, we managed to recover the codephrase used between the asset and his handler.")
					self.caller.msg("|mNurse|n says: Once you've identified the asset talk to them and say the following: 'I have been sent by the penguin'.")
					self.caller.msg("|mNurse|n says: The asset will respond with 'Well, let's take a waddle then'.")
					self.caller.msg("|mNurse|n says: You're getting close to being able to get out of this hell hole, keep your eyes peeled and your ears open.")
					self.caller.msg("|mNurse|n says: Go find that asset and report back to debrief.")
					return
			else:
				self.caller.msg("|/|mNurse|n says: You don't appear to have anything new to report, get out there and complete your mission agent!")
				return
		else:
			self.caller.msg("|/The nurse looks you over, getting you all fixed up.|/|mNurse|n says: Ok inmate, you're all patched up. Get out of here and try to stay out of trouble.")
			return


class NurseCmdSet(CmdSet):
	key = "NurseCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(debrief())

class nurse(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A nurse with a kind face and a cleanly pressed uniform is busy filling out paperwork, checking on each patient. She walks over to you.|/|mNurse|n says: Well, I'm no mind reader, talk to me and tell me what's wrong?"
		self.cmdset.add_default(NurseCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "You try that again and there will be an involuntary surgery in your immediate future."