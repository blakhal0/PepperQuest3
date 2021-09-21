from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class finalscene(default_cmds.MuxCommand):
	key = "decision"
	auto_help = True
	def func(self):
		if self.caller.db.faction == "fed":
			self.caller.tags.add("noleave")
			if not self.caller.tags.get("doubleagent"):
				self.caller.msg("|/|m%s|n says: I don't know what the hell is going on here, but you're both under arrest, drop your weapons." % (self.caller.key))
				self.caller.msg("|mJanitor|n says: Agent %s, you know me, but not my true name." % (self.caller.key))
				self.caller.msg("Janitor rips off his fake mustache")
				self.caller.msg("|mJanitor|n says: My name is Sterling Archer.")
				self.caller.msg("|mArcher|n says: Director Keye tried to have me assassinated because I was getting too close to figuring out what he was up to.")
				self.caller.msg("|mArcher|n says: You see these two have been in cahoots running a spice smuggling ring and splitting the profits.")
				self.caller.msg("|mArcher|n says: I faked my death and took a job as a janitor at the NSA so I could gather intel and figure out who his contact was, and rob them.")
				self.caller.msg("|mArcher|n says: So, we're in a bit of a pickle here, there's a lot of cash and product in this room, and obviously not all three of us are walking out.")
				self.caller.msg("|mArcher|n says: So how do you want to handle this?")
				answer = yield("|/Uphold your oath as an NSA agent and |cArrest|n Leia, bringing an end to the spice scourge in this country.|/Go dirty, |cShoot|n Leia and split the money and product.")
				if answer.lower() in ["arrest"]:
					self.caller.msg("|/You train your weapon on Leia.")
					self.caller.msg("|m%s|n says: Leia, your days of running spice are over, you're under arrest for crimes against the United States." % (self.caller.key))
					self.caller.msg("|m%s|n says: Archer, you can take the money, that amount of spice is a life sentence for her, take the cash and get out of here, enjoy your retirement." % (self.caller.key))
					self.caller.msg("|/|/|/In the following days and weeks, Leia is prosecuted, and sentenced to life.")
					self.caller.msg("Director Keye is arrested and charged with treason. His execution by hanging is broadcast live on all major networks.")
					self.caller.msg("Several other high ranking members of the government and other NSA agents are arrested and charged with high crimes against the nation.")
					self.caller.msg("You have singlehandedly freed the nation of the terrifying grip of tasty food and are promoted to Director of the NSA where you rule with an iron fist, crushing corruption and the spice trade.")
					self.caller.msg("Jerk.")
					self.caller.tags.add("honestfed")
				elif answer.lower() in ["shoot"]:
					self.caller.msg("|/You train your weapon on Leia and fire two rounds into her chest and one in her head.")
					self.caller.msg("You nod to Archer.")
					self.caller.msg("|m%s|n says: Always doubletap." % (self.caller.key))
					self.caller.msg("While Leia's corpse leaks blood on the floor, you split the cash and spice with Archer.")
					self.caller.msg("You leave the 9th Circle SpiceEasy, catch the first flight to Cuba and spend the rest of your days enjoying warm sun, cold drinks, and spicy food.")
					self.caller.tags.add("dirtyfed")
				else:
					self.caller.msg("|/You turnip brained idiot, you have to choose to either |cArrest|n or |cShoot|n. It's not that hard. Try again.")
					return
			elif self.caller.tags.get("doubleagent"):
				self.caller.msg("|/|m%s|n says: I don't know what the hell is going on here, but you're both under arrest, drop your weapons." % (self.caller.key))
				self.caller.msg("|mJanitor|n says: Agent %s, you know me, but not my true name." % (self.caller.key))
				self.caller.msg("Janitor rips off his fake mustache")
				self.caller.msg("|mJanitor|n says: My name is Sterling Archer.")
				self.caller.msg("|mArcher|n says: Director Keye tried to have me assassinated because I was getting too close to figuring out what he was up to.")
				self.caller.msg("|mArcher|n says: You see these two have been in cahoots running a spice smuggling ring and splitting the profits.")
				self.caller.msg("|mArcher|n says: I faked my death and took a job as a janitor at the NSA so I could gather intel and figure out who his contact was, and rob them.")
				self.caller.msg("|mArcher|n says: So, we're in a bit of a pickle here, there's a lot of cash and product in this room, and obviously not all three of us are walking out.")
				self.caller.msg("|mArcher|n says: So how do you want to handle this?")
				answer = yield("|/Uphold your oath as an NSA agent and |cArrest|n Leia, bringing an end to the spice scourge in this country.|/Go dirty, |cShoot|n Leia and split the money and product.|/Pull a |cDoublecross|n, shoot Archer and join the Ghost Reapers Cartel.")
				if answer.lower() in ["arrest"]:
					self.caller.msg("|/You train your weapon on Leia.")
					self.caller.msg("|m%s|n says: Leia, your days of running spice are over, you're under arrest for crimes against the United States." % (self.caller.key))
					self.caller.msg("|m%s|n says: Archer, I don't need the money, that amount of spice is a life sentence for her, take it and get out of here, enjoy your retirement." % (self.caller.key))
					self.caller.msg("|/|/|/In the following days and weeks, Leia is prosecuted, and sentenced to life.")
					self.caller.msg("Director Keye is arrested and charged with treason. His execution by hanging is broadcast live on all major networks.")
					self.caller.msg("Several other high ranking members of the government and other NSA agents are arrested and charged with high crimes against the nation.")
					self.caller.msg("You have singlehandedly freed the nation of the terrifying grip of tasty food and are promoted to Director of the NSA where you rule with an iron fist, crushing corruption and the spice trade.")
					self.caller.msg("Jerk.")
					self.caller.tags.add("honestfed")
				elif answer.lower() in ["shoot"]:
					self.caller.msg("|/You train your weapon on Leia and fire two rounds into her chest and one in her head.")
					self.caller.msg("You nod to Archer.")
					self.caller.msg("|m%s|n says: Always doubletap." % (self.caller.key))
					self.caller.msg("While Leia's corpse leaks blood on the floor, you split the cash and spice with Archer.")
					self.caller.msg("You leave the 9th Circle SpiceEasy, catch the first flight to Cuba and spend the rest of your days enjoying warm sun, cold drinks, and spicy food.")
					self.caller.tags.add("dirtyfed")
				elif answer.lower() in ["doublecross"]:
					self.caller.msg("|/You train your weapon on Archer and fire two rounds into his chest and one in his head.")
					self.caller.msg("You nod to Leia.")
					self.caller.msg("|m%s|n says: Always doubletap." % (self.caller.key))
					self.caller.msg("|m%s|n says: So, I'm interested in joining your organization, any openings?" % (self.caller.key))
					self.caller.db.faction == "cartel"
					self.caller.msg("|mLeia|n says: Of course, we can always use another source at the NSA.")
					self.caller.msg("|m%s|n says: Oh, I'll be the only one..." % (self.caller.key))
					self.caller.msg("You officially become a double agent.")
					self.caller.msg("After a 'tragic' accident that resulted in the deaths of the Director and both Executive Director's, and many many successful operations that bring down all opposition to the Cartel, you are promoted to the Director of the NSA.")
					self.caller.msg("You have a long and luxurious life, stupidly rich from all the money the Cartel brings in, with your assistance.")
					self.caller.msg("You're a bad person, but the country gets to keep enjoying spicy food, for a price.")
					self.caller.tags.add("doubleagentfed")
				else:
					self.caller.msg("|/You turnip brained idiot, you have to choose to either |cArrest|n, |cShoot|n, or |cDoublecross|n. It's not that hard. Try again.")
					return
			wastetime = yield("|/|/Please press enter to continue")
			self.caller.msg("|/|/|525  ::::::::   ::::::::  ::::    :::  ::::::::  :::::::::      ::: ::::::::::: ::::::::  :::|/|505:+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+:    :+: :+:|/|405+:+        +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+  +:+   +:+  +:+    +:+        +:+|/|305+#+        +#+    +:+ +#+ +:+ +#+ :#:        +#++:++#:  +#++:++#++: +#+    +#++:++#++ +#+|/|205+#+        +#+    +#+ +#+  +#+#+# +#+   +#+# +#+    +#+ +#+     +#+ +#+           +#+ +#+|/|105#+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#     #+# #+#    #+#    #+#|/|005  ########   ########  ###    ####  ########  ###    ### ###     ### ###     ########  ###|n|/Congratulations!! You've completed PepperQuest 3 as an Agent of the National Spice Agency.")
			self.caller.msg("Your name will be added to the Book of Heroes in the Storyroom.")
			self.caller.msg("Let's see what your stats were:")
			self.caller.msg("++++++++++++++++++++++++++++++++++++++++")
			if self.caller.tags.get("honestfed"):
				self.caller.msg("You completed the game as a Honest Agent of the National Spice Agency.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Honest Agent of the National Spice Agency." % (self.caller.key)
			if self.caller.tags.get("dirtyfed"):
				self.caller.msg("You completed the game as a Dirty Rat of an Agent of the National Spice Agency.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Dirty Rat of an Agent of the National Spice Agency." % (self.caller.key)
			if self.caller.tags.get("doubleagentfed"):
				self.caller.msg("You completed the game as a Dirty Double Crossing Double Agent, who changed sides at the last minute to join the Ghost Reapers.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Dirty Double Crossing Double Agent, who changed sides at the last minute to join the Ghost Reapers." % (self.caller.key)
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
		if self.caller.db.faction == "cartel":
			self.caller.tags.add("noleave")
			if not self.caller.tags.get("doubleagent"):
				self.caller.msg("|/|m%s|n says: I don't know what the hell is going on here, but you're both getting shot if I don't get some answers." % (self.caller.key))
				self.caller.msg("|mLeia|n says: %s, you know me, this is our informant in the NSA." % (self.caller.key))
				self.caller.msg("|mLeia|n says: Apparently he isn't quite who he said he was, he's a burnt spy trying to rip us off.")
				self.caller.msg("|mLeia|n says: There's no reason to make a thing out of this, let's kill him and together we'll run the cartel.")
				self.caller.msg("|mBurnt Spy|n says: Hey, %s, she's lying. Director Keye and her are in cahoots. Keye tried to have me killed and she's the proof I need to bust him. I just need her. You, the money, and the spice can walk right out of here, and I promise your organization will drop off the NSA's radar." % (self.caller.key))
				self.caller.msg("|mLeia|n says: So, how do you want to handle this?")
				answer = yield("|/Protect the cartel and its property, |cShoot|n the NSA agent.|/Seize power, |cSacrifice|n Leia and become the head of the cartel.")
				if answer.lower() in ["shoot"]:
					self.caller.msg("|/You train your weapon on the Burnt Spy.")
					self.caller.msg("|m%s|n says: I don't like that you've been working with the enemy Leia, but family is family." % (self.caller.key))
					self.caller.msg("You fire two rounds into his chest and one in his head.")
					self.caller.msg("You nod to Leia.")
					self.caller.msg("|m%s|n says: Always doubletap." % (self.caller.key))
					self.caller.msg("The lads from the SpiceEasy are no strangers to disposing of a body, by the time they're done, there never was a body and the room is spotless.")
					self.caller.msg("Over the next months you implement military grade encrypted communications, covert operations training, and implement new ingenious smuggling operations.")
					self.caller.msg("The Faucheurs Fantomes crush their competition and become the only name in the spice game.")
					self.caller.msg("The people of the country see you as heroes, supplying spice with minimal bloodshed, reasonable prices, and top notch quality.")
					self.caller.tags.add("honestcartel")
				elif answer.lower() in ["sacrifice"]:
					self.caller.msg("|/You train your weapon on Leia")
					self.caller.msg("You nod to the Burnt Spy.")
					self.caller.msg("|m%s|n says: The traitorous swine is all yours." % (self.caller.key))
					self.caller.msg("|mBurnt Spy|n says: Leia, your days of running spice are over, you're under arrest for crimes against the United States.")
					self.caller.msg("The Burnt Spy arrests Leia.")
					self.caller.msg("|mBurnt Spy|n says: As a sign of good will, you can keep the money and the spice, I just need a confession out of her.")
					self.caller.msg("Director Keye is arrested and charged with treason. His execution by hanging is broadcast live on all major networks.")
					self.caller.msg("Several other high ranking members of the government and other NSA agents are arrested and charged with high crimes against the nation.")
					self.caller.msg("Under your administration the Faucheurs Fantomes become the only name in the spice game. The people are happy, and your pockets are full.")
					self.caller.tags.add("dirtycartel")
				else:
					self.caller.msg("|/You turnip brained idiot, you have to choose to either |cArrest|n, |cShoot|n, or |cDoublecross|n. It's not that hard. Try again.")
					return
			if self.caller.tags.get("doubleagent"):
				self.caller.msg("|/|m%s|n says: I don't know what the hell is going on here, but you're both getting shot if I don't get some answers." % (self.caller.key))
				self.caller.msg("|mLeia|n says: %s, you know me, this is our informant in the NSA." % (self.caller.key))
				self.caller.msg("|mLeia|n says: Apparently he isn't quite who he said he was, he's a burnt spy trying to rip us off.")
				self.caller.msg("|mLeia|n says: There's no reason to make a thing out of this, let's kill him and together we'll run the cartel.")
				self.caller.msg("|mBurnt Spy|n says: Hey, %s, she's lying. Director Keye and her are in cahoots. Keye tried to have me killed and she's the proof I need to bust him. I just need her. You, the money, and the spice can walk right out of here, and I promise your organization will drop off the NSA's radar." % (self.caller.key))
				self.caller.msg("|mLeia|n says: So, how do you want to handle this?")
				answer = yield("|/Protect the cartel and its property, |cShoot|n the NSA agent.|/Seize power, |cSacrifice|n Leia and become the head of the cartel.|/Choose to |cDefect|n and join the NSA.")
				if answer.lower() in ["shoot"]:
					self.caller.msg("|/You train your weapon on the Burnt Spy.")
					self.caller.msg("|m%s|n says: I don't like that you've been working with the enemy Leia, but family is family." % (self.caller.key))
					self.caller.msg("You fire two rounds into his chest and one in his head.")
					self.caller.msg("You nod to Leia.")
					self.caller.msg("|m%s|n says: Always doubletap." % (self.caller.key))
					self.caller.msg("The lads from the SpiceEasy are no strangers to disposing of a body, by the time they're done, there never was a body and the room is spotless.")
					self.caller.msg("Over the next months you implement military grade encrypted communications, covert operations training, and implement new ingenious smuggling operations.")
					self.caller.msg("The Faucheurs Fantomes crush their competition and become the only name in the spice game.")
					self.caller.msg("The people of the country see you as heroes, supplying spice with minimal bloodshed, reasonable prices, and top notch quality.")
					self.caller.tags.add("honestcartel")
				elif answer.lower() in ["sacrifice"]:
					self.caller.msg("|/You train your weapon on Leia")
					self.caller.msg("You nod to the Burnt Spy.")
					self.caller.msg("|m%s|n says: The traitorous swine is all yours." % (self.caller.key))
					self.caller.msg("|mBurnt Spy|n says: Leia, your days of running spice are over, you're under arrest for crimes against the United States.")
					self.caller.msg("The Burnt Spy arrests Leia.")
					self.caller.msg("|mBurnt Spy|n says: As a sign of good will, you can keep the money and the spice, I just need a confession out of her.")
					self.caller.msg("Director Keye is arrested and charged with treason. His execution by hanging is broadcast live on all major networks.")
					self.caller.msg("Several other high ranking members of the government and other NSA agents are arrested and charged with high crimes against the nation.")
					self.caller.msg("True to his word, the Burnt Spy leaves the cartel alone for as long as you are in charge.")
					self.caller.msg("You occasionally throw him a tip about up and coming competitors and they are stamped out with ruthless aggression.")
					self.caller.msg("Under your administration the Faucheurs Fantomes become the only name in the spice game. The people are happy and your pockets are full.")
					self.caller.tags.add("dirtycartel")
				elif answer.lower() in ["defect"]:
					self.caller.msg("|/You train your weapon on Leia")
					self.caller.msg("You nod to the Burnt Spy.")
					self.caller.msg("|m%s|n says: Hows about a job?" % (self.caller.key))
					self.caller.msg("|m%s|n says: I'm sick and tired of these jerks bossing me around." % (self.caller.key))
					self.caller.msg("|mLeia|n says: YOU FUCKING TRAITOR!")
					self.caller.msg("You shoot Leia in the knee")
					self.caller.msg("|m%s|n says: Sorry, I couldn't hear you over the sound of me shooting you." % (self.caller.key))
					self.caller.msg("|mBurnt Spy|n says: Well, you certainly have the skills for the job. You're hired.")
					self.caller.msg("|mBurnt Spy|n says: Leia, your days of running spice are over, you're under arrest for crimes against the United States.")
					self.caller.msg("After Leia rolls on Director Keye, he is arrested and charged with treason. His execution by hanging is broadcast live on all major networks.")
					self.caller.msg("Several other high ranking members of the government and other NSA agents are arrested and charged with high crimes against the nation.")
					self.caller.msg("The Burnt Spy is reinstated, and after praising your efforts as 'essential' you're promoted to a high ranking position where you spend your days taking down your former colleagues, making a load of money, and performing 'sampling and off-site storage' of confiscated spice.")
					self.caller.tags.add("doubleagentcartel")
				else:
					self.caller.msg("|/You turnip brained idiot, you have to choose to either |cArrest|n, |cShoot|n, or |cDoublecross|n. It's not that hard. Try again.")
					return
			wastetime = yield("|/|/Please press enter to continue")
			self.caller.msg("|/|/|525  ::::::::   ::::::::  ::::    :::  ::::::::  :::::::::      ::: ::::::::::: ::::::::  :::|/|505:+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+:    :+: :+:|/|405+:+        +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+  +:+   +:+  +:+    +:+        +:+|/|305+#+        +#+    +:+ +#+ +:+ +#+ :#:        +#++:++#:  +#++:++#++: +#+    +#++:++#++ +#+|/|205+#+        +#+    +#+ +#+  +#+#+# +#+   +#+# +#+    +#+ +#+     +#+ +#+           +#+ +#+|/|105#+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#     #+# #+#    #+#    #+#|/|005  ########   ########  ###    ####  ########  ###    ### ###     ### ###     ########  ###|n|/|/You've completed PepperQuest 3 as a member of the Faucheurs Fantomes.")
			self.caller.msg("Your name will be added to the Book of Heroes in the Storyroom.")
			self.caller.msg("Let's see what your stats were:")
			self.caller.msg("++++++++++++++++++++++++++++++++++++++++")
			if self.caller.tags.get("honestcartel"):
				self.caller.msg("You completed the game as a Honest Member of the Faucheurs Fantomes aka Ghost Reapers.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Honest Member of the Faucheurs Fantomes aka Ghost Reapers." % (self.caller.key)
			if self.caller.tags.get("dirtycartel"):
				self.caller.msg("You completed the game as a Dirty Rat of a Member of the Faucheurs Fantomes aka Ghost Reapers.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Dirty Rat of a Member of the Faucheurs Fantomes aka Ghost Reapers." % (self.caller.key)
			if self.caller.tags.get("doubleagentcartel"):
				self.caller.msg("You completed the game as a Dirty Double Crossing Double Agent Cartel Member, who changed sides at the last minute to join the National Spice Agency.")
				target = search_object("#2623")
				target[0].db.story += "|/%s completed the game as a Dirty Double Crossing Double Agent Cartel Member, who changed sides at the last minute to join the National Spice Agency." % (self.caller.key)
			self.caller.msg("You shanked %s people in prison." % (self.caller.db.shived))
			self.caller.msg("You 'distributed free product' to %s people and NPC's." % (self.caller.db.maced))
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
		return

class BattleCmdSet(CmdSet):
	key = "BattleCmdSet"
	def at_cmdset_creation(self):
		self.add(finalscene())

class battle(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(BattleCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")