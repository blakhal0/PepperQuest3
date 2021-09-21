from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class work(default_cmds.MuxCommand):
	key = "break out"
	aliases = ["Break Out", "Break out", "break Out"]
	auto_help = False
	def func(self):
		if not self.caller.search("Secret Info", location=self.caller, quiet=True):
			self.caller.msg("|/|mJules|n says: Hey, before you go doing anything Lucien needs to talk to you. Real important.")
			return
		if self.caller.search("Debris", location=self.caller, quiet=True):
			self.caller.msg("|/You're holding as much debris as you can sneak into the yard with. Go to the yard and |cScatter Debris|n.")
			return
		if not self.caller.search("Hammer", location=self.caller, quiet=True):
			self.caller.msg("|/You don't have a hammer.")
			return
		if not self.caller.search("Poster", location=self.caller, quiet=True):
			self.caller.msg("|/You don't have a poster to hide the hole you're making.")
			return
		if self.caller.db.debris >= 5:
			self.caller.msg("|/The hole is now large enough to get into the elevator shaft. Now is your chance to |cEscape|n.")
			return
		if self.caller.db.debris == 2:
			self.caller.msg("|/The hole is getting bigger, but there's more work to be done.")
		if self.caller.db.debris == 3:
			self.caller.msg("|/The hole is getting bigger, you've managed to break through, you can feel the slight breeze coming through the hole.")
		if self.caller.db.debris == 4:
			self.caller.msg("|/The hole is nearly big enough to squeeze through! You're almost there.")
		self.caller.tags.add("working")
		self.caller.msg("|/Careful to not tear the edges, you remove the poster from the wall.")
		yield 2
		self.caller.msg("You begin the difficult job of quietly chipping away at the concrete wall in your cell.")
		yield 6
		self.caller.msg("It's slow going work.")
		debris_proto = {
		"key": "Debris",
		"typeclass": "typeclasses.objects.nodropobj",
		"desc": "Bits of concrete.",
		"location": self.caller
		}
		spawn(debris_proto)
		yield 4
		self.caller.msg("You've removed as much debris as you can hide in your pockets. Take it out to the yard and |cScatter Debris|n.")
		self.caller.msg("You put the poster back up to cover up your work.")
		self.caller.tags.remove("working")
		return

class escape(default_cmds.MuxCommand):
	key = "escape"
	aliases = ["Escape"]
	auto_help = False
	def func(self):
		if not self.caller.db.debris >= 5:
			self.caller.msg("|/The hole isn't big enough to escape through yet.")
			return
		for o in self.caller.contents:
			if o.key == "Shiv":
				o.delete()
			if o.key == "Hammer":
				o.delete()
			if o.key == "Poster":
				o.delete()
			if o.key == "Sticky Hand":
				o.delete
			if o.key == "Loaded Dice":
				o.delete()
			if o.key == "Prison Wallet":
				o.delete()
			if o.key == "Plastic":
				o.delete()
		self.caller.tags.remove("jules")
		self.caller.tags.remove("fahad")
		self.caller.tags.remove("lucien")
		self.caller.msg("|/You shimmy your way through the hole in the wall and into the elevator shaft.")
		self.caller.msg("The shaft is dark and full of cobwebs, but you manage to keep your footing and soon find yourself on top of the elevator car.")
		self.caller.msg("Fumbling about for a minute you find the latch and drop down in to the elevator car.")
		self.caller.msg("You press M and the car begins to slowly lower, the doors open and you find yourself in the morgue.")
		results = search_object("#447")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class EscapeCmdSet(CmdSet):
	key = "EscapeCmdSet"
	def at_cmdset_creation(self):
		self.add(escape())
		self.add(work())
	
class breakout(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(EscapeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")
