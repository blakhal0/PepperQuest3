from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class deal(default_cmds.MuxCommand):
	key = "talk pusher"
	aliases = ["Talk Pusher", "Talk pusher", "talk Pusher"]
	auto_help = False
	def func(self):
		self.caller.msg("|/|mPusher|n says: Hey you, you lookin? I got the hookup right here.")
		answer = yield("So what's what, you looking or not? Yes or no, I don't have all day.")
		if answer.lower() in ["y", "yes"]:
			self.caller.msg("|/|mPusher|n says: Cool cool, look man, I hate to be that guy, but, you know, the streets is the streets...")
			answer2 = yield("You a cop? Yes or no? You gotta tell me if you are.")
			if answer2.lower() in ["n", "no"]:
				self.caller.msg("|/|mPusher|n says: All good then, step into my office, you're new here so the first one's free.")
				self.caller.msg("You follow the pusher over to the corner")
				self.caller.msg("|/|mPusher|n says: Look here, I got the best of the best, the hottest of the hot, check it out.")
				self.caller.msg("The pusher reaches into his coat and pulls out a gun.")
				self.caller.msg("|mUnder Cover Fed|n says: GET ON THE GROUND SCUMBAG!! NOW DO IT NOW!!|/Ten-fiver-nine, the spider caught a fly.")
				self.caller.msg("You're quickly handcuffed and a black hood is pulled over your head.")
				self.caller.msg("|mUnder Cover Fed|n says: It's the reeducation center for this one. One less fiend on the street.|/")
				results = search_object("#219")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			if answer2.lower() in ["y", "yes"]:
				self.caller.msg("|/|mUnder Cover Fed|n says: Oh, no shit, me too. Go on and beat it, I've got work to do.|/The Under Cover Fed saunters back over to the wall and continues clicking and whistling.")
				return
		if answer.lower() in ["n", "no"]:
			self.caller.msg("|/|mPusher|n says: Then hit the bricks, I ain't got time for the likes of you.")
			return
		self.caller.msg("|/|mPusher|n says: Look here mush mouth, yes or no isn't all that difficult, I don't have time to waste, beat it.")
		return

class PusherCmdSet(CmdSet):
	key = "PusherCmdSet"
	def at_cmdset_creation(self):
		self.add(deal())
	
class pusher(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A shady looking character stands against the brick wall occasionally clicking and whistling.|/'Spice, got spice, *tick tick* got that spice *whistle*'"
		self.cmdset.add_default(PusherCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")