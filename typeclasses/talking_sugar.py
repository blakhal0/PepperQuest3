from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from typeclasses.objects import DefaultObject
from evennia.utils.evmenu import EvMenu
from evennia.prototypes.spawner import spawn

class talkingsugar(default_cmds.MuxCommand):
	key = "Talk Sugar"
	aliases = ["talk sugar", "Talk sugar", "talk Sugar"]
	auto_help = True

	def func(self):
		EvMenu(self.caller, "typeclasses.talking_sugar", startnode="menu_start_node")

def menu_start_node(caller):
	text = "What's up pla-YAH!!!|/Sugar attempts some type of complicated hand shake with you.|/It's all good, we'll get it next time bruh."
	options = []
	if not caller.tags.get("sugarbaby") and not caller.tags.get("sugardone"):
		options.append({"desc": "Umm, yeah, how's it going. Luke sent me, you got something for him?", "goto": "offer"})
	if not caller.search("Microrecorder", location=caller, quiet=True) or not caller.search("Package", location=caller, quiet=True) or not caller.search("Spicy Panda Snacks", location=caller, quiet=True):
		if not caller.tags.get("sugardone") and caller.tags.get("sugarbaby"):
			options.append({"desc": "What do you need me to do again?", "goto": "jobs"})
	if caller.search("Microrecorder", location=caller, quiet=True) and caller.search("Package", location=caller, quiet=True) and caller.search("Spicy Panda Snacks", location=caller, quiet=True):
		options.append({"desc": "I got all the things!", "goto": "done"})
	options.append({"desc": "So I've heard about this dream spice stuff, what's that all about?", "goto": "getspice"})
	options.append({"desc": "Oh, you know what, I just remembered I got this thing. Time sensitive, I gotta roll.", "goto": "exit"})
	return text, options

def offer(caller):
	text = "Right, so here's the deal, Luke still owe from last time, and your broke looking ass for sure don't have any cash.|/He says you're real good at running errands though, so you want the stuff, you do as needed, got it?"
	options = ({"desc": "God DAMMIT LUKE!! Fine, what do I need to do.",
		"goto": "jobs"},
		{"desc": "Forget that, I'm outta here.",
		"goto": "exit"})
	return text, options

def jobs(caller):
	tasks = ""
	if not caller.tags.get("sugarbaby"):
		caller.tags.add("sugarbaby")
	if not caller.search("Microrecorder", location=caller, quiet=True):
		tasks += "Bubbles borrowed my microrecorder, talking about some shit about squirrels, I need you to get that back.|/"
	if not caller.search("Package", location=caller, quiet=True):
		tasks += "I need you to go pick up a package for me at the SpiceEasy, the password for the door is Hand of Glory.|/"
	if not caller.search("Spicy Panda Snacks", location=caller, quiet=True):
		tasks += "I'm kinda hungry, I want some spicy panda snacks from the corner store."
	text = "See, I knew right off when I looked at you, you was real. Aight, here's what I need:|/%s" % (tasks)
	options = ({"desc": "What, no kitchen sink? Fine, I'll get to work on it.",
		"goto": "menu_start_node"})
	return text, options

def done(caller):
	for o in caller.contents:
		if o.key == "Microrecorder" or o.key == "Spicy Panda Snacks" or o.key == "Package":
			o.delete()
	caller.tags.add("sugardone")
	caller.tags.remove("sugarbaby")
	peppers_proto = {
		"key": "Ghost Peppers",
		"typeclass": "typeclasses.objects.DefaultObject",
		"desc": "A baggie of dried ghost peppers.",
		"location": caller
	}
	spawn(peppers_proto)
	text = "Thanks a lot, I'll take all that *Sugar grabs the stuff*, and here's this for you *Sugar hands you a bag of Ghost Peppers*."
	options = ({"desc": "Well I'd say it's been fun. But it hasn't.",
		"goto": "menu_start_node"})
	return text, options

def getspice(caller):
	if caller.search("Dream Spice", location=caller, quiet=True):
		text = "Hey yo, don't get greedy now. You already got some."
		options = ({"desc": "Oh, yeah I forgot I already had some.",
			"goto": "menu_start_node"})
	else:
		text = "Yeah, this the new new stuff right here. Whole NEW LE-VEL.|/You ever eat super spicy food right before bed and then get wild dreams?|/Well this is like that, but way better, straight science and shit.|/They found these dream peppers that grow in the desert and gave em to these SUPER geeks.|/Ripped em apart at the DNA level, spliced in some tiger blood or some such shit, and made some kind of super pepper. Now the streets got it.|/Since I like you, you can have some for free, come back if you need more."
		dspice_proto = {
			"key": "Dream Spice",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A baggie of rainbow pepper crystals.",
			"location": caller
		}
		spawn(dspice_proto)
		options = ({"desc": "Thanks, I appreciate it.",
			"goto": "menu_start_node"})
	return text, options

def exit(caller):
	text = "Lay-TAH pla-YAH!!"
	options = ()
	return text, options

def silentexit(caller):
	text = ""
	options = ()
	return text, options

class SugarCmdSet(CmdSet):
	key = "SugarCmdSet"
	def at_cmdset_creation(self):
		self.add(talkingsugar())

class sugar(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A little too tall, bleached blonde hair, sagging shorts, a designer T-shirt that's extra long, a hat with a flat bill, and as white as his name.|/That's Sugar.|/Sugar is a douchebag, Sugar is also the only dealer with quality product within three area codes."
		self.cmdset.add_default(SugarCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("evnpc")
		self.db.get_err_msg = "Easy on the threads. I've blasted fools for less than wrinkling my shirt. Noimsayin."