from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class watch(default_cmds.MuxCommand):
	"""
	Watch TV

	Usage:
	Watch TV

	See what's happening in the world.
	"""
	key = "watch tv"
	auto_help = True
	def func(self):
		if not self.caller.tags.get("busted"):
			self.caller.msg("|/Renee hands you the remote and you turn the volume up.")
			yield 4
			self.caller.msg("|/...Thank you Kent, as you can see behind me authorities from the National Spice Agency have seized a cargo container headed for our dear metropolis.")
			yield 7
			self.caller.msg("|/Now, the final numbers aren't in yet, but preliminary estimates say that 5 tons of super hot peppers, hidden inside fake bananas, have been confiscated.")
			yield 7
			self.caller.msg("|/Renee looks over at you wide-eyed, 'Sweet spaghetti monster in the sky, 5 TONS!! That's gonna cause a spice drought in the area. I bet Sugar is gonna use this an an excuse to raise his prices.'")
			yield 10
			self.caller.msg("|/Your attention is brought back to the broadcast 'National Spice Agents, acting on an anonymous tip, performed a daring pre-dawn raid on the docks seizing the Montreal based Bordel de Merde.'|/'In a press release, the NSA states that the cargo ship has ties to the shadowy French Canadian Faucheurs Fantômes, or Ghost Reapers, pepper cartel.'")
			yield 10
			self.caller.msg("|/This has been April O'Neil Channel 6 News, back to you Kent.")
			self.caller.msg("You turn the volume back down a bit and toss the remote to Renee.")
			return
		else:
			self.caller.msg("The TV is broken.")
			return

class TVCmdSet(CmdSet):
	key = "SleepCmdSet"
	def at_cmdset_creation(self):
		self.add(watch())
	
class tv(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A decent sized CRT Television.|/Someone has carefully sculpted tinfoil onto the rabbit ears in an attempt to improve reception."
		self.cmdset.add_default(TVCmdSet, permanent=True)
		self.locks.add("get:false()")