from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk rodney"
	aliases = ["Talk Rodney", "Talk rodney", "talk Rodney" ]
	auto_help = True
	def func(self):
		if not self.caller.search("NSA Badge", location=self.caller, quiet=True):
			self.caller.msg("|/|mRodney|n says: Sorry, only official agents can check out weapons. Please see the registration clerk to get your credentials.")
			return
		if self.caller.search("Stun Gun", location=self.caller, quiet=True):
			self.caller.msg("|/|mRodney|n says: I already gave you the only weapon we had on hand. Unless the other agents return their gear, I've got nothing to sign out to you.")
			return
		self.caller.msg("|/|mRodney|n says: Welcome Agent %s, I'm the requisitions officer, I've got all the arms and ammo you'll need." % (self.caller.key))
		self.caller.msg("|mRodney|n says: Let's see here, you're cleared for... *beep boop bip* all weapons, wow, you didn't even have to go through training, impressive. I'm sure that won't impact the civilians poorly in any way.")
		self.caller.msg("|mRodney|n says: And let's see what we have in inventory... *beep boop bip* Oh, oh that's too bad.")
		self.caller.msg("|mRodney|n says: Looks like no one has returned any of the weapons from the big raid a few weeks ago.")
		self.caller.msg("|m%s|n says: What the shit do you mean? This is the armory!! The NSA is stacked to the gills with weapons, I've seen them first hand." % (self.caller.key))
		self.caller.msg("|mRodney|n says: Yeah, take that attitude, that'll help. Look this isn't a magic room, it doesn't just restock on it's own.")
		self.caller.msg("|mRodney|n says: Oh wait, looks like we do have the Bone Zapper 2550, a less lethal grade stun gun.")
		answer = yield("|mRodney|n says: You want it or not?")
		if answer.lower() in ["yes", "y"]:
			self.caller.msg("|/|mRodney|n says: Okay, here you go, sign here that you're checking it out...perfect. Enjoy!")
			sgun_proto = {
			"key": "Stun Gun",
			"typeclass": "typeclasses.sgun.sgun",
			"location": self.caller,
			"desc": "Bone Zapper 2550"
			}
			spawn(sgun_proto)
			return
		if answer.lower() in ["no", "n"]:
			self.caller.msg("|/|mRodney|n says: Whatever, I'm not the one that's going to be out there getting attacked by spiced up lunatics. Good Luck.")
			return
		self.caller.msg("|/|mRodney|n says: What's that? I couldn't make out what you were saying with your lip pouting like that.")
		return

class RodneyCmdSet(CmdSet):
	key = "RodneyCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class rodney(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Rodney stands behind a metal grate, tapping keys on a keyboard and referencing paperwork."
		self.cmdset.add_default(RodneyCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mRodney|n says: I have access to ALL the weapons, think about that."