from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk atropos"
	aliases = ["Talk Atropos", "Talk atropos", "talk Atropos"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("atroposdone"):
			self.caller.msg("|/|mAtropos|n says: I'm done with you for the moment, go do something that's not standing there taking up space.")
			self.caller.msg("|mAtropos|n says: I'll let you know if I need you again.")
			return
		if self.caller.tags.get("foodrace"):
			self.caller.tags.remove("foodrace")
			self.caller.msg("|/|mAtropos|n says: Ah, my food, and it's not cold, excellent.")
			self.caller.msg("You hand Atropos the tray of food.")
			for o in self.caller.contents:
				if o.key == "Food":
					o.delete()
			self.caller.msg("|mAtropos|n says: Mmmmm, spicy tacos, Chef does good work.")
			self.caller.msg("Atropos moves to a small table set with a plate, silverware, and a glass of wine and enjoys her meal.")
			self.caller.msg("You might want to talk to her again once her mouth isn't full of food.")
			self.caller.tags.add("doordash")
			return
		if not self.caller.tags.get("doordash"):
			self.caller.msg("|/|mAtropos|n says: I'm famished, be a good little henchperson and head down to the kitchen and get my food from Chef, make sure you get it back here before it gets cold. I HATE cold food.")
			return
		if self.caller.tags.get("blackmail"):
			self.caller.msg("|/|m%s|n says: The problem is resolved. Our member should be out of solitary soon." % (self.caller.key))
			self.caller.msg("|mAtropos|n says: Interesting, so where's the debt money?")
			self.caller.msg("|m%s|n says: Turns out Nataly and Guard Jones had a little something setup, Nataly erased his debt out of the book." % (self.caller.key))
			self.caller.msg("|mAtropos|n says: That's excellent work, I've been suspicious of that little rat for a while.")
			self.caller.msg("|mAtropos|n says: And if there's one thing a Viper knows how to do, it's eliminate a rat.")
			self.caller.msg("|mAtropos|n says: If you're waiting for a hug and a handshake you're in the wrong place. Carry on with your day, I'll let you know if I need your services again.")
			self.caller.tags.add("natalydead")
			self.caller.tags.add("viewasset")
			self.caller.tags.add("atroposdone")
			return
		if self.caller.tags.get("debtcollector"):
			self.caller.msg("|/|mAtropos|n says: Here are the debts that need collected:|/Qlorvg Qzpv 345|/Vodllw Yofvh 124|/Hzizs Xlmmli 87")
			self.caller.msg("|mAtropos|n says: I could have sworn that there was another debt in here, but bookie must have collected before he got 86'd.")
			self.caller.msg("|mAtropos|n says: Go talk to these people and tell them you're there to |cCollect|n.")
			self.caller.msg("|mAtropos|n says: Make it snappy, solitary is no place for one of ours to be, we wouldn't leave you there, so don't be the reason they're left there.")
			return
		if self.caller.tags.get("debtcollected"):
			self.caller.tags.add("atroposdone")
			self.caller.tags.add("viewasset")
			self.caller.tags.remove("debtcollected")
			self.caller.msg("|/|mAtropos|n says: Ahh, wonderful, this'll top up our funds and get our member out of solitary.")
			self.caller.msg("|mAtropos|n says: If you're waiting for a hug and a handshake you're in the wrong place. Carry on with your day, I'll let you know if I need your services again.")
			return
		self.caller.msg("|/|mAtropos|n says: Ah, our newest recruit. We owe you some thanks for retrieving this debt book.")
		self.caller.msg("|mAtropos|n says: We're a bit behind on our bribes to the guards and they threw one of our members into solitary until we pay up.")
		self.caller.msg("|mAtropos|n says: I'm going to need someone to go collecting on these debts if I can get the cipher the old bookie used figured out.")
		self.caller.msg("|mAtropos|n says: Here, take a look see if you can figure it out:|/Qlorvg Qzpv 345|/Vodllw Yofvh 124|/Hzizs Xlmmli 87")
		self.caller.msg("|mAtropos|n says: I could have sworn that there was another debt in here, but bookie must have collected before he got 86'd.")
		self.caller.tags.add("debtcollector")
		self.caller.msg("|mAtropos|n says: Go talk to these people and tell them you're there to |cCollect|n.")
		self.caller.msg("|mAtropos|n says: Make it snappy, solitary is no place for one of ours to be, we wouldn't leave you there, so don't be the reason they're left there.")
		return

class AtroposCmdSet(CmdSet):
	key = "AtroposCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class atropos(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Atropos sits at a fine wooden desk doing some type of work in a notebook, occasionally referencing the debt book you got from Pierre."
		self.cmdset.add_default(AtroposCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mAtropos|n says: I wouldn't even have to raise my voice to have you killed."