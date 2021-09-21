from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk lucien"
	aliases = ["Talk Lucien", "Talk lucien", "talk Lucien"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("lucien"):
			self.caller.msg("|mLucien Laurin|n says: Isabelle is working on a plan to escape the prison, she needs your help.")
			self.caller.msg("|mLucien Laurin|n says: Please, go talk to her and give any assistance you can.")
			return
		if not self.caller.tags.get("fahad"):
			self.caller.msg("|/|mLucien Laurin|n says: I am very busy right now, I believe I have discovered a grave threat to the cartel. Come back later, S'il vous plait.")
			self.caller.msg("Lucien goes back to furiously searching through various files, paperwork, and pictures.")
			return
		self.caller.msg("|/|mLucien Laurin|n says: Ah %s, merci, regarde ici, I have discovered a grave threat to the cartel." % (self.caller.key))
		self.caller.msg("|mLucien Laurin|n says: We must get this information to Montreal, without it we face disaster.")
		self.caller.msg("|mLucien Laurin|n says: This must NOT be intercepted at any cost.")
		self.caller.msg("|mLucien Laurin|n says: Isabelle is working on a plan to escape the prison, she needs your help.")
		self.caller.msg("|mLucien Laurin|n says: Please, go talk to her and give any assistance you can.")
		self.caller.tags.add("lucien")
		info_proto = {
		"key": "Secret Info",
		"typeclass": "typeclasses.objects.nodropbook",
		"desc": "A sealed letter.",
		"story": "You carefully loosen the seal on the letter and read it.|/There is a rat in the house working with the NSA.|/It's somewhere near the top.|/The bearer of this info can be trusted, I recommend they are tasked with finding the rat.|/- Signed, Lucien Laurin.",
		"location": self.caller
		}
		spawn(info_proto)
		self.caller.msg("Lucien hands you a sealed letter.")
		return

class LucienCmdSet(CmdSet):
	key = "LucienCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class lucien(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Lucien is completely focused on the multitude of documents in front of him."
		self.cmdset.add_default(LucienCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mLucien|n says: Eh? I would not do that."