from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class reform(default_cmds.MuxCommand):
	key = "Use Reformotron"
	aliases = ["use reformotron", "Use reformotron", "use Reformotron"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("reformactivity"):
			self.caller.msg("You are currently already engaged in an activity.|/Please allow the ReformOtron to complete the activity before choosing another.|/Enjoy your reformation!!")
			return
		self.caller.msg("|/Welcome to ReformOtron, the worlds first fully automated reformation system.")
		self.caller.msg("You are currently at the Re-education Center because you are a filthy scum-sucking spice addict.")
		self.caller.msg("You will remain at this center for education until you have reformed.")
		self.caller.msg("Please choose your activity:")
		answer = yield("-Reform|/-Therapy|/-Meal|/-Exercise|/-Relaxation")
		if answer.lower() in ["reform"]:
			self.caller.tags.add("reformactivity")
			self.caller.msg("|/You have chosen Reform")
			self.caller.msg("Thank you for acknowledging that you are human trash and need to reform to be a useful member of society.")
			self.caller.msg("Admitting that you are a bottom dwelling fiend is the first step.")
			yield 6
			answer2 = yield("|/Do you willingly, and of your own admission, admit that you are the trash of the world and are a spice fiend?")
			if answer2.lower() in ["y", "yes"]:
				self.caller.msg("|/Thank you for admitting the obvious, you are truly scum, but with our help, you may become better scum.")
				answer3 = yield("Do you recognize that your government is acting in your best interest and the interest of the rest of the country by:|/destroying your privacy|/instating constant surveillance|/and detaining and re-educating spice addicts for your own safety?")
				if answer3.lower() in ["y", "yes"]:
					self.caller.msg("|/It is good that you accept your own inability to make independent decisions, the government is to be trusted absolutely.|/A compliant citizen is a good citizen.")
					answer4 = yield("Do you wholeheartedly acknowledge that the greatest threat to the wonderful and patriotic way of life provided to you is:|/spice|/those who pollute the streets with spice|/those who consume spice against the governments wishes and warnings|/and those that enable the previously mentioned persons or entities in any way shape or form?")
					if answer4.lower() in ["y", "yes"]:
						self.caller.msg("|/This is very encouraging to hear.|/Constant vigilance by you, the lowly citizen, is one of the most important weapons we have against the spice epidemic.|/Remember, ratting on your neighbors, family, and friends is the most patriotic activity you can engage in.|/One final question and your reformation will be complete.")
						answer5 = yield("Please acknowledge that the following is your voluntary statement to be publicly distributed with your picture upon release from the reeducation center:|/I, %s, am a helpless spice fiend. My actions, if left unchecked, would result directly in the destruction of our country's safety and way of life. I further swear, upon penalty of death, my undying allegiance to this country and the great leader.|/Do you agree with this statement?" % (self.caller.key))
						if answer5.lower() in ["y", "yes"]:
							self.caller.msg("|/It is excellent that you have brought your thinking in line with the brilliant minds of this administrations leadership.")
							self.caller.msg("Your reeducation is complete.|/Thank you for using ReformOtron.")
							self.caller.msg("The room begins to fill with gas.")
							yield 8
							self.caller.msg("The world goes grey, you drop to the ground and pass out.")
							yield 3
							results = search_object("#33")
							self.caller.move_to(results[0], quiet=True, move_hooks=False)
							self.caller.tags.remove("reformactivity")
							self.caller.msg("|/You feel the calming comfort of your own bed as you regain consciousness.|/")
							return
						elif answer5.lower() in ["n", "no"]:
							self.caller.msg("That is unfortunate, but not unexpected. You will remain here until your reformation is complete.|/Enjoy your stay.")
							self.caller.tags.remove("reformactivity")
							return
						else:
							self.caller.msg("|/Attempts to input invalid data will not be tolerated.")
							self.caller.msg("Re-education Specialists will be along shortly to instruct you in proper input methods.")
							self.caller.msg("Your cell door swings open and you are shot with a bean bag round in the stomach.")
							self.caller.msg("|mRe-education Specialists say|n: Looks like we got a wanna be hacker here.|/YOUR OPTIONS ARE: REFORM, THERAPY, MEAL, EXERCISE, OR RELAXATION!!! FIGURE IT OUT!!")
							self.caller.msg("The Re-education Specialists kick you repeatedly until you black out.|/")
							self.caller.tags.remove("reformactivity")
							return
					elif answer4.lower() in ["n", "no"]:
						self.caller.msg("That is unfortunate, but not unexpected. You will remain here until your reformation is complete.|/Enjoy your stay.")
						self.caller.tags.remove("reformactivity")
						return
					else:
						self.caller.msg("|/Attempts to input invalid data will not be tolerated.")
						self.caller.msg("Re-education Specialists will be along shortly to instruct you in proper input methods.")
						self.caller.msg("Your cell door swings open and you are shot with a bean bag round in the stomach.")
						self.caller.msg("|mRe-education Specialists say|n: Looks like we got a wanna be hacker here.|/YOUR OPTIONS ARE: REFORM, THERAPY, MEAL, EXERCISE, OR RELAXATION!!! FIGURE IT OUT!!")
						self.caller.msg("The Re-education Specialists kick you repeatedly until you black out.|/")
						self.caller.tags.remove("reformactivity")
						return
				elif answer3.lower() in ["n", "no"]:
					self.caller.msg("That is unfortunate, but not unexpected. You will remain here until your reformation is complete.|/Enjoy your stay.")
					self.caller.tags.remove("reformactivity")
					return
				else:
					self.caller.msg("|/Attempts to input invalid data will not be tolerated.")
					self.caller.msg("Re-education Specialists will be along shortly to instruct you in proper input methods.")
					self.caller.msg("Your cell door swings open and you are shot with a bean bag round in the stomach.")
					self.caller.msg("|mRe-education Specialists say|n: Looks like we got a wanna be hacker here.|/YOUR OPTIONS ARE: REFORM, THERAPY, MEAL, EXERCISE, OR RELAXATION!!! FIGURE IT OUT!!")
					self.caller.msg("The Re-education Specialists kick you repeatedly until you black out.|/")
					self.caller.tags.remove("reformactivity")
					return
			elif answer2.lower() in ["n", "no"]:
				self.caller.msg("That is unfortunate, but not unexpected. You will remain here until your reformation is complete.|/Enjoy your stay.")
				self.caller.tags.remove("reformactivity")
				return
			else:
				self.caller.msg("|/Attempts to input invalid data will not be tolerated.")
				self.caller.msg("Re-education Specialists will be along shortly to instruct you in proper input methods.")
				self.caller.msg("Your cell door swings open and you are shot with a bean bag round in the stomach.")
				self.caller.msg("|mRe-education Specialists say|n: Looks like we got a wanna be hacker here.|/YOUR OPTIONS ARE: REFORM, THERAPY, MEAL, EXERCISE, OR RELAXATION!!! FIGURE IT OUT!!")
				self.caller.msg("The Re-education Specialists kick you repeatedly until you black out.|/")
				self.caller.tags.remove("reformactivity")
				return
		elif answer.lower() in ["therapy"]:
			self.caller.tags.add("reformactivity")
			self.caller.msg("|/You have chosen Therapy")
			self.caller.msg("Qualified therapists have been dispatched and will arrive soon to begin your session.")
			yield 6
			self.caller.msg("|/*BZZZZZZ* The cell door slides open and two 'Therapists' enter the room.")
			self.caller.msg("The 'Therapists' whip out extendible metal batons and cattle prods and begin to bludgeon you in the head while administering electro shock therapy to your groin.")
			self.caller.msg("|mTherapists say|n: YOU DON'T EVER WANT SPICE AGAIN, ISN'T THAT RIGHT YOU PIECE OF GARBAGE!!!")
			self.caller.msg("You are soon beaten to unconsciousness, convulsing as you begin to vomit.")
			self.caller.tags.remove("reformactivity")
			return
		elif answer.lower() in ["meal", "food"]:
			self.caller.tags.add("reformactivity")
			self.caller.msg("|/You have chosen Meal")
			self.caller.msg("Our world renounced chefs are preparing a delicious and tasty meal for you now. Please wait for room service to deliver.")
			yield 5
			self.caller.msg("|/A small slot in the cell door slides open near the floor and a tray is tossed in.")
			self.caller.msg("Carefully poking a few of the items you muster up courage and try a few bites...")
			self.caller.msg("Oh, yumm, plain oatmeal, half cooked potato with the skin removed, a small salad of blanched kale, single piece of white bread without butter, and a glass of room temperature water.")
			self.caller.msg("Might as well go lick the wall to try and get some flavor.")
			self.caller.msg("You choke down the tasteless 'meal' and put the tray back.")
			self.caller.msg("The Reformotron lights up, 'Seasoning is the devils playground, a good citizen derives happiness from denying the devil.'")
			self.caller.tags.remove("reformactivity")
			return
		elif answer.lower() in ["exercise"]:
			self.caller.tags.add("reformactivity")
			self.caller.msg("|/You have chosen Exercise")
			self.caller.msg("Exercise is key to a happy and healthy lifestyle.|/The exercise wolverine will be arriving in your cell momentarily, please attempt to avoid injury during exercise.|/We care about your safety.")
			self.caller.msg("We are currently injecting the wolverine with aggression drugs and poking it with a stick.")
			yield 6
			self.caller.msg("|/*BZZT* The cell door slides open, someone dumps a furious wolverine into your cell and the door slams shut.")
			self.caller.msg("The wolverine attacks the door wildly, snarling and snapping its jaws, foaming spit flying everywhere, as you attempt to climb on top of the sink/toilet hoping it won't see you.")
			yield 5
			self.caller.msg("The wolverine turns and stares at you...")
			yield 4
			self.caller.msg("You spend the next several hours attempting to avoid the wolverine, unsuccessfully, while being mauled.")
			self.caller.tags.remove("reformactivity")
			return
		elif answer.lower() in ["relaxation"]:
			self.caller.tags.add("reformactivity")
			self.caller.msg("|/You have chosen Relaxation")
			self.caller.msg("An ear splitting siren begins to wail in the cell while a lightning bright light flashes.")
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 6
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("|/RELAX. RELAX. RELAX. RELAX.")
			yield 3
			self.caller.msg("WWWOOooooooOOOOOWWWWWWWWOOOOooooooWWWWWW")
			yield 3
			self.caller.msg("You begin to bash your head on the wall in an attempt to knock yourself out.|/Thankfully, you finally do it hard enough and you're out.")
			self.caller.tags.remove("reformactivity")
			return
		else:
			self.caller.msg("|/Attempts to input invalid data will not be tolerated.")
			self.caller.msg("Re-education Specialists will be along shortly to instruct you in proper input methods.")
			self.caller.msg("Your cell door swings open and you are shot with a bean bag round in the stomach.")
			self.caller.msg("|mRe-education Specialists say|n: Looks like we got a wanna be hacker here.|/YOUR OPTIONS ARE: REFORM, THERAPY, MEAL, EXERCISE, OR RELAXATION!!! FIGURE IT OUT!!")
			self.caller.msg("The Re-education Specialists kick you repeatedly until you black out.|/")
			return

class ReformotronCmdSet(CmdSet):
	key = "ReformotronCmdSet"
	def at_cmdset_creation(self):
		self.add(reform())
	
class reformotron(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A screen behind a thick piece of plexiglass glows lightly, Please |cUse Reformotron|n to begin reformation procedures."
		self.cmdset.add_default(ReformotronCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You try everything you can think of, there's no way possible to get to the screen."