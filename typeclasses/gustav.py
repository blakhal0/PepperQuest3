from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk gustav"
	aliases = ["Talk Gustav", "Talk gustav", "talk Gustav"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("reaperinvite"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
		if self.caller.db.faction == "fed":
			self.caller.msg("There's no one here by that name to talk to.")
			return
		if self.caller.db.cartel == "vipers":
			self.caller.msg("There's no one here by that name to talk to.")
			return
		if self.caller.db.cartel == "reapers" or self.caller.db.faction == "cartel":
			self.caller.msg("Stay strong friend.")
			return
		if self.caller.tags.get("interview"):
			self.caller.msg("|/|mGustav|n says: Hey kid, you don't want to go in there. Them the Feds in there.")
			self.caller.msg("|mGustav|n says: And as bad a place as you might be now, trust me, getting messed up with them will only make things worse.")
		self.caller.msg("|/|mGustav|n says: Look, this place is rough. No one's getting out of here, well, not through the front door anyways, and knowing that makes life cheap.")
		self.caller.msg("|mGustav|n says: We hear you got popped doing business with an associate of ours, Sugar. I know, he's not our favorite person either, but his count is always on and product is always secure.")
		self.caller.msg("|mGustav|n says: Now, we ain't trying to tell you how to live your life, but if you want to keep on living it your way, you need backup in here.")
		self.caller.msg("|mGustav|n says: We're extending an offer to join our crew, the Ghost Reapers. We know how to handle the heat, if you catch my drift.")
		self.caller.msg("|mGustav|n says: Think it over, no need to rush to a decision, if you're interested, come talk to Jules up in cell 3B.")
		self.caller.msg("|mGustav|n says: Watch your back, this place ain't for the weak or the unwary.")
		self.caller.msg("Gustav claps a hand on your shoulder and walks away.")
		self.caller.tags.add("reaperinvite")
		return

class ReaperCmdSet(CmdSet):
	key = "ReaperCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class gustav(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Gustav is leaning against the wall in the hallway corner, he looks at you and motions to come closer. He has a tattoo of a ghost carrying a reapers scythe on his neck."
		self.cmdset.add_default(ReaperCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(reaperinvite)")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mGustav|n says: It seems like we're getting off on the wrong foot here."