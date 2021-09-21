from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint
import random

class manfight(default_cmds.MuxCommand):
	key = "Wrestle"
	def func(self):
		fighters = ["The Rock", "Brutus THE BARBER Beefcake", "The Million Dollar Man Ted Dibiase"]
		fighter = random.choice(fighters)
		weapons = ["rock", "paper", "scissors"]
		fighterwin = 0
		playerwin = 0
		round = 1
		i = 1
		self.caller.msg("|/|mAnnouncer|n says: LLLLLadies and Gentlemen, we have a NEW fighter in the arena today.")
		self.caller.msg("|mAnnouncer|n says: Let's hear it for %s!!!" % (self.caller.key))
		self.caller.msg("The crowd goes wild.")
		yield 3
		self.caller.msg("|/|mAnnouncer|n says: In the other corner we have the man, the myth, the legend %s!" % (fighter))
		self.caller.msg("The crowd goes wild.")
		yield 3
		self.caller.msg("|/|mAnnouncer|n says: This match is scheduled for 2 falls.")
		self.caller.msg("|mAnnouncer|n says: Fighters, to the center of the ring.")
		self.caller.msg("|mRef|n says: Now I want a clean fight, no spitting, eye gouging, hitting below the belt, tagging in support, foreign objects, none of it.")
		self.caller.msg("|mRef|n says: %s are you ready...." % (fighter))
		self.caller.msg("|m%s|n says: I was born ready." % (fighter))
		self.caller.msg("|mRef|n says: %s are you ready...." % (self.caller.key))
		self.caller.msg("|m%s|n says: OOOOHHHHH YEEEAAHHH BROTHER, %s, you're going down!!" % (self.caller.key, fighter))
		self.caller.msg("The fighters approach the center of the frozen ring...")
		while i < 10:
			if playerwin == 2 or fighterwin == 2:
				break
			self.caller.msg("|/|mAnnouncer|n says: Round %s" % (round))
			self.caller.msg("|mAnnouncer|n says: %s, %s wins." % (self.caller.key, playerwin))
			self.caller.msg("|mAnnouncer|n says: %s, %s wins." % (fighter, fighterwin))
			answer = yield("Choose your option: Rock, Paper, Scissors.")
			if not answer.lower() in ["rock", "paper", "scissors"]:
				self.caller.msg("|/|mAnnouncer|n says: Ohhh, that's too bad to see, %s attempted to cheat." % (self.caller.key))
				self.caller.msg("|mRef|n says: Winner due to disqualification, %s!!" % (fighter))
				break
			if round == 1:
				if fighter == "The Rock":
					fighterweapon = "rock"
				if fighter == "Brutus THE BARBER Beefcake":
					fighterweapon = "scissors"
				if fighter == "The Million Dollar Man Ted Dibiase":
					fighterweapon = "paper"
			if round == 2:
				fighterweapon = random.choice(weapons)
			if round == 3:
				fighterweapon = random.choice(weapons)
			if answer.lower() == "rock" and fighterweapon == "paper":
				self.caller.msg("|/%s picks up a piece of %s and gives you a nasty papercut!" % (fighter, fighterweapon))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (fighter, fighterweapon))
				fighterwin += 1
				round += 1
				continue
			if answer.lower() == "rock" and fighterweapon == "scissors":
				self.caller.msg("|/You grab a rock and bash %s in the face!" % (fighter))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (self.caller.key, answer))
				playerwin += 1
				round += 1
				continue
			if answer.lower() == "rock" and fighterweapon == "rock":
				self.caller.msg("|/|mAnnouncer|n says: TIE ROUND!!")
				round += 1
				continue
			if answer.lower() == "paper" and fighterweapon == "scissors":
				self.caller.msg("|/%s picks up a pair of %s and stabs you in the shoulder!" % (fighter, fighterweapon))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (fighter, fighterweapon))
				fighterwin += 1
				round += 1
				continue
			if answer.lower() == "paper" and fighterweapon == "rock":
				self.caller.msg("|/You pick up a piece of paper and give %s a nasty papercut!" % (fighter))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (self.caller.key, answer))
				playerwin += 1
				round += 1
				continue
			if answer.lower() == "paper" and fighterweapon == "paper":
				self.caller.msg("|/|mAnnouncer|n says: TIE ROUND!!")
				round += 1
				continue
			if answer.lower() == "scissors" and fighterweapon == "rock":
				self.caller.msg("|/%s grabs a rock and bashes you in the face!" % (fighter))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (fighter, fighterweapon))
				fighterwin += 1
				round += 1
				continue
			if answer.lower() == "scissors" and fighterweapon == "paper":
				self.caller.msg("|/You pick up a pair of scissors and stab %s in the shoulder!" % (fighter))
				self.caller.msg("|mAnnouncer|n says: %s wins with %s!" % (self.caller.key, answer))
				playerwin += 1
				round += 1
				continue
			if answer.lower() == "scissors" and fighterweapon == "scissors":
				self.caller.msg("|/|mAnnouncer|n says: TIE ROUND!!")
				round += 1
				continue
		if playerwin == 2:
			self.caller.msg("|/You won $100!!")
			self.caller.db.cash += 100
		if fighterwin == 2:
			self.caller.msg("|/Sorry, you lost. Better luck next time.")
		if self.caller.tags.get("vip"):
			return
		if self.caller.db.cash >= 5000:
			self.caller.tags.add("vip")
			self.caller.msg("|r|/A representative from the 9th Circle approaches.|n")
			self.caller.msg("Hello %s, we've been observing you and have determined we like your style.|/I would like to extend an invitation to our VIP lounge area.|/The bouncer has already been alerted that you're on the approved list.|/We hope to continue to have your patronage, and thank you for choosing the 9th Circle SpiceEasy." % (self.caller.key))
			return

class OctagonCmdSet(CmdSet):
	key = "OctagonCmdSet"
	def at_cmdset_creation(self):
		self.add(manfight())
	
class octagon(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The fighting pit is dug down into the floor and covered, floor and walls, in ice. Blood and teeth are frozen into the ice from previous fights.|/A sign reads 'Come |cWrestle|n in the octagon, free to enter, $100 if you win.'"
		self.cmdset.add_default(OctagonCmdSet, permanent=True)
		self.locks.add("get:false()")