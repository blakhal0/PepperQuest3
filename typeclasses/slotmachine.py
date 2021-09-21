from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint

class slots(default_cmds.MuxCommand):
	key = "Spicy Slots"
	aliases = ["slicy slots", "Spicy slots", "spicy Slots", "slots"]
	def func(self):
		if self.caller.tags.get("slots"):
			self.caller.msg("|/|/Security comes over.|/|mSecurity|n says: Hey! we've been warned by our friends in Colorado about punks like you trying to rip us off. ONE SPIN AT A TIME!!.|/|/")
			return
		multiplier = yield("|/|/Welcome to |rSpicy Slots!!|n|/You currently have $%s in cash.|/Each credit is $10. How many credits would you like to play? 1-10" % (self.caller.db.cash))
		if not multiplier.isdigit():
			self.caller.msg("Sorry, you need to choose a number of credits 1-10.")
			return
		if not 0 < int(multiplier) <= 10:
			self.caller.msg("Sorry, you need to choose a number of credits 1-10.")
			return
		wager = 10 * int(multiplier)
		if self.caller.db.cash < wager:
			self.caller.msg("You don't have enough cash to play $%s, this game costs $10 per credit, you currently only have $%s" % (wager, self.caller.db.cash))
			return
		self.caller.tags.add("slots")
		self.caller.db.cash -= wager
		reel1 = randint(1, 6)
		reel2 = randint(1, 6)
		reel3 = randint(1, 6)
		if reel1 == 1:
			self.reel1pos = "||BAR||"
		if reel1 == 2:
			self.reel1pos = "|rPEPPER|n"
		if reel1 == 3:
			self.reel1pos = "||DOUBLE BAR||"
		if reel1 == 4:
			self.reel1pos = "|gW|yI|cL|mD|n"
		if reel1 == 5:
			self.reel1pos = "|yBELL|n"
		if reel1 == 6:
			self.reel1pos = "|gCOIN|n"
		if reel2 == 1:
			self.reel2pos = "||BAR||"
		if reel2 == 2:
			self.reel2pos = "|rPEPPER|n"
		if reel2 == 3:
			self.reel2pos = "||DOUBLE BAR||"
		if reel2 == 4:
			self.reel2pos = "|gW|yI|cL|mD|n"
		if reel2 == 5:
			self.reel2pos = "|yBELL|n"
		if reel2 == 6:
			self.reel2pos = "|gCOIN|n"
		if reel3 == 1:
			self.reel3pos = "||BAR||"
		if reel3 == 2:
			self.reel3pos = "|rPEPPER|n"
		if reel3 == 3:
			self.reel3pos = "||DOUBLE BAR||"
		if reel3 == 4:
			self.reel3pos = "|gW|yI|cL|mD|n"
		if reel3 == 5:
			self.reel3pos = "|yBELL|n"
		if reel3 == 6:
			self.reel3pos = "|gCOIN|n"
		self.caller.msg("You put $%s in the slot machine and pull the handle..." % (wager))
		yield 2
		self.caller.msg("The reels start to slow down..")
		yield 2
		self.caller.msg("The reels stop on|/%s - %s - %s" % (self.reel1pos, self.reel2pos, self.reel3pos))
		if reel1 == 2 and reel2 == 2 and reel3 == 2:
			self.winnings = wager * 1000
			self.caller.msg("YOU WON THE |yJACKPOT|n!!!")
		elif reel1 in [1,4] and reel2 in [1,4] and reel3 in [1,4]:
			self.winnings = wager * 8
		elif reel1 in [2,4] and reel2 in [2,4] and reel3 in [2,4]:
			self.winnings = wager * 30
		elif reel1 in [3,4] and reel2 in [3,4] and reel3 in [3,4]:
			self.winnings = wager * 8
		elif reel1 == 4 and reel2 == 4 and reel3 == 4:
			self.winnings = wager * 8
		elif reel1 in [5,4] and reel2 in [5,4] and reel3 in [5,4]:
			self.winnings = wager * 8
		elif reel1 in [6,4] and reel2 in [6,4] and reel3 in [6,4]:
			self.winnings = wager * 8
		elif reel1 in [2,4] and reel2 in [2,4] and reel3 in [1,3,5,6]:
			self.winnings = wager * 6
		elif reel1 in [2,4] and reel2 in [1,3,5,6] and reel3 in [1,2,3,4,5,6]:
			self.winnings = wager * 4
		else:
			self.winnings = 0
		self.caller.tags.remove("slots")
		self.caller.db.cash += self.winnings
		if self.winnings > 0:
			self.caller.msg("You won $%s!!" % (self.winnings))
			self.caller.msg("You currently have $%s in cash." % (self.caller.db.cash))
		if self.winnings == 0:
			self.caller.msg("Sorry, you lost. Better luck next time.")
			self.caller.msg("You currently have $%s in cash." % (self.caller.db.cash))
		if self.caller.tags.get("vip"):
			return
		if self.caller.db.cash >= 5000:
			self.caller.tags.add("vip")
			self.caller.msg("|r|/A representative from the 9th Circle approaches.|n")
			self.caller.msg("Hello %s, we've been observing you and have determined we like your style.|/I would like to extend an invitation to our VIP lounge area.|/The bouncer has already been alerted that you're on the approved list.|/We hope to continue to have your patronage, and thank you for choosing the 9th Circle SpiceEasy." % (self.caller.key))

class SlotCmdSet(CmdSet):
	key = "SlotCmdSet"
	def at_cmdset_creation(self):
		self.add(slots())
	
class slotmachine(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A slightly worn, but still nice looking Spicy Slots slot machine.|/A tag on the side of the machine says 'Property of the Torrance Arms, Null Point, Colorado'|/Try your luck and play |cSpicy Slots|n!! Only $10 a credit Bet up to 10 credits!."
		self.cmdset.add_default(SlotCmdSet, permanent=True)
		self.locks.add("get:false()")
