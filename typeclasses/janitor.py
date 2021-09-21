from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk janitor"
	aliases = ["Talk Janitor", "Talk janitor", "talk Janitor" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mJanitor|n says: Hey, watch what you're doing there, I gotta clean all this stuff.")
		self.caller.msg("|mJanitor|n says: Hi, the name is Itor, Jan Itor... M.D.")
		self.caller.msg("|m%s|n says: You're a doctor?" % (self.caller.key))
		self.caller.msg("|mJanitor|n says: What? Just because a guy scrubs a toilet, he can't be educated? You know, I've had it up to here with you arrogant jerks.")
		self.caller.msg("|mJanitor|n says: 'Oh, that guy cleans up my trash, he must be a mouth breathing uneducated knuckle dragging idiot, I'm surprised he doesn't just run around flinging poo at us.'")
		self.caller.msg("|m%s|n says: No, no that's not what I...." % (self.caller.key))
		self.caller.msg("|mJanitor|n says: Haha, I'm just yanking your chain. I've got a degree in front end web design, you can see how far that gets you.")
		self.caller.msg("|mJanitor|n says: You think if I had doctor money I'd spend my time cleaning up old coffee cups and scrubbing sinks? Come on now.")
		self.caller.msg("|m%s|n says: So you clean the ENTIRE building? What kind of security clearance did you need for that?" % (self.caller.key))
		self.caller.msg("|mJanitor|n says: Sure do, every inch. Beauty of being the 'lowest bidder', just had to sign a document saying I wouldn't betray government secrets.")
		self.caller.msg("|mJanitor|n says: Well, apparently unlike you fancy suit wearing folk, I don't have time to just stand around chit chatting in the bathroom, I've got work to do.")
		self.caller.msg("The janitor goes back to work.")
		return

class JanitorCmdSet(CmdSet):
	key = "JanitorCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class janitor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Janitor is busy cleaning the bathroom, occasionally grabbing items off the cart and fussing with an obviously fake mustache."
		self.cmdset.add_default(JanitorCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mJanitor|n says: Hey there, I'm the one that picks stuff up around here."