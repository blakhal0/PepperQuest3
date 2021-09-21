from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chow(default_cmds.MuxCommand):
	key = "Eat Chow"
	aliases = ["Eat chow", "eat chow", "eat Chow"]
	auto_help = True
	def func(self):
		if self.caller.db.cartel == "vipers":
			self.caller.msg("|/The line is long and moves slowly, shuffling forward two steps at a time.")
			yield 5
			self.caller.msg("Finally, you reach the serving line.")
			yield 5
			self.caller.msg("|mInmate|n says: Hey, new blood, you're with us, you get the good stuff now.")
			self.caller.msg("The inmate takes your tray back into the kitchen and comes back out with some tacos and an ice cream dish.")
			self.caller.msg("|mInmate|n says: Don't worry, you're with us, no one is gonna mess with you.")
			self.caller.msg("You take a seat with the rest of the Naga Vipers and enjoy your delicious tacos.")
			return
		elif self.caller.db.faction == "fed":
			self.caller.msg("|/The line is long and moves slowly, shuffling forward two steps at a time.")
			yield 3
			self.caller.msg("|/Finally, you reach the serving line.")
			self.caller.msg("|/The servers plop down a ladle of steaming beans, mashed potatoes, unbuttered white bread, and a block of hot tofu.")
			self.caller.msg("You take a seat at a nearly empty table and force yourself to shovel down the bland tasteless food.")
			if self.caller.tags.get("gracedone"):
				return
			self.caller.msg("Gruesome Grace sits down across from you.")
			self.caller.msg("|mGruesome Grace|n says: It's very kind of you to bring me a second tray of food.")
			self.caller.msg("Gruesome Grace grabs your tray and shoves a heaping spoonful of mashed potatoes into her mouth.")
			self.caller.msg("You stare her down as she continues to eat, grinning while her lips smack open and closed.")
			self.caller.msg("|mGruesome Grace|n says: You got something to say about it?")
			answer = yield("Start a fight or just keep quiet?")
			if answer.lower() in ["start a fight", "start fight", "fight"]:
				self.caller.tags.add("gracedone")
				self.caller.msg("|/|m%s|n says: Yeah, I got something to say you ugly slob." % (self.caller.key))
				self.caller.msg("You grab the tray of food and dump what's left on her head.")
				self.caller.msg("|m%s|n says: I'm not sure if this makes you look better, or the food worse." % (self.caller.key))
				self.caller.msg("Gruesome Grace stands up roaring and jumps over the table putting you into a headlock.")
				self.caller.msg("A brief struggle ensues, you manage to land a few punches, which ends with you on the receiving end of a particularly vicious noogie.")
				self.caller.msg("The guards come storming in just as you're starting to lose consciousness.|/|mGuard|n says: Inmate Grace, you're racking up quite a few frequent flier miles in solitary. Get this other inmate to the infirmary, sweet boogly moogly, that's one hell of a noogie.")
				results = search_object("#436")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			elif answer.lower() in ["stay quiet", "keep quiet", "quiet"]:
				self.caller.msg("|/You bite your tongue, hang your head in shame and sit there silently.")
				self.caller.msg("|mGruesome Grace|n says: Yeah, that's what I thought. From now on, you bring me a tray of food EVERY time you eat.")
				self.caller.msg("|mGruesome Grace|n says: Get outta my face you little wimp.")
				return
			else:
				self.caller.msg("|/|mGruesome Grace|n says: Yeah, just mumble to yourself, you little wimp.|/You didn't choose an available option. Try |cEat Chow|n again.")
				return
		elif self.caller.db.cartel == "reapers":
			self.caller.msg("|/The line is long and moves slowly, shuffling forward two steps at a time.")
			yield 5
			self.caller.msg("Finally, you reach the serving line.")
			yield 5
			self.caller.msg("The Naga Vipers run the chow line and the kitchen, and they're not a fan of you.")
			self.caller.msg("The servers plop down a ladle of steaming beans, mashed potatoes, unbuttered white bread, and a block of hot tofu.")
			self.caller.msg("You take a seat at a nearly empty table and look at your food, they didn't even bother to try and hide the spit and dead roaches they put in your food.")
			self.caller.msg("Chuckling works its way through the air from the chow line, you take your tray and dump it in the trash.")
			return
		else:
			self.caller.msg("|/The line is long and moves slowly, shuffling forward two steps at a time.")
			yield 5
			self.caller.msg("Finally, you reach the serving line.")
			yield 5
			self.caller.msg("The servers plop down a ladle of steaming beans, mashed potatoes, unbuttered white bread, and a block of hot tofu.")
			self.caller.msg("You take a seat at a nearly empty table and force yourself to shovel down the bland tasteless food.")
			return

class ChowCmdSet(CmdSet):
	key = "ChowCmdSet"
	def at_cmdset_creation(self):
		self.add(chow())
	
class chowline(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/A line of people are waiting to get their meal. A boring bland, but at least warm, meal.|/You can join them if you want to |cEat Chow|n."
		self.cmdset.add_default(ChowCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialobj")
		self.db.get_err_msg = "You can't take an entire line of people."