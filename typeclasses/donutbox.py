from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class moveboxes(default_cmds.MuxCommand):
	key = "Move Boxes"
	aliases = ["Move Boxes", "Move boxes", "move Boxes", "move boxes"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You give the stack of boxes a nudge with your foot.")
		self.caller.msg("A large, nasty looking spider jumps out from behind the boxes.")
		self.caller.msg("|mGuard|n shrieks: SPIDER!!! EEEEEEEEEK")
		self.caller.msg("The guards respond by instinct and are in full riot gear in a flash.")
		self.caller.msg("|mGuard|n says: STOP RESISTING!!! AAAHHHH, IT'S COMING RIGHT FOR ME!! SELF DEFENSE!!! SELF DEFENSE!!!!")
		self.caller.msg("The guards deploy all available methods of force on the poor spider.")
		self.caller.msg("The guards are distracted, now is your chance, it won't last long.")
		self.caller.tags.add("gdistract")
		yield 10
		if not self.caller.tags.get("gdistract"):
			return
		self.caller.msg("|/|mGuard|n says: IT'S GOT A KNIFE!!!")
		yield 7
		if not self.caller.tags.get("gdistract"):
			return
		self.caller.msg("|/|mGuard|n says: HOW DID IT GET YOUR TASE... KAZERRRRRRT-tat-tat-tat-tat-tat.")
		self.caller.msg("|mGuard|n says: OFFICER DOWN!!")
		yield 7
		if not self.caller.tags.get("gdistract"):
			return
		self.caller.msg("|/The guards are gaining the upper hand.")
		yield 5
		if not self.caller.tags.get("gdistract"):
			return
		if self.caller.tags.get("gdistract"):
			self.caller.tags.remove("gdistract")
			self.caller.msg("|/The guards have subdued the spider.")
			self.caller.msg("|mGuard|n says: You guys uhhh, you think we should plant some crack on it so the charges stick?")
			self.caller.msg("The guards are no longer distracted.")
			if self.caller.tags.get("holdskey"):
				self.caller.tags.remove("holdskey")
				self.caller.msg("|/|mGuard|n shouts: DROP THAT KEY RIGHT NOW SCUMBAG!!!")
				self.caller.msg("The guards dog pile on you and beat the hell out of you.")
				for o in self.caller.contents:
					if o.key == "Soap":
						o.delete()
				self.caller.msg("The guards find the soap and confiscate it.")
				results = search_object("#436")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			return
		return

class DonutBoxCmdSet(CmdSet):
	key = "DonutBoxCmdSet"
	def at_cmdset_creation(self):
		self.add(moveboxes())

class donutbox(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A floor to ceiling stack of old donut boxes."
		self.cmdset.add_default(DonutBoxCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "This may actually be a load bearing structure, maybe just |cMove Boxes|n."