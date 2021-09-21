from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class play(default_cmds.MuxCommand):
	key = "talk old timers"
	aliases = ["Talk Old Timers", "Talk Old timers", "Talk old Timers", "talk Old Timers", "talk Old timers", "talk old Timers"]
	auto_help = False
	def func(self):
		if self.caller.tags.get("oldtimers"):
			self.caller.msg("Hey, there's the kid with the big brains by golly! Thanks for your help!!")
			return
		self.caller.msg("|/|mChuck|n says: No no no. That's not right you old goat. Turn your damned hearing aide up, I already said that won't work.")
		self.caller.msg("|mRalph|n says: You know what, you got about as much sense as hairs on your head.")
		self.caller.msg("Both old timers look up at you through thick glasses.")
		self.caller.msg("|mChuck|n says: Whatta you want? Dang kids always sticking their noses where they don't belong.")
		self.caller.msg("|mRalph|n says: Think you're pretty smart eh, sooo much smarter than your elders? Ya dag gum whipper snapper. Well, you're so smart, figure this out.")
		self.caller.msg("|/+-----+-----+-----+")
		self.caller.msg("|  |r$|n  |  |y@     $|n  |")
		self.caller.msg("|     ||-----+-----|")
		self.caller.msg("|  |r#|n  |     |  ?  |")
		self.caller.msg("||-----+-----|     |")
		self.caller.msg("|  |c#     @|n  |  ?  |")
		self.caller.msg("+-----+-----+-----+|/")
		answer = yield("What's your answer smarty pants?: ")
		if answer in ["%!", "% !", "%,!", "%, !", "!%", "! %", "!,%", "!, %"]:
			self.caller.tags.add("oldtimers")
			self.caller.msg("Well I'll be, that solves it!! Good job!! Looks like maybe the old timers need a little reminder that the young are the future sometimes.")
			self.caller.msg("We don't have much, but here, you can have this. Now, don't go causing any trouble you hear? You'll break your dear old mom's heart.")
			matches_proto = {
				"key": "Match",
				"typeclass": "typeclasses.objects.DefaultObject",
				"desc": "A single strike anywhere match.",
				"location": self.caller
				}
			spawn(matches_proto)
			self.caller.msg("The Old Timers hand you a strike anywhere Match.")
			return
		else:
			self.caller.msg("|/You block head, that's not the right answer.|/Go on get, leave this to the professionals.")
			return

class OldTimersCmdSet(CmdSet):
	key = "OldTimersCmdSet"
	def at_cmdset_creation(self):
		self.add(play())
	
class oldtimers(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A couple of old timers are sitting at a table, scratching their bald heads looking at some weird puzzle."
		self.cmdset.add_default(OldTimersCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "Keep your dag nap hands to yourself."