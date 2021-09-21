from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk jules"
	aliases = ["Talk Jules", "Talk jules", "talk Jules"]
	auto_help = True
	def func(self):
		if self.caller.db.cartel == "reapers":
			self.caller.msg("|/|mJules|n says: How have you been neighbor. It's good to see you again.")
			return
		if self.caller.search("Key Impression", location=self.caller, quiet=True):
			self.caller.msg("|/|mJules|n says: I love it when a plan comes together.")
			self.caller.msg("|mJules|n says: Now, lets make us a key shall we.")
			self.caller.msg("|mJules|n says: Looks like a we got a Sargent key with 4-1-6-3-8 as the cuts.")
			self.caller.msg("Jules pulls out a bag from inside his mattress and sets to work.")
			self.caller.msg("|mJules|n says: That should do it, one Maintenance Key for you.")
			guardkey_proto = {
			"key": "Maintenance Key",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A copy of the Maintenance Key.",
			"location": self.caller
			}
			spawn(guardkey_proto)
			for o in self.caller.contents:
				if o.key == "Key Impression":
					o.delete()
			self.caller.msg("|mJules|n says: You've proven yourself valuable to the family. Welcome to the Faucheurs Fantomes, the Ghost Reapers.")
			self.caller.db.cartel = "reapers"
			self.caller.db.faction = "cartel"
			self.caller.tags.remove("reaperinvite")
			self.caller.tags.remove("keymaker")
			self.caller.tags.add("jules")
			self.caller.msg("|mJules|n says: Go talk to Fahad in 4B. He's been working on a plan to get some money, well stamps, ya know, prison money.")
			return
		if self.caller.tags.get("keymaker"):
			self.caller.msg("|/|mJules|n says: Now, you can't just go stealing the key, you'll need to make an impression of it in a bar of soap.")
			self.caller.msg("|mJules|n says: If you haven't met Red yet, he's a neutral party in cell 8B, he's a man that knows how to get things.")
			self.caller.msg("|mJules|n says: Normally he'd charge, ain't nothing free in this life but death, but I'll send word to hook you up at no charge.")
			self.caller.msg("|mJules|n says: Now, the key we need is in the Guard Room in the center of the first floor. So you're gonna be walking right into the lions den here.")
			self.caller.msg("|mJules|n says: You're probably not going to have long to get it done, remember you need to |cGet Key|n |cMake Impression|n and |cReturn Key|n so be ready when the opportunity presents itself.")
			self.caller.msg("|mJules|n says: Bring the impression back here when you're done.")
			self.caller.msg("|mJules|n says: Here, throw this cleaning crew outfit on, talk to the guard on the west side of the guard room, Bronson cracked their skull a few years ago and they ain't been right since.")
			self.caller.msg("|mJules|n says: Good luck, try to not fuck it up.")
			self.caller.msg("You throw on the uniform, it doesn't look much different from your normal outfit.")
			return
		self.caller.msg("|/|mJules|n says: Hey neighbor, welcome.")
		self.caller.msg("|mJules|n says: Since you're here, I'm going to take it that you're interested in joining our crew.")
		self.caller.msg("|m%s|n says: I think you mean cartel, don't you?" % (self.caller.key))
		self.caller.msg("|mJules|n says: That's one word for it, we prefer family. Better optics, but let's not bullshit each other, it is what it is.")
		self.caller.msg("|mJules|n says: A great defiance of the spice prohibition and all those who stand for it. And we make money doing it, a lot of money.")
		self.caller.msg("|mJules|n says: We're the dominant force on the streets, we're the dominant force in this prison, we operate the spiceeasy's and we supply most of the country with peppers.")
		self.caller.msg("|mJules|n says: Now, you're in here because you got caught with some of our product that you helped procure. So we owe you a bit of a debt.")
		self.caller.msg("|mJules|n says: But, we are a family and we don't just let strangers join us.")
		self.caller.msg("|mJules|n says: I hate to do this, but you're going to have to perform a minor task for us to prove loyalty.")
		self.caller.msg("|mJules|n says: You'll find, to no surprise I'm sure, that in this prison there's a door with a lock on it.")
		self.caller.msg("|mJules|n says: Also, there's a key in the guard room marked with an M. We need a copy of that key.")
		self.caller.msg("|mJules|n says: So, what do you say? Up for a little mission impossible shit?")
		answer = yield("Take on the mission and join the Ghost Reapers? Yes or No")
		if answer.lower() in ["yes", "y"]:
			self.caller.tags.add("keymaker")
			if self.caller.tags.get("interview"):
				self.caller.tags.remove("interview")
			self.caller.msg("|/|mJules|n says: Now, you can't just go stealing the key, you'll need to make an impression of it in a bar of soap.")
			self.caller.msg("|mJules|n says: If you haven't met Red yet, he's a neutral party in cell 8B, he's a man that knows how to get things.")
			self.caller.msg("|mJules|n says: Normally he'd charge, ain't nothing free in this life but death, but I'll send word to hook you up at no charge.")
			self.caller.msg("|mJules|n says: It takes a second to get a decent impression of a key. You'll need to |cGet Key|n |cMake Impression|n and |cReturn Key|n.")
			self.caller.msg("|mJules|n says: You're probably not going to have long to get it done, so be ready if the opportunity presents itself.")
			self.caller.msg("|mJules|n says: You're walking right into the lions den here, don't act like a fool in there.")
			self.caller.msg("|mJules|n says: Bring it back here when you're done.")
			self.caller.msg("|mJules|n says: Good luck, try to not get your skull cracked open.")
		elif answer.lower() in ["no", "n"]:
			self.caller.msg("|/|mJules|n says: No, skin off my back. If you change your mind, come talk to me again.")
			self.caller.msg("|mJules|n says: Keep your mind clear and your vibes groovy.")
			return
		else:
			self.caller.msg("|/|mJules|n says: There are many words of wisdom in this world, what you just said, that wasn't any of them.")
			return
		return

class JulesCmdSet(CmdSet):
	key = "JulesCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class jules(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Jules is sitting in a meditative pose, softly humming."
		self.cmdset.add_default(JulesCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mJules|n says: You lay hands on me, IN MY HOUSE??!!"