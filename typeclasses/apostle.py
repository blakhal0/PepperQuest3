from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk apostle"
	aliases = ["Talk Apostle"]
	auto_help = False
	def func(self):
		if self.caller.tags.get("apostle"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
		self.caller.msg("|/|mFellow Zest|n says: Hello there. What's that? Your name is %s?" % (self.caller.key))
		yield 4
		self.caller.msg("|/Well hello %s, my name is Fellow Zest. Do you have a moment to talk about our lord and savior...." % (self.caller.key))
		self.caller.msg("Suddenly, a woman in a dress and white arm band rounds the corner followed by two federal agents.")
		self.caller.msg("THERE HE IS, GET HIM!!!!|/The agents burst into a sprint barking orders into the cuffs of their jackets.")
		self.caller.msg("Fellow Zest lets out a high pitched screech, reaches under his robes, and begins to douse himself with pepper spray.")
		yield 10
		self.caller.msg("|/|mFellow Zest|n says: HE WHO HAS BEEN NAMED OF THE COLOR OF SPICE HOLDS THE BOOK OF ULTIMATE KNOWLEDGE, THE RETURN OF THE GREAT HOT ONES IS UPON US!!")
		self.caller.msg("|mFellow Zest|n says: YOU'LL NEVER TAKE ME ALIVE!!!! I'LL NEVER STOP BELIEVING IN THE GREAT...ahHAHAHAHAhahahaahguaugaugaugh.|/Fellow Zest drops to the ground twitching as the agents mercilessly taser him.")
		yield 10
		self.caller.msg("|/The agents begin raining down blows between cuffing Fellow Zest and slipping a black bag over his head.")
		self.caller.msg("|mAgent 1|n says: It's the reeducation camps for you! *cough cough* goodnight irene, my EYES!!! He doused himself in illegal chemicals!!!! I think I've been contaminated!!!!")
		self.caller.msg("Agent 2 quickly pulls out a gas mask, looks over to his companion, draws their sidearm and fires.")
		yield 10
		self.caller.msg("Jaw wide in horror, you watch as the splatter rebounds off the pavement and lands on your shoes as Agent 1 collapses, covered in milk.|/|mAgent 2|n says: That should handle it until the decontamination squad arrives, do try and act like a professional.|/Agent 2 lifts his cuff to his mouth, 'We have an agent down, the perpetrator deployed an advanced biological weapon. Perp is tagged and bagged, ready for relocation.'")
		yield 10
		self.caller.msg("|/After carefully wiping the milk off your shoes, you look back up, directly into the gas mask of Agent 2.")
		self.caller.msg("|mAgent 2|n says: You got lucky kid, that guy's a known terrorist, we've been tracking his movements for hours now.|/Best get going before you get any of this chemical on you, it can be pretty addictive, it'd be too bad if we had to make room for two to the reeducation center...")
		self.caller.tags.add("apostle")
		self.caller.msg("A nondescript panel van screams to a halt, the door swings open and Fellow Zest is quickly thrown in before it speeds away.")
		self.caller.msg("|m%s|n says: Yeah, I hear that's real nasty stuff, I'm just going to be on my way, glad to see you all protecting us!" % (self.caller.key))
		return

class ApostleCmdSet(CmdSet):
	key = "ApostleCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class apostle(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A bearded man with died red hair wearing robes is standing against one of the apartments holding a stack of pamphlets. There are pentagrams made of peppers tattooed on his hands."
		self.cmdset.add_default(ApostleCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:not tag(apostle)")