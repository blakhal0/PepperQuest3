from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class work(default_cmds.MuxCommand):
	key = "Work"
	aliases = ["work"]
	auto_help = True
	def func(self):
		answer = yield("|/What project would you like to work on:|/Bird House|/Bind a Book|/Fast Food Uniform|/Dentures|/Coffee Cup")
		if answer in ["bird house", "bird", "house"]:
			self.caller.msg("|/Stacks of pre-cut wooden parts are stacked in front of you.")
			self.caller.msg("You begin assembling the small bird houses.")
			self.caller.msg("Soon the glue has your hands covered in wood dust and sticking together.")
			self.caller.msg("You're starting to feel sick, you read the glue package 'Extremely toxic, avoid skin contact at all costs!!'")
			self.caller.msg("A feeble attempt to beg for help stumbles out of your mouth as you hit the ground.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
		elif answer in ["bind a book", "bind", "book"]:
			self.caller.msg("|/Piles of folded pages and book bindings are stacked on the workstation.")
			self.caller.msg("You start stacking up the multiple groups of pages and start binding them together with a large heavy needle.")
			self.caller.msg("The work gets harder and harder as the needle dulls, you toss the used needle in the trash and grab a fresh one.")
			self.caller.msg("After what seems like an eternity you have completed one book 'Is your child a Spice Head? A Guide to Enhanced Interrogation Tactics You Can do at Home'.")
			return
		elif answer in ["fast food uniform", "uniform", "fast food", "food uniform"]:
			self.caller.msg("|/An embroidery machine is setup on your workstation.")
			self.caller.msg("You carefully align the work uniform and begin embroidering a large golden M on the front.")
			yield 5
			self.caller.msg("The box of blank uniforms seems endless, but after several hours of vigorous work, you complete the box.")
			return
		elif answer in ["dentures", "teeth"]:
			if not self.caller.tags.get("shoplifting") or self.caller.tags.get("handle"):
				self.caller.msg("|/You turn on the heater and get the water boiling.")
				self.caller.msg("After a minute or two you pour in the plastic beads, wait for them to soften, and pull them out.")
				yield 5
				self.caller.msg("Pressing the plastic into the mold, you realize that this stuff could be used to make about anything you need.")
				self.caller.msg("After a long while of color matching pigments and shaping individual teeth, you're done with one set of dentures.")
				return
			else:
				handle_proto = {
				"key": "Handle",
				"typeclass": "typeclasses.objects.DefaultObject",
				"desc": "A molded plastic handle.",
				"location": self.caller
				}
				spawn(handle_proto)
				self.caller.msg("|/You turn on the heater and get the water boiling.")
				self.caller.msg("After a minute or two you pour in the plastic beads, wait for them to soften, and pull them out.")
				self.caller.msg("You quickly roll it into a makeshift handle and slip it into your pocket.")
				self.caller.tags.add("handle")
				return
		elif answer in ["coffee cup", "coffee", "cup"]:
			self.caller.msg("|/A stack of paper and plastic cups is set on your workstation.")
			self.caller.msg("One by one, you load them into a printer that puts a mermaid looking green logo onto them.")
			yield 5
			self.caller.msg("After several hours you finish your stack of cups.")
			return
		else:
			self.caller.msg("|/|mGuard|n says: There's a list right in front of you, can't you read?")
			return

class WorkCmdSet(CmdSet):
	key = "WorkCmdSet"
	def at_cmdset_creation(self):
		self.add(work())

class workstation(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A workstation where you can |cWork|n on projects. Might as well do something to pass the ample amount of time right?"
		self.cmdset.add_default(WorkCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialobj")
		self.db.get_err_msg = "|/The workstation is firmly bolted to the ground."