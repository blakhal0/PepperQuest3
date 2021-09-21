from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject

class talkingMike(default_cmds.MuxCommand):
	key = "Talk Mike"
	aliases = ["talk Mike", "talk mike", "talk Mike"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("wdc"):
			self.caller.msg("|/|mMike|n says: No need to rush, enjoy the food, it is the absolute least I can do and I imagine it's been a long time since you've had a meal that good.")
			self.caller.msg("|mMike|n says: When you're ready, transportation will be waiting outside, with new documentation for you.")
			return
		self.caller.msg("|/|mMike|n says: Hey, %s, glad you got here safe and sound." % (self.caller.key))
		self.caller.msg("|mMike|n says: They call me the Moose, Mikey Moose. I'm the head of an international spice cartel I work hard every day and I sleep well at night.")
		self.caller.msg("|m%s|n says: ... How did you know who I am?" % (self.caller.key))
		self.caller.msg("|mThe Moose|n says: Easy, FMB is just an empty building we lease.")
		self.caller.msg("Mike points over the bar towards the floor to a screen with feeds from several security cameras.")
		self.caller.msg("|mThe Moose|n says: If someone goes there, then here, we know they're new and looking for me.")
		self.caller.msg("|mThe Moose|n says: Just because spice is legal here doesn't mean being an international criminal is.")
		self.caller.msg("|mThe Moose|n says: Aye, Tommy, %s just escaped a maximum security prison and was smuggled into a foreign country, I imagine that builds a hell of an appetite." % (self.caller.key))
		self.caller.msg("|mThe Moose|n says: Pop over to Boustan's and pick up some proper spicy shawarma and a side of poutine from the underground spot would ya, bit of northern hospitality.")
		self.caller.msg("|mTommy|n says: You got it boss.")
		self.caller.msg("Tommy grabs some cash out of the till and steps to.")
		self.caller.msg("|mThe Moose|n says: Now that we've got some privacy, I understand you've got a bit of information for me.")
		for o in self.caller.contents:
			if o.key == "Secret Info":
				o.delete
		self.caller.msg("You hand the info to The Moose who takes out a small UV light and holds it over the paper, hidden words begin to glow.")
		self.caller.msg("|mThe Moose|n says: Those dirty rat bastards.")
		self.caller.msg("The Moose lights the paper on fire and stamps out the ashes.|/Tommy returns and sets down the most amazing smelling food in front of you.")
		self.caller.msg("|mThe Moose|n says: I've got a hard thing to ask, but you're the only one that can do it.")
		self.caller.msg("|mThe Moose|n says: I need you to go to Washington DC and smoke out the rat that's working with the NSA.")
		self.caller.msg("|mThe Moose|n says: I'll have transportation waiting outside by the time you're done eating, with new ID and passport.")
		self.caller.msg("|mThe Moose|n says: Your service is greatly appreciated, I'm sure you won't fail.")
		self.caller.tags.add("wdc")
		return

class MikeCmdSet(CmdSet):
	key = "MikeCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingMike())

class mikemoose(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Mike is sitting at the rounded corner of the bar, snacking on spicy peanuts, enjoying a drink."
		self.cmdset.add_default(MikeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "The bartender leaps the bar and has your face smashed on the well worn bartop with you in an armbar in the blink of an eye.|/|mMike|n says: No need to get excited Tommy, they're new, and my guest. Welcome to Grumpy's."