from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn
from random import randint

class plunder(default_cmds.MuxCommand):
	key = "steal"
	aliases = ["Steal"]
	auto_help = False
	def func(self):
		if not self.caller.search("Sticky Hand", location=self.caller, quiet=True):
			self.caller.msg("|/Command 'steal' is not available. Type ''help'' for help.")
			return
		if self.caller.search("Heist Loot", location=self.caller, quiet=True):
			self.caller.msg("|/Feeling bold from your recent success, you give it another shot.")
			self.caller.msg("The Naga Viper guard sees you and grabs you by the throat, pinning you against the cell door.")
			self.caller.msg("There's a scuffle of feet behind you and you feel several sharp objects stabbing you in the back.")
			for o in self.caller.contents:
				if o.key == "Heist Loot":
					o.delete()
			self.caller.msg("The Naga Viper guard rummages around in your pockets, finds the stolen loot, and tosses it back into the cell.")
			self.caller.msg("Woozy from the blood loss and the lack of oxygen, you crumble to the floor when you're finally released.")
			results = search_object("#436")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		luck = randint(1, 4)
		if luck == 1:
			self.caller.msg("|/You take a look around, there's a Naga Viper cartel member standing right there on the catwalk staring you down, not to mention the ones in the cell.")
			self.caller.msg("This seems like a terrible plan.")
			self.caller.msg("Certain that there's an impending infirmary visit in your immediate future, you decide to walk away and try later.")
			return
		if luck == 2:
			self.caller.msg("|/You take a look around, there's a Naga Viper cartel member standing right there on the catwalk staring you down, not to mention the ones in the cell.")
			self.caller.msg("Fuck those assholes, I'm a Ghost Reaper, I'll take what I want.")
			self.caller.msg("You pull the sticky hand back and let if fly.")
			self.caller.msg("|mCartel Member|n shouts: What the hell just slapped me in the ear?")
			self.caller.msg("You turn around and walk directly into your cell to hide.")
			results = search_object("#292")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		if luck in [3, 4]:
			self.caller.msg("|/You walk up to the Naga Viper keeping watch.")
			self.caller.msg("|m%s|n says: Hey, isn't that one of your people down there getting stabbed?" % (self.caller.key))
			self.caller.msg("|mCartel Member|n says: WHAT??!!?")
			self.caller.msg("With the outside guard distracted you pull the sticky hand back and let it fly at a bundle of stamps nearest the door.")
			self.caller.msg("SUCCESS!!")
			loot_proto = {
			"key": "Heist Loot",
			"typeclass": "typeclasses.objects.nodropobj",
			"desc": "A bundle of books of stamps.",
			"location": self.caller
			}
			spawn(loot_proto)
			self.caller.msg("You quickly pocket the loot.")
			self.caller.msg("|m%s|n says: Oh, my mistake, that's just some random snitch, nevermind." % (self.caller.key))
			self.caller.msg("Take the loot back to Fahad.")
			return

class HeistCmdSet(CmdSet):
	key = "HeistCmdSet"
	def at_cmdset_creation(self):
		self.add(plunder())
	
class heist(DefaultObject):
	def at_object_creation(self):
		self.cmdset.add_default(HeistCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")