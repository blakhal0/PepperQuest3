from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint
import random

class botfight(default_cmds.MuxCommand):
	key = "Bot Wars"
	aliases = ["bot wars", "Bot wars", "bot Wars"]
	def func(self):
		botnames1 = ["Smashenstein", "Hellfire", "Segfault"]
		botnames2 = ["Nastypants", "Pepperbot", "Decapacitator"]
		movement = ["circles, circles, circles", "makes a darting move", "swings wide, sneaks up from behind", "goes straight at it", "makes a daring charge", "feints right, swings left"]
		botonepower = 20
		bottwopower = 20
		bot1 = random.choice(botnames1)
		bot2 = random.choice(botnames2)
		bots = [bot1, bot2]
		powerlevel = "missed"
		if bot2 == "Pepperbot":
			bottwopower = 100
		self.caller.msg("|/HELLO!! And welcome to Bot Wars!! This round we have %s vs %s, who will survive??!!?!|/PLACE YOUR BETS NOW!!" % (bot1, bot2))
		botbet = yield("Which bot would you like?")
		if not botbet.lower() in [bot1.lower(), bot2.lower()]:
			self.caller.msg("Oh, sorry, that bot isn't in this match. Maybe next round!!")
			return
		wager = yield("How much would you like to wager? You currently have $%s in cash." % (self.caller.db.cash))
		if not wager.isdigit():
			self.caller.msg("|/Sorry, I didn't understand what you said. Please try again.")
			return
		if not 0 < int(wager):
			self.caller.msg("|/Sorry, we only take wagers in whole dollar amounts.")
			return
		if int(wager) > self.caller.db.cash:
			self.caller.msg("|/Sorry, it appears you're a bit short on funds for a wager of that size.")
			return
		self.caller.msg("|/All bets are in, aaaaannnnnddd HEEEEERREEE WEEEEEE GOOOOOOO!!!!!!")
		yield 1
		self.caller.msg("In the red corner we have %s, in the blue corner we have %s." % (bot1, bot2))
		yield 2
		self.caller.msg("|/BOTS READY???")
		yield 1
		self.caller.msg("|/FIGHT!!")
		i = 1
		while i <= 10:
			strikebot = random.choice(bots)
			if strikebot == bot1:
				victim = bot2
			if strikebot == bot2:
				victim = bot1
			power = randint(1, 10)
			if power == 1 or power == 2 or power == 3:
				powerlevel = "glancing"
			if power == 4 or power == 5 or power == 6:
				powerlevel = "solid"
			if power == 7 or power == 8:
				powerlevel = "crushing"
			if power == 9 or power == 10:
				powerlevel = "devastating"
			action = random.choice(movement)
			self.caller.msg("|/%s %s!" % (strikebot, action))
			self.caller.msg("A %s blow to %s!" % (powerlevel, victim))
			yield 2
			if strikebot == bot1:
				bottwopower -= power
			if strikebot == bot2:
				botonepower -= power
			if botonepower <= 0:
				self.caller.msg("|/OHHH! And it's all over folks, %s is out of the fight!!" % (bot1))
				winner = bot2
				break
			if bottwopower <= 0:
				self.caller.msg("|/OHHH! And it's all over folks, %s is out of the fight!!" % (bot2))
				winner = bot1
				break
		if winner.lower() == botbet.lower():
			winnings = 10 * int(wager)
			self.caller.msg("You won $%s!!" % (winnings))
			self.caller.db.cash += winnings
			self.caller.msg("You currently have $%s in cash." % (self.caller.db.cash))
		if not winner.lower() == botbet.lower():
			self.caller.db.cash -= int(wager)
			self.caller.msg("Sorry, you lost. Better luck next time.")
		if self.caller.tags.get("vip"):
			return
		if self.caller.db.cash >= 5000:
			self.caller.tags.add("vip")
			self.caller.msg("|r|/A representative from the 9th Circle approaches.|n")
			self.caller.msg("Hello %s, we've been observing you and have determined we like your style.|/I would like to extend an invitation to our VIP lounge area.|/The bouncer has already been alerted that you're on the approved list.|/We hope to continue to have your patronage, and thank you for choosing the 9th Circle SpiceEasy." % (self.caller.key))
			return

class BotCmdSet(CmdSet):
	key = "BotCmdSet"
	def at_cmdset_creation(self):
		self.add(botfight())
	
class botwars(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Welcome to Bot Wars, where two mechanical marvels smash and bash the crap out of each other. |cBot Wars|n to place your bets!! Winners paid 10x!!"
		self.cmdset.add_default(BotCmdSet, permanent=True)
		self.locks.add("get:false()")