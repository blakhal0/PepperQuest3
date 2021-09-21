from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class endoftheworld(default_cmds.MuxCommand):
	key = "ritual"
	auto_help = True
	def func(self):
		if self.caller.tags.get("acolyte") and self.caller.search("Spiceronomicon", location=self.caller, quiet=True) and self.caller.search("Ruby Seed", location=self.caller, quiet=True) and self.caller.search("Emerald Seed", location=self.caller, quiet=True) and self.caller.search("Citrine Seed", location=self.caller, quiet=True) and self.caller.search("Amethyst Seed", location=self.caller, quiet=True):
			self.caller.msg("You approach the altar, place the Spiceronomicon on the stand, open to the last page, and hold the glowing seeds out in front of you.")
			self.caller.msg("A distant voice echo's from beyond.")
			answer1 = yield("|/What was said at the beginning of time?")
			if answer1.lower() == "bring forth that which was the beginning":
				self.caller.msg("The sun is suddenly eclipsed, the sky is a fiery red. You can hear the people on the streets, the cars crashing into one another.")
				yield 3
				answer2 = yield("|/What was said to the everlasting flame?")
				if answer2.lower() == "bring forth that which is eternal":
					self.caller.msg("The air itself sizzles and crackles with heat and electricity, your skin and eyes burn from the heat.")
					yield 3
					answer3 = yield("|/What do you say upon this day, acolyte, servant of the Great Hot Ones?")
					if answer3.lower() == "bring forth that which is the end":
						yield 2
						self.caller.msg("|/The earth quakes, buildings sway and crack, giant fissures open spewing forth heat.")
						self.caller.msg("A great tear in the sky opens, you mind trembles and quivers in pain.")
						self.caller.msg("You swallow the 4 seeds.")
						self.caller.msg("A great mass of fiery tentacles burst forth from the rip as a crushing sound echo's in your head.")
						self.caller.msg("Acolyte, the one who has completed the ritual for our return, we have waited since before time for for your arrival.")
						yield 10
						self.caller.msg("We've been attempting to reach you regarding your cars extended warranty.....")
						yield 5
						self.caller.msg("The Great Hot Ones merge their being into your now immortal form.")
						self.caller.msg("You lay waste to all that exists, scrubbing this pathetic plane of existence clean except for your devoted followers, leaving only a worldwide jungle of hot peppers.")
						self.caller.msg("The few humans that survive now lead simple lives in their villages, caring for the plants, and worshiping you, the God of Spice.")
						yield("Please press enter to continue")
						self.caller.msg("|/|/|525  ::::::::   ::::::::  ::::    :::  ::::::::  :::::::::      ::: ::::::::::: ::::::::  :::|/|505:+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+:    :+: :+:|/|405+:+        +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+  +:+   +:+  +:+    +:+        +:+|/|305+#+        +#+    +:+ +#+ +:+ +#+ :#:        +#++:++#:  +#++:++#++: +#+    +#++:++#++ +#+|/|205+#+        +#+    +#+ +#+  +#+#+# +#+   +#+# +#+    +#+ +#+     +#+ +#+           +#+ +#+|/|105#+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#     #+# #+#    #+#    #+#|/|005  ########   ########  ###    ####  ########  ###    ### ###     ### ###     ########  ###|n|/Congratulations!! You've completed PepperQuest 3 as an Acolyte of the Order of the Burning Ring.")
						self.caller.msg("Your name will be added to the Book of Heroes in the Storyroom.")
						self.caller.msg("|/|/|rYou found the hidden storyline, I would like to offer you my personal congratulations and gratitude for digging that deep into the game. Thank you!!|n - Blakhal0|/|/")
						self.caller.msg("Let's see what your stats were:")
						self.caller.msg("++++++++++++++++++++++++++++++++++++++++")
						self.caller.msg("You completed the game as an Acolyte of Order of the Burning Ring, servant of the Great Hot Ones, and destroyed the world, jerk.")
						target = search_object("#2623")
						target[0].db.story += "|/|r%s|n completed the game as a |rSpice God|n and destroyed the world." % (self.caller.key)
						self.caller.msg("You shanked %s people in prison." % (self.caller.db.shived))
						self.caller.msg("You stunned %s people and NPC's." % (self.caller.db.stunned))
						self.caller.msg("You earned %s books of stamps." % (self.caller.db.stamps))
						self.caller.msg("You amassed %s cash gambling." % (self.caller.db.cash))
						self.caller.msg("|/|/Thanks for playing our game!!|/Without all of you, none of this would have happened.|/Again, thank you all so much!! Stay Spicy My Friends.")
						for o in self.caller.contents:
							o.delete()
						self.caller.tags.remove()
						self.caller.db.riddlefail = 0
						self.caller.db.faction = "none"
						self.caller.db.dreamreturn = "#178"
						self.caller.db.sendback = "#33"
						self.caller.db.bothered = 0
						self.caller.db.cartel = "none"
						self.caller.db.stamps = 0
						self.caller.db.shived = 0
						self.caller.db.debris = 0
						self.caller.db.spiceeasyanswer = ""
						self.caller.db.scanned = 0
						self.caller.db.claimed = 0
						self.caller.db.dreamfail = 0
						self.caller.db.stunned = 0
						self.caller.db.maced = 0
						self.caller.db.cash = 0
						self.caller.db.distributed = 0
						self.caller.tags.add("beatgame")
						beginning = yield("Press enter to return to the beginning of the game.")
						results = search_object("#2")
						self.caller.move_to(results[0], quiet=True, move_hooks=True)
						return
					else:
						self.caller.msg("The Spiceronomicon slams shut as the seeds burn your hand.")
						self.caller.msg("A distant voice echo's.")
						self.caller.msg("These are not the words of a true acolyte!!")
						return
				else:
					self.caller.msg("The Spiceronomicon slams shut as the seeds burn your hand.")
					self.caller.msg("A distant voice echo's.")
					self.caller.msg("These are not the words of a true acolyte!!")
					return
			else:
				self.caller.msg("The Spiceronomicon slams shut as the seeds burn your hand.")
				self.caller.msg("A distant voice echo's.")
				self.caller.msg("These are not the words of a true acolyte!!")
				return
		else:
			self.caller.msg("|/You have learned much, but did not find all the knowledge needed to bring forth the Great Hot Ones.")
			self.caller.msg("First you must meet a believer of the faith.|/You must obtain a book from a place of great suffering.|/Discover the 4 seeds found in darkest depths.|/And the knowledge one obtains from following the path of Dante passing through 9 portas.")
			self.caller.msg("Better luck next time.")
			return

class RitualCmdSet(CmdSet):
	key = "RitualCmdSet"
	def at_cmdset_creation(self):
		self.add(endoftheworld())
	
class altar(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An odd altar of glowing red tentacles. Looks like some kind of |cRitual|n has to be performed here."
		self.cmdset.add_default(RitualCmdSet, permanent=True)
		self.locks.add("get:false()")