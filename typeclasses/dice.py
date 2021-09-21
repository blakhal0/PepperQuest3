from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint

class gamble(default_cmds.MuxCommand):
	key = "Play Dice"
	aliases = ["play dice", "Play dice", "play Dice"]
	auto_help = True
	def func(self):
		if self.caller.db.stamps == 0:
			self.caller.msg("|/|mInmate|n says: Here, since you're new here I'll spot you a book of stamps, free of charge.")
			self.caller.db.stamps += 1
		if self.caller.search("Loaded Dice", location=self.caller, quiet=True):
			self.caller.msg("|/You take a couple 'practice' rolls and swap out for the loaded dice.")
			self.caller.msg("You grab the dice and roll...")
			yield 3
			self.caller.msg("|/Oh, yeah, that's a winner!! PAY ME!!")
			self.caller.db.stamps += 1
			self.caller.msg("You've got %s books of stamps." % (self.caller.db.stamps))
			return
		luck = randint(1, 4)
		if luck in [2, 3, 4]:
			self.caller.msg("|/Best to play it safe and only wager 1 book of stamps.")
			self.caller.msg("You grab the dice and roll...")
			yield 3
			self.caller.msg("|/Oh, yeah, that's a winner!! PAY ME!!")
			self.caller.db.stamps += 1
			self.caller.msg("You win a book of stamps.")
			self.caller.msg("You've got %s books of stamps." % (self.caller.db.stamps))
			self.caller.msg("The other players look a bit upset.")
			return
		else:
			self.caller.msg("|/You're feeling lucky and go all in.")
			yield 3
			self.caller.msg("|/Oh, yeah, that's a winner!! PAY ME!!")
			yield 3
			self.caller.msg("|/|mInmate|n says: Forget you chump, that's all my stamps!!")
			self.caller.msg("The inmate pulls out a knife and stabs you repeatedly.")
			self.caller.msg("While you're on the ground bleeding they steal all your stamps.")
			self.caller.db.stamps = 0
			self.caller.msg("Everything fades to grey.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class DiceCmdSet(CmdSet):
	key = "DiceCmdSet"
	def at_cmdset_creation(self):
		self.add(gamble())

class dice(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A few inmates are gathered around throwing dice for stamps. Wanna try your luck? |cPlay dice|n."
		self.cmdset.add_default(DiceCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialobj")
		self.db.get_err_msg = "|/One of the inmates slaps you in the head, 'Don't take our dice, we had to kill someone to make them!!'"