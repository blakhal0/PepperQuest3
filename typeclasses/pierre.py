from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn
from random import randint

class chat(default_cmds.MuxCommand):
	key = "talk pierre"
	aliases = ["Talk Pierre", "Talk pierre", "talk Pierre"]
	auto_help = True
	def func(self):
		if self.caller.db.cartel == "vipers" or self.caller.tags.get("rumbledone"):
			self.caller.msg("There is no one here by that name to talk to.")
			return
		elif not self.caller.tags.get("rumble"):
			self.caller.msg("|/|mPierre|n says: Go away tiny person, you bother me like a fly.")
			self.caller.msg("|/|mPierre|n says: Not like a pretty butterfly, but the nasty biting kind that I swat!")
			self.caller.msg("Pierre goes back to lifting massive stacks of weights.")
			return
		else:
			self.caller.msg("|/Nataly has to be out of her damn mind sending you out here without a heavily armed force to try and get the debt book back from Pierre Montagne.")
			self.caller.msg("Pierre is busy stacking weights on a metal bar that appears to be about to snap under the stress and does not notice you approaching.")
			self.caller.msg("You've got the drop on him, but you can't imagine this ending well for you.")
			answer = yield("What do you want to do? Attack, Run Away, Ask Pierre Nicely.")
			for o in self.caller.contents:
				if o.key == "Butterfly":
					o.delete()
					self.caller.msg("|/As you grab the brass knuckles from your waist band, the butterfly you caught escapes and flutters through the air.")
					self.caller.msg("|mPierre|n says: Oh, a lovely papillion!!! I do love how they float and flutter in the sky.")
					self.caller.msg("Pierre takes off skipping through the yard and in his haste to chase the butterfly drops the book you're after.")
					self.caller.msg("You calmly walk over and pick up the book tossing the brass knuckles away casually.")
					self.caller.msg("That worked out quite nicely.")
					book_proto = {
					"key": "Debt Book",
					"typeclass": "typeclasses.objects.book",
					"story": "Huh, looks like a bunch of jibberish.|/hAT BASHs Debt Book:|/Qlorvg Qzpv 345|/Vodllw Yofvh 124|/Tfziw Qlmvh 200|/Hzizs Xlmmli 87",
					"desc": "A coded bookies ledger.",
					"location": self.caller
					}
					spawn(book_proto)
					for o in self.caller.contents:
						if o.key == "Brass Knuckles":
							o.delete()
					self.caller.tags.remove("rumble")
					self.caller.tags.add("rumbledone")
					return
			if answer.lower() in ["attack"]:
				luck = randint(1, 4)
				if luck in [2, 4]:
					self.caller.msg("|/It appears luck is on your side today.")
					self.caller.msg("You casually walk up to Pierre and with a swift movement you slam your brass knuckled fist into his throat.")
					self.caller.msg("Pierre sputters and grabs you by the head preparing to crush your skull.")
					self.caller.msg("|m%s|n says: Look, we're in a real delicate situation here, your throat is swelling up as we speak." % (self.caller.key))
					self.caller.msg("|m%s|n says: So how about you give me that debt book, I let you get to the infirmary before you pass out and start choking to death." % (self.caller.key))
					self.caller.msg("Pierre quickly nods in agreement, reaches inside his shirt and hands you the debt book.")
					book_proto = {
					"key": "Debt Book",
					"typeclass": "typeclasses.objects.book",
					"desc": "A coded bookies ledger.",
					"story": "Huh, looks like a bunch of jibberish.|/hAT BASHs Debt Book:|/Qlorvg Qzpv 345|/Vodllw Yofvh 124|/Tfziw Qlmvh 200|/Hzizs Xlmmli 87",
					"location": self.caller
					}
					spawn(book_proto)
					for o in self.caller.contents:
						if o.key == "Shank":
							o.delete()
					self.caller.msg("You drop the brass knuckles and casually walk away. You get the feeling you'd best make good time getting back to Nataly.")
					self.caller.tags.remove("rumble")
					self.caller.tags.add("rumbledone")
					return
				else:
					self.caller.msg("|/You begin to approach Pierre. It appears luck is not on your side today.")
					self.caller.msg("Pierre suddenly turns, looks, and sees the brass knuckles in your hand. His face darkens with fury and you're staring up into the eyes of a living volcano, ready to erupt.")
					self.caller.msg("Pierre grabs you by the head and crushes your skull.")
					self.caller.msg("|/|rYou are dead.|n")
					results = search_object("#292")
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
			elif answer.lower() in ["run away", "run", "away"]:
				self.caller.msg("|/You spineless, lily livered, bawk-bagawk coward.")
				self.caller.msg("You run away crying and don't stop until you're hiding under the blankets in your cell.")
				results = search_object("#292")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			elif answer.lower() in ["ask pierre nicely", "ask", "ask nicely"]:
				luck = randint(1, 4)
				if luck in [1, 3]:
					self.caller.msg("|/You put the brass knuckles back in your waist band, stand up straight, and approach Pierre, clearing your throat.")
					self.caller.msg("|m%s|n says: Hello Pierre, look, this is a bit awkward, but I've been asked to get a certain book you have, umm, acquired." % (self.caller.key))
					self.caller.msg("|m%s|n says: Now, I'm not calling you a thief by any means, but it doesn't belong to you and I would very much appreciate it if you would give it to me." % (self.caller.key))
					self.caller.msg("|m%s|n says: What would your mother tell you to do?" % (self.caller.key))
					self.caller.msg("Pierre sputters and gets a bit misty eyed.")
					self.caller.msg("|mPierre|n says: She w-w-w-would say it's not nice to take things from people just because I'm bigger than they are.")
					self.caller.msg("|mPierre|n says: It's not a very good book anyways, I can't even read it. Here, you can have it.")
					self.caller.msg("You tell Pierre thank you as he hands you the book and then squeek a bit as he squeezes you in a bear hug and the brass knuckles drop out of your waist band.")
					self.caller.msg("Best to just consider the brass knuckles gone forever.")
					book_proto = {
					"key": "Debt Book",
					"typeclass": "typeclasses.objects.book",
					"desc": "A coded bookies ledger.",
					"story": "Huh, looks like a bunch of jibberish.|/hAT BASHs Debt Book:|/Qlorvg Qzpv 345|/Vodllw Yofvh 124|/Tfziw Qlmvh 200|/Hzizs Xlmmli 87",
					"location": self.caller
					}
					spawn(book_proto)
					for o in self.caller.contents:
						if o.key == "Brass Knuckles":
							o.delete()
					self.caller.tags.remove("rumble")
					self.caller.tags.add("rumbledone")
					return
				else:
					self.caller.msg("|/You put the brass knuckles back in your waist band, stand up straight, and approach Pierre, clearing your throat.")
					self.caller.msg("|m%s|n says: Hello Pierre, look, this is a bit awkward, but I've been asked to get a certain book you have, umm, acquired." % (self.caller.key))
					self.caller.msg("|m%s|n says: Now, I'm not calling you a thief by any means, but it doesn't belong to you and I would very much appreciate it if you would give it to me." % (self.caller.key))
					self.caller.msg("|m%s|n says: What would your mother tell you to do?" % (self.caller.key))
					self.caller.msg("|mPierre|n says: Well, why don't you ask her, she's right over here. 'Hey mama, this twerp wants to ask you a question.'")
					self.caller.msg("Pierre and his mama proceed to beat the living crap out of you until the guards start to fire tear gas and bean bags to quell the fight.")
					results = search_object("#436")
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
			else:
				self.caller.msg("|/You stutter step a bit, but can't quite build up the courage to make a decision...")
				return

class PierreCmdSet(CmdSet):
	key = "PierreCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class pierre(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/Pierre Montagne is an absolute hulk. His muscles have muscles.|/Pierre casually lifts up two other inmates and begins using them to do curls."
		self.cmdset.add_default(PierreCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(rumbledone) and not attr(cartel, vipers)")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "Pierre giggles.|/|mPierre|n says: Stop, HAHAHAHAHA, stop that. It tickles."