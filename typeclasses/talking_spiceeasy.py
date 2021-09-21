from evennia import default_cmds, CmdSet, InterruptCommand, search_object
from evennia.utils.evmenu import EvMenu
import random
from evennia.prototypes.spawner import spawn

def menu_start_node(caller):
	openingline = ["Hey there, how's it going? I just can't get enough of this place!", "This place is really something else isn't it! I never want to leave!!", "I would drink a THOUSAND of these drinks if I could", "I NEED MORE!! MORE MORE MORE!!!", "I don't think I can fit another drop in me, but I just keep ordering drinks.", "These spicy drinks are AMAZING, I can't get enough!", "Oh, oh I'm sooo bloated, why do I keep drinking.", "If I was drowning in a sea of these Sizzling Sazerac, I would drink the sea dry."]
	firstoption = ["This place is really something isn't it?", "Wow, I've never been anywhere like this before!", "This is the best place ever!!", "I feel like I never want to leave this place", "After being here, who would go anywhere else?!?!"]
	text = random.choice(openingline)
	options = []
	options.append({"desc": "%s" % (random.choice(firstoption)), "goto": "randombs"})
	options.append({"desc": "So I was wondering if you might be holding a Package... for Sugar, the, uhhh, provider of spice on the other side of town? I was sent here to get it.", "exec": boot})
	options.append({"desc": "Oh, you know what, I think I got you confused with someone else, my apologies.", "goto": "exit"})
	return text, options

def randombs(caller):
	text = "You got that right, this place it the cat's pajamas!"
	options = ({"desc": "Oh, by the way I was wondering...",
		"goto": "menu_start_node"})
	return text, options

def boot(caller):
	if caller.db.bothered == 3:
		return "kickout"
	else:
		caller.db.bothered += 1
		return "goaway"

def goaway(caller):
	text = "You some kind of Fed or something? Get the hell away from me before I have the bouncer introduce your face to the alley floor."
	options = ()
	return text, options

def kickout(caller):
	caller.db.bothered = 2
	caller.msg("|/______________________________________________________________________________")
	caller.msg("|/Alright, you're making a nuisance of yourself, it's time to go.")
	caller.msg("______________________________________________________________________________")
	caller.msg("|/")
	caller.msg("The bouncer grabs you by the shoulder and the back of the pants and carries you out to the door and tosses you into the alley.|/")
	results = search_object("#116")
	caller.move_to(results[0], quiet=True, move_hooks=False)
	text = ""
	options = ()
	return text, options

def exit(caller):
	text = "Hey, enjoy the night, and gulp down a few of these drinks while you're here!! As many as you can!!!"
	options = ()
	return text, options
