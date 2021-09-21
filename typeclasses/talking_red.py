from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class talkred(default_cmds.MuxCommand):
	key = "talk red"
	aliases = ["Talk Red", "Talk red", "talk Red"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|m%s|n says: I understand you are a man who knows how to get things." % (self.caller.key))
		self.caller.msg("|mRed|n says: I have been known to locate certain things, from time to time.")
		self.caller.msg("|/|mRed|n says: Welcome to Red's prison emporium. Do you have a request or would you like to view the merchandise?")
		answer = yield("Request or Merch?")
		if answer.lower() in ["request", "r"]:
			request = yield("|/|mRed|n says: Ok, what do you need?")
			if request.lower() in ["shank"]:
				if self.caller.search("Shank", location=self.caller, quiet=True):
					self.caller.msg("|/|mRed|n says: You only need one pal.")
					return
				self.caller.msg("|/|mRed|n says: Yeah, I got one. Keep yourself safe out there.")
				shiv_proto = {
				"key": "Shank",
				"typeclass": "typeclasses.stabby.stabby",
				"location": self.caller
				}
				spawn(shiv_proto)
				return
			if request.lower() in ["spiceronomicon"]:
				if self.caller.search("Spiceronomicon", location=self.caller, quiet=True):
					self.caller.msg("|/|mRed|n says: Acolyte, you already possess the sacred text.")
					return
				if not self.caller.tags.get("acolyte"):
					self.caller.msg("|/|mRed|n says: I have no idea what you're talking about.")
					return
				self.caller.msg("|/|mRed|n says: You seek the ultimate knowledge? Take care, great loss was suffered to obtain this book.")
				spiceonomicon_proto = {
				"key": "Spiceronomicon",
				"typeclass": "typeclasses.objects.nodropbook",
				"story": "With great care you open the worn and ancient tome.|/You examine the pages, the writing a deep red. Was this written in blood??|/Your fingers begin to tingle and your eyes burn, not blood, cayenne pepper ink.|/You lick your finger to turn the page, oooh spicy!!|/Your eyes blur with stinging tears as you read the scrawling prophecies of the mad hermit.|/'...Woe to the hero who must make the sacrifice and so will mark the beginning of the return of the great hot ones.'|/'In this time will rise an acolyte who will face persecution and suffering.'|/'First shall the hero find them self across the Acheron unwittingly in the abyss.'|/'Next shall the hero meet the third, and name him so in his house of indulgence.'|/'In darkest depths are sowed the seeds of eternal flame.'|/'Upon the precipice of the lowest ring shall the gates be opened and into the world be reborn its end.'|/You flip through the book and stop on the final page.|/'The Wanderings of Portas 1, 9: Beatrice dispatches the guide who leads the path to divine the word.'|/ibiaebntbbmvwubysummsxsridpuivxehbwltqiisqmnnaxldxsrjkcomfrvhwancaotmqtortaogodmftypmhlkkdhovmsyqmngcihvjihxizksgsmiavddxumijvvrtflsjejrueqqsumlrkrdwcqgwhuifaxkbpslcktvtuaqjhueqbjnvfxeqmwizjjcqcixomjduotnkphhcrukwav",
				"desc": "An ancient and worn tome.",
				"location": self.caller
				}
				spawn(spiceonomicon_proto)
				return
			if request.lower() in ["hammer"]:
				if self.caller.search("Hammer", location=self.caller, quiet=True):
					self.caller.msg("|/|mRed|n says: You only need one pal.")
					return
				if not self.caller.db.cartel == "reapers":
					self.caller.msg("|/|mRed|n says: Sorry, fresh out.")
					return
				self.caller.msg("|/|mRed|n says: Sure thing, I got that.")
				if request.lower() in ["hammer"]:
					if self.caller.db.stamps >= 10:
						self.caller.db.stamps -= 10
						self.caller.msg("|mRed|n says: Looks like you got the funds, here you go.")
						self.caller.msg("Red hands you the hammer.")
						hammer_proto = {
						"key": "Hammer",
						"typeclass": "typeclasses.objects.DefaultObject",
						"desc": "A small hammer.",
						"location": self.caller
						}
						spawn(hammer_proto)
						return
					else:
						self.caller.msg("|mRed|n says: Looks like you're a bit short on funds, the hammer is 10 books of stamps, you've only got %s" % (self.caller.db.stamps))
						return
			if request.lower() in ["poster"]:
				if self.caller.search("Poster", location=self.caller, quiet=True):
					self.caller.msg("|/|mRed|n says: You only need one pal.")
					return
				if not self.caller.db.cartel == "reapers":
					self.caller.msg("|/|mRed|n says: Sorry, fresh out.")
					return
				if self.caller.db.stamps >= 5:
					self.caller.db.stamps -= 5
					self.caller.msg("|mRed|n says: Looks like you got the funds, here you go.")
					self.caller.msg("Red hands you the poster.")
					poster_proto = {
					"key": "Poster",
					"typeclass": "typeclasses.objects.DefaultObject",
					"desc": "A poster of Raquel Welch",
					"location": self.caller
					}
					spawn(poster_proto)
					return
				else:
					self.caller.msg("|mRed|n says: Looks like you're a bit short on funds, the poster is 5 books of stamps, you've only got %s" % (self.caller.db.stamps))
					return
			else:
				self.caller.msg("|/|mRed|n says: Sorry friend, but that just ain't something I can get my hands on right now.")
		elif answer.lower() in ["merch", "merchandise", "m"]:
			self.caller.msg("|/|mRed|n says: Here's what I got on hand:")
			list = ""
			if not self.caller.search("Dream Spice", location=self.caller, quiet=True):
				list += "Dream Spice: 1 book of stamps"
			if self.caller.tags.get("keymaker") and not self.caller.search("Soap", location=self.caller, quiet=True):
				list += "|/Soap: On the house"
			if not self.caller.search("Plastic", location=self.caller, quiet=True) and not self.caller.search("Dice", location=self.caller, quiet=True):
				list += "|/Waste Plastic: 2 books of stamps"
			if list == "":
				list = "|/|mRed|n says: I'm fresh out of everything, try stopping by later."
				return
			self.caller.msg("%s" % (list))
			purchase = yield("|/|mRed|n says: Ok, what do you need?")
			if purchase.lower() in ["soap"]:
				if self.caller.search("Soap", location=self.caller, quiet=True):
					self.caller.msg("|mRed|n says: Cleanliness is next to godliness, but you only need one bar of soap.")
					return
				self.caller.msg("|/|mRed|n says: Sure thing, this one's on the house, don't get used to that.|/Red hands you a bar of soap.")
				soap_proto = {
				"key": "Soap",
				"typeclass": "typeclasses.objects.nodropobj",
				"desc": "A fresh bar of soap.",
				"location": self.caller
				}
				spawn(soap_proto)
				return
			if purchase.lower() in ["dream spice", "spice"]:
				if self.caller.search("Dream Spice", location=self.caller, quiet=True):
					self.caller.msg("|mRed|n says: You've already got some dream spice, no need to make a stash.")
					return
				if self.caller.db.stamps >= 1:
					self.caller.db.stamps -= 1
					self.caller.msg("|/|mRed|n says:Sure thing, one dose of Dream Spice.|/Red hands you the Dream Spice.")
					dspice_proto = {
					"key": "Dream Spice",
					"typeclass": "typeclasses.objects.nodropobj",
					"desc": "A small dose of dream spice.",
					"location": self.caller
					}
					spawn(dspice_proto)
					return
				else:
					self.caller.msg("|mRed|n says: Looks like you're a bit short on funds, dream spice is 1 book of stamps, you've only got %s" % (self.caller.db.stamps))
					return
			if purchase.lower() in ["waste plastic", "plastic"]:
				if self.caller.search("Plastic", location=self.caller, quiet=True):
					self.caller.msg("|mRed|n says: You've already got some junk plastic, why would you want more.")
					return
				if self.caller.db.stamps >= 2:
					self.caller.db.stamps -= 2
					self.caller.msg("|/|mRed|n says:Sure thing, one chunk of junk plastic.|/Red hands you the Plastic.")
					plastic_proto = {
					"key": "Plastic",
					"typeclass": "typeclasses.objects.nodropobj",
					"desc": "A handfull of junk white plastic.",
					"location": self.caller
					}
					spawn(plastic_proto)
					return
				else:
					self.caller.msg("|mRed|n says: Looks like you're a bit short on funds, this plastic is 2 book of stamps, you've only got %s" % (self.caller.db.stamps))
					return
			else:
				self.caller.msg("|/|mRed|n says: I don't have that, did you not understand the options? If there's something specific you want to request, make a request.")
				return
		else:
			self.caller.msg("|/|mRed|n says: Clean the mush out of your mouth, I can't understand a damn thing you're saying.")
			return

class RedCmdSet(CmdSet):
	key = "RedCmdSet"
	def at_cmdset_creation(self):
		self.add(talkred())

class red(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Red sits on his bunk, glasses perched on the end of his nose, thumbing through a magazine."
		self.cmdset.add_default(RedCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mRed|n says: You do that again, and you're going to get busy dying real fast."