from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class interrogate(default_cmds.MuxCommand):
	key = "interrogate"
	auto_help = True
	def func(self):
		stress = 0
		rounds = 0
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/The subject has been 'disposed of'.")
			return
		while rounds < 5:
			if stress > 100:
				self.caller.msg("|/The subject has passed out due to stress.")
				self.caller.msg("You'll need to start over.")
				break
			if stress < 0:
				self.caller.msg("|/The subject has passed out, you've administered too much sedative.")
				self.caller.msg("You'll need to start over.")
				break
			if stress <= 25:
				self.caller.msg("|/The subjects stress level is low, they seem uncooperative.")
			if 25 < stress <= 65:
				self.caller.msg("|/The subject is mildly stressed, they seem like they're about to give up some info.")
			if 65 < stress <= 90:
				self.caller.msg("|/The subject is properly motivated and talking.")
				self.caller.msg("|m%s|n says: Who's the leader of the Ghost Reapers? Where can we find them? Who are they working with in the NSA?" % (self.caller.key))
				if rounds == 0:
					self.caller.msg("|mSubject|n says: OWWW! Shit. You people are sick freaks. Yeah, yeah I know the guy you're looking for...")
					yield 2
					self.caller.msg("|mSubject|n says: His name is Vincent....")
					yield 2
					self.caller.msg("|mSubject|n says: VAN GOGH FUCK YOURSELF!")
					yield 3
				elif rounds == 1:
					self.caller.msg("|/|mSubject|n says: Alright, alright, just stop, please stop.")
					yield 2
					self.caller.msg("|mSubject|n says: Her name is Jenny, don't be fooled, she might have some rocks, but she's still Jenny, Jenny from the block.")
					yield 3
				elif rounds == 2:
					self.caller.msg("|/|mSubject|n says: FUCKING STOP I'LL TELL YOU WHAT YOU WANT TO KNOW!")
					yield 2
					self.caller.msg("|mSubject|n says: Yo, I'll tell you what I want, what I really, really want.|/So tell me what you want, what you really, really want.|/I'll tell you what I want, what I really, really want.")
					yield 3
				elif rounds == 3:
					self.caller.msg("|/|mSubject|n says: Enough, enough, I'll spill. You gotta understand, these people are gonna kill me. I promised that I'd never.")
					self.caller.msg("|m%s|n says: You'd never what?" % (self.caller.key))
					yield 2
					self.caller.msg("|mSubject|n says: Never gonna give you up|/Never gonna let you down|/Never gonna run around and desert you|/Never gonna make you cry|/Never gonna say goodbye|/Never gonna tell a lie and hurt you.")
					yield 3
					self.caller.msg("The subject is close to breaking, one more round should do it.")
				elif rounds == 4:
					self.caller.msg("|/|mSubject|n says: Alright, alright, I can't take anymore. You're looking for Leia, she's supposed to meet her connect at |cThe 9th Circle|n SpiceEasy, the entrance is on the corner of 16th and Florida, the phone booth.")
					self.caller.msg("|mSubject|n says: It's a hidden entrance, you can't see it. Just go to where the phone booth is and go in |cThe 9th Circle|n.")
					self.caller.tags.remove("interrogate")
					self.caller.tags.add("finalend")
					self.caller.msg("|/The subject has given you the info you're looking for. Now it's time to act and find the rat.")
					yield 3
					break
				rounds += 1
			if 90 < stress <= 100:
				self.caller.msg("|/The subject is too stressed to respond and is going to faint soon.")
			answer = yield("|/What method of interrogation do you want to use?|/Punch.|/Pull a tooth.|/Hot Pliers.|/Water Board.|/Tickle their feet.|/Electric Shock.|/Finger clamp.|/Administer sedative.")
			if answer.lower() in ["punch"]:
				stress += 5
				self.caller.msg("|/You slug the subject in the gut.")
				self.caller.msg("|mSubject|n says: Hahaha, you hit like my grandma")
				yield 3
				continue
			if answer.lower() in ["tooth", "pull", "pull a tooth"]:
				stress += 35
				self.caller.msg("|/You grab the pliers and force the subjects mouth open, you can hear them beg through muffled screams.")
				self.caller.msg("The subject starts to cry as blood pours out of their mouth.")
				self.caller.msg("|mSubject|n says: Please stop, I'm a human dammit, this is not right!!")
				yield 3
				continue
			if answer.lower() in ["hot", "pliers", "hot pliers"]:
				stress += 15
				self.caller.msg("|/You run the blowtorch over the pliers and press it to the subjects chest briefly.")
				self.caller.msg("The subject howls in pain briefly.")
				yield 3
				continue
			if answer.lower() in ["water", "board", "water board"]:
				stress += 50
				self.caller.msg("|/You tip the chair all the way back and put a towel over their face.")
				self.caller.msg("Slowly pouring water over the towel the subject starts to cough and choke, struggling for breath and violently trying to escape the restraints.")
				yield 3
				continue
			if answer.lower() in ["tickle", "tickle feet", "tickle their feet"]:
				stress += 10
				self.caller.msg("|/You tickle their feet, they scream laughing, gasping for breath.")
				self.caller.msg("|mSubject|n says: I.... can't... breathe..... STOP!!")
				self.caller.msg("You don't stop until they wet themselves.")
				yield 3
				continue
			if answer.lower() in ["finger", "clamp", "finger clamp"]:
				stress += 13
				self.caller.msg("|/Forcefully straightening one of the subjects finger you place a clamp around their finger nail and the bottom of the chair arm and start increasing pressure.")
				self.caller.msg("|mSubject|n says: NO! NO! STOP NOOOOOOO!!!")
				yield 3
				continue
			if answer.lower() in ["electric", "shock", "electric shock"]:
				stress += 15
				self.caller.msg("|/Touching the battery cables together, you give the subject a show with the sparks.")
				self.caller.msg("Their entire body stiffens and convulses as you press the cables to their nipples.")
				yield 3
				continue
			if answer.lower() in ["administer", "sedative", "administer sedative"]:
				stress -= 30
				self.caller.msg("|/You inject the subject with a mild sedative. Their muscles appear to release tension slightly.")
				yield 3
				continue
		else:
			self.caller.msg("|/SUCCESS!! The subject gives up all the information needed.")
			return
		return

class InterrogateCmdSet(CmdSet):
	key = "InterrogateCmdSet"
	def at_cmdset_creation(self):
		self.add(interrogate())
	
class torture(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The subject is strapped tightly into a reclining chair. A variety of torture devices are at your disposal."
		self.cmdset.add_default(InterrogateCmdSet, permanent=True)
		self.locks.add("get:false()")