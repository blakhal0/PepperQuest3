from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class repair(default_cmds.MuxCommand):
	key = "Fix Pepperbot"
	aliases = ["fix pepperbot", "Fix pepperbot", "fix Pepperbot"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("finalend"):
			self.caller.msg("|/Pepperbot is already fixed.")
			return
		if not self.caller.tags.get("botrepair"):
			self.caller.msg("Vivian is working on Pepperbot, if you mess with it while she's gone you're going to be in trouble!!")
			return
		status = "not fixed"
		pepperbotstatus = "none"
		stress = 0
		while not status == "fixed":
			if stress > 3:
				self.caller.msg("|/You cry out in frustration and toss your tools down.|/You've gotten too stressed and walk away from working on the bot.")
				break
			self.caller.msg("|/Pepperbot is faulting, try to fix it.")
			answer = yield("What do you want to try?|/Kick it.|/Hit it.|/Hit it harder.|/Swear at it.|/Praise the bot.|/Give up.")
			if answer.lower() == "hit it":
				self.caller.msg("|/You hit Pepperbot, it chips an electronic noise.")
				self.caller.msg("You've made Pepperbot sad.")
				pepperbotstatus = "sad"
				stress += 1
				yield 2
				continue
			elif answer.lower() == "kick it":
				self.caller.msg("|/You kick Pepperbot, it chips an electronic noise.")
				self.caller.msg("You've made Pepperbot sad.")
				pepperbotstatus = "sad"
				stress += 1
				yield 2
				continue
			elif answer.lower() == "give up":
				self.caller.msg("|/You admit defeat and give up.")
				break
			elif answer.lower() == "hit it harder":
				if pepperbotstatus == "sad" or pepperbotstatus == "none":
					self.caller.msg("|/Grumbling you give Pepperbot a tremendous whack.")
					self.caller.msg("*sad bot noises*")
					pepperbotstatus = "sad"
					stress += 2
				if pepperbotstatus == "happy":
					status = "fixed"
					self.caller.msg("|/|m%s|n says: Come on buddy, I believe in you, you can do this!!" % (self.caller.key))
					self.caller.msg("You give the bot a reassuring fender rub.")
					self.caller.msg("You give Pepperbot a giant whack, you hear a small click and the bot whirs to life.")
					self.caller.msg("You fixed the bot!!!")
					self.caller.tags.add("finalend")
				yield 2
				continue
			elif answer.lower() == "swear at it":
				self.caller.msg("|/You dirty rotten good for nothing useless pile of silicon!!!")
				self.caller.msg("Pepperbot isn't fixed, but you feel a lot better.")
				if stress > 0:
					stress -=1
				yield 2
				continue
			elif answer.lower() == "praise the bot":
				self.caller.msg("|/|m%s|n says: Look, I know it's hard being a bot, but together we can do this!! You're a good bot!" % (self.caller.key))
				self.caller.msg("*happy bot noises*")
				pepperbotstatus = "happy"
				yield 2
				continue
			else:
				self.caller.msg("|/That's not an approved method for fixing malfunctioning robots.")
				yield 2
				continue
		if status == "fixed":
			self.caller.msg("|/Pepperbot is back up and running, great work!!")
			return
		return

class PepperbotCmdSet(CmdSet):
	key = "PepperbotCmdSet"
	def at_cmdset_creation(self):
		self.add(repair())

class pepperbot(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An orange robot made from an old electric wheelchair."
		self.cmdset.add_default(PepperbotCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "Pepperbot makes a whining noise."