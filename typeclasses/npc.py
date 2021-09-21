from typeclasses.objects import DefaultObject
import random

class npc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.msg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "Kidnapping is a crime."

descriptions = ["They're just standing there staring off into space", "Sweating profusely, they dab their forehead", "They don't even appear to recognize you, they're just going about their day.", "Just a normal citizen.", "A business person in a very fancy suit.", "An expressionless face stares back at you."]
phrases = ["Hey, watch where you're going!", "Get away from me, why are you talking to me??", "Traffic around here is crazy!", "Oh, I shouldn't have eaten that 8th hotdog, uhhhhh, my stomach.", "Sometimes I think some we were all made just to fill up space, no real purpose at all.", "BEWARE THE WEREMADILLO!!", "I like to eat paste, so bland and filling, yummmm!", "I don't have time to chit chat.", "... And that's why I'm investing all my money in yams."] 

class randomnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = random.choice(descriptions)
		self.db.msg = random.choice(phrases)
		self.locks.add("get:false()")
		self.db.get_err_msg = "Kidnapping is a crime."

class factionnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("faction", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.msgnone = ""
		self.db.msgfed = ""
		self.db.msgcartel = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "Kidnapping is a crime."

class cartelnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("cartel", category="talkative")
		self.db.desc = "A hardened criminal."
		self.db.msgnone = ""
		self.db.msgvipers = ""
		self.db.msgreapers = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "What? You wanna hold my pocket or something?"

class multinpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("multi", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.msg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "Kidnapping is a crime."

class tagnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("tagnpc", category="talkative")
		self.db.desc = ""
		self.db.taggedresp = ""
		self.db.untaggedresp = ""
		self.db.tag = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "Back off pal!!"

class addtagnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("addtagnpc", category="talkative")
		self.db.desc = ""
		self.db.msg = ""
		self.db.addtag = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "Back off pal!!"

class evmnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("evm", category="talkative")
		self.db.desc = "Just a normal person."
		self.locks.add("get:false()")
		self.db.get_err_msg = "Kidnapping is a crime."