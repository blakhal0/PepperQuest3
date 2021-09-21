from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class microwavecmd(default_cmds.MuxCommand):
	"""
	Use Microwave.

	Usage:
	Use Microwave

	Use the microwave to heat something up.
	"""
	key = "Use Microwave"
	alias = ["use microwave", "microwave"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You press the door button, the door slowly swings open with a groan.|/You look around at the shelves and see some options for microwaving.")
		answer = yield("|/What would you like to microwave?|/Burrito|/Hot Dog|/Sandwich|/Can of Hairspray|/Kitten")
		if answer.lower() in ["burrito"]:
			self.caller.msg("|/'Yummmmm, burritos' you grab an El Bomba burrito from the freezer and toss it in the microwave.")
			yield 3
			self.caller.msg("The microwave dings, you snatch up the burrito and take a bite.|/Odd, you can't taste anything.")
			yield 3
			self.caller.msg("'Where's all this smoke coming from' your jaw liquefies and splatters on the floor, you're eating literal lava.")
			self.caller.msg("Agony wracks your body as you burn from the inside out like a luau pig.|/|rYOU ARE DEAD|n")
			results = search_object("#33")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif answer.lower() in ["hot dog", "hotdog"]:
			self.caller.msg("|/'Ahh the mighty hot dog, mystery meat in the fun and convenient shape of a tube.' You toss a hot dog in the microwave and turn it on.")
			yield 3
			self.caller.msg("The microwave dings, you put the hot dog in the bun, pile on the toppings to perfection and take a bite...")
			yield 4
			self.caller.msg("'THAT is a tasty hot dog.' You scarf the rest down as you suddenly realize you have no money to pay for it.|/No evidence, no crime. Perfectly executed.")
			return
		elif answer.lower() in ["sandwich"]:
			self.caller.msg("|/*grumble grumble* 'Oh man, am I hungry'. A chicken and cheese sandwich catches your eye in the cooler.")
			yield 4
			self.caller.msg("In a spinning move you snag the sandwich out of the cooler, chuck it in the microwave, close the door and press start.")
			yield 4
			self.caller.msg("The microwave dings, 'Hummm, this sandwich looks a little dry, maybe some mayo..' you press down on the self serve mayo and chomp down.")
			yield 5
			self.caller.msg("You reflect back on your life from the hospital bed, your friends and family around you, in a rattle you speak your last words 'never trust corner store mayo...'")
			self.caller.msg("|/|/|rYOU ARE DEAD|n")
			results = search_object("#33")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
			return
		elif answer.lower() in ["can of hairspray", "hairspray"]:
			self.caller.msg("|/You pick up a big metal can of aquanet from the shelf.|/Glancing quickly at the back you don't see anything that specifically says 'Do Not Microwave', must be safe.")
			yield 4
			self.caller.msg("The can rattles a bit as you toss it in the microwave and close the door...")
			yield 3
			self.caller.msg("You press the start button...")
			yield 2
			self.caller.msg("   ..-^~~~^-..")
			self.caller.msg(" .~           ~.")
			self.caller.msg("(;:           :;)")
			self.caller.msg(" (:           :)")
			self.caller.msg("  ':._   _.:'")
			self.caller.msg("      | |")
			self.caller.msg("    (=====)")
			self.caller.msg("      | |")
			self.caller.msg("      | |")
			self.caller.msg("   ((/   \))")
			self.caller.msg("|r|/|/YOU ARE DEAD|n")
			results = search_object("#33")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif answer.lower() in ["kitten"]:
			self.caller.msg("|/'Oh wow, a cute little fluffy kitten, how odd that they have these in stock' you think to yourself as you pick it up.")
			yield 4
			self.caller.msg("The kitten meows and purrs as you pet it.")
			yield 3
			self.caller.msg("The adorable little kitten paws and meows at the door as it closes, it's little toe beans pressing against the glass.")
			yield 5
			self.caller.msg("'3 minutes should do the trick right?' contemplation crosses your mind as you look at the adorable kitten.|/Maybe you're making the wrong decision here, you begin to rethink your choices.")
			yield 9
			self.caller.msg("'Yeah, better make it 4 minutes!'")
			self.caller.msg("'Four-Zero-Zero aaaaaaand start.'")
			yield 6
			self.caller.msg("An ear piercing scream drowns out all else as a super-powered mutant electric tiger hulks out of the microwave, swings a massive murder mitten of razor sharp claws, and disembowels you where you stand.")
			self.caller.msg("Scrambling to put your guts back in, the world begins to go grey as you hear your bones snapping in the giant beasts jaws.")
			yield 5
			self.caller.msg("|/You didn't seriously think I was going to let you microwave a cat and get away with it did you? You sick bastard.|/|/|rYOU ARE DEAD|n")
			results = search_object("#33")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("You deside that microwave food isn't in your diet for today.")
			return
class MicrowaveCmdSet(CmdSet):
	key = "MicrowaveCmdSet"
	def at_cmdset_creation(self):
		self.add(microwavecmd())

class microwave(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An offbrand microwave sits on the counter next to the soda fountain.|/Years of splattered burrito fillings line the inside."
		self.cmdset.add_default(MicrowaveCmdSet, permanent=True)
		self.locks.add("get:false()")