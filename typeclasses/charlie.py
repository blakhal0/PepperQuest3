from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk charlie"
	aliases = ["Talk Charlie", "Talk charlie", "talk Charlie" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mCharlie|n says: I'm not so sure, does it capture the eternal struggle right and proper?")
		answer = yield("|mCharlie|n says: Is there something you want to ask me?")
		if answer.lower() in ["start a ruckus", "make a ruckus", "cause a ruckus", "ruckus"]:
			if not self.caller.search("Poison Pills", location=self.caller, quiet=True):
				self.caller.msg("|/|mCharlie|n says: Aye mate, I do that all the time, why would you want ol Charlie Bronson to be giving the guv'ners a crick in the neck for? I'll do what I want, when I want, jog on.")
				return
			self.caller.msg("|/|mCharlie|n says: It has been a time since I've given them chaps a good dose of the violence.")
			self.caller.msg("|mCharlie|n says: Alright, consider ol Charlie Bronson on the ticket.")
			self.caller.msg("Charlie begins to strip down naked.")
			self.caller.msg("|mCharlie|n says: Oy, grab that bit of butter there and give me a good greasing up yeah? These pricks won't know what hit them.")
			self.caller.msg("Reluctantly you do as Charlie requests and grease him up, top to tail.")
			self.caller.msg("|mCharlie|n says: Owlright, now these bastards are hard, but ol Charlie Bronson is a fookin diamond.")
			self.caller.msg("|mCharlie|n says: I'll givem the business for as long as I can, but whatever you're up to, get after it yeah?")
			self.caller.msg("|mCharlie|n screams: OY! YOU FOOKIN BILLIE BOYS BEST GET READY, OL CHARLIE BRONSON IS SETTING OFF!!")
			self.caller.msg("Charlie takes off out of the cell screaming, grabbing the nearest guard, and slamming a fist into their face, showering the area with teeth.")
			self.caller.tags.add("ruckus")
			yield 80
			if not self.caller.tags.get("ruckus"):
				return
			self.caller.msg("Charlie is giving the guards a hell of a time, but he's starting to look tired.")
			yield 10
			if not self.caller.tags.get("ruckus"):
				return
			self.caller.msg("The guards are getting the upper hand on Charlie, things are quieting down.")
			yield 10
			if not self.caller.tags.get("ruckus"):
				return
			self.caller.tags.remove("ruckus")
			self.caller.msg("The guards have Charlie restrained and back in his cell, the ruckus is over.")
			return
		else:
			self.caller.msg("|/|mCharlie|n says: You daft in the head? Go on, beat it.")
			return

class grab(default_cmds.MuxCommand):
	key = "get charlie"
	aliases = ["Get Charlie", "Get charlie", "get Charlie" ]
	auto_help = False
	def func(self):
		self.caller.msg("|/|mCharlie|n says: Oi! YOU FOOKIN WAT MATE??!??!")
		self.caller.msg("In a display of truly awesome violence Charlie punches you in the throat and then proceeds to bash your skull against the wall.")
		self.caller.msg("|/|mCharlie|n says: DON'T EVER TOUCH ME YOU MANKY GIT! Oooh, that's just the color of red I need for this project.|/Charlie scoops up a handful of your blood and begins to paint his sculpture.")
		results = search_object("#436")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return


class CharlieCmdSet(CmdSet):
	key = "CharlieCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(grab())

class charlie(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Charlie busies himself tearing up paper making a papier mache sculpture of one person strangling another."
		self.cmdset.add_default(CharlieCmdSet, permanent=True)
#		self.locks.add("get:false()")
		self.tags.add("specialnpc")