from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu
from evennia.prototypes.spawner import spawn

class talkingbubbles(default_cmds.MuxCommand):
	key = "Talk Bubbles"
	aliases = ["talk bubbles", "Talk bubbles", "talk Bubbles"]
	auto_help = True

	def func(self):
		if self.caller.tags.get("sugarbaby") and not self.caller.tags.get("bubsdone"):
			EvMenu(self.caller, "typeclasses.talking_bubbles", startnode="sugar_mission_node")
			return
		EvMenu(self.caller, "typeclasses.talking_bubbles", startnode="menu_start_node")

def menu_start_node(caller):
	text = "...Naw, naw it's not like that, you're getting it all wrong.|/Oh, hey, hey-hey, %s, Bubbles looks back to the squirrel, I was just telling this little squirrel here about the spice dream.|/But, Bubbles shakes his head, he just doesn't get it, do you even think that squirrels dream?" % (caller.key)
	options = ({"desc": "I'm a, I'm not real sure on that one Bubbs. I suppose they could. Maybe you could explain the spice dream to me?",
		"goto": "dreams"},
		{"desc": "What's the good word? How's life treating you?",
		"goto": "generalbs"},
		{"desc": "Shit man, I forgot I gotta run. Things to do.",
		"goto": "exit"})
	return text, options

def dreams(caller):
	text = "Bubbles chuckles, You think you're smarter than a squirrel. Alright big brain, here's the long and short.|/You get some dream spice, take the spice, and sleep."
	options = ({"desc": "Well that all seems pretty self explanatory, what about all that is the squirrel having problems with?",
		"goto": "biggerissues"},
		{"desc": "Right, ok. I should be able to figure it out from there",
		"goto": "exit"})
	return text, options

def generalbs(caller):
	text = "It goes, sometimes it don't. Just the way life is right? All just another turn of the pattern. But I always got $5 on the dream."
	options = ({"desc": "So, what's this about a spice dream?",
		"goto": "dreams"})
	return text, options

def biggerissues(caller):
	text = "See, I told you ya ain't no smarter than this squirrel, even he had the sense to see there has to be something bigger.|/Your brain might be big, but your understanding *tsk* it's real small you know?"
	options = ({"desc": "Alright then, explain it to me like I'm a squirrel.",
		"goto": "squirrelstyle"},
		{"desc": "You know what, shove it. I'm outta here.",
		"goto": "exit"})
	return text, options

def squirrelstyle(caller):
	text = "Okay, but, my squirrel is a bit rusty, and I was taught by a Malabar giant squirrel, so excuse the accent and some of it doesn't translate directly.|/Bubbles clears his throat, Squeek, squeeky, chitter chitter, squeakity, chitter. Squeeker squeekity bark chitter.|/Bubbles stares at you unblinkingly, head cocked slightly to the side."
	options = ({"desc": "God dammit Bubbs, you've burnt every last brain cell haven't you. IN ENGLISH DAMMIT!!",
		"goto": "englishstyle"},
		{"desc": "Fuck this shit, you burnt out spice crazed madman, have a good day.",
		"goto": "exit"})
	return text, options

def englishstyle(caller):
	text = "Bubbles twitches violently. Oh, right. *ahem* Getting to the dream is the easy part, after that is when the hard part starts.|/You can get to the dream anywhere you can get dream spice and a place to sleep.|/Just watch out for Omar."
	options = ({"desc": "So it's like a dream puzzle? Interesting.",
		"goto": "menu_start_node"})
	return text, options

def sugar_mission_node(caller):
	caller.tags.add("bubsdone")
	recorder_proto = {
		"key": "Microrecorder",
		"typeclass": "typeclasses.objects.DefaultObject",
		"desc": "A handheld sony audio recorder.",
		"location": caller
	}
	spawn(recorder_proto)
	text = "Oh, Sugar wants the microrecorder back? Ok, ok, let me just transfer my research data to dead tree format.|/Bubbles takes the recorder, rewinds, and presses play. All you hear is a bunch of squeaking and chittering.|/Ok, ok. Yeah that's good stuff. Alright, here you go."
	options = ({"desc": "Thanks Bubbles, I really appreciate you making this easy for me.",
		"goto": "menu_start_node"})
	return text, options

def exit(caller):
	text = "Some think this world is the dream, and one day we will wake from it. But only those that truly dream understand the truth."
	options = ()
	return text, options

def silentexit(caller):
	text = ""
	options = ()
	return text, options

class BubblesCmdSet(CmdSet):
	key = "BubblesCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingbubbles())

class bubbles(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Bubbles sits on a bench, holding a small squirrel making chittering noises.|/The entire neighborhood either loves him, or things he's a madman."
		self.cmdset.add_default(BubblesCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("evnpc")
		self.db.get_err_msg = "Watch it! The place is crawling with feds, they'll arrest your ass like that. *snaps fingers*"