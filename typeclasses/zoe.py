from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk zoe"
	aliases = ["Talk Zoe", "Talk zoe", "talk Zoe" ]
	auto_help = True
	def func(self):
		if self.caller.db.faction == "fed":
			self.caller.msg("There is no one here by that name to talk to.")
			return
		self.caller.msg("|/|mZoe|n says: Bonjour %s, we have been waiting a long time for you, I had almost given up hope." % (self.caller.key))
		self.caller.msg("|mZoe|n says: Lucien gave to you a document yes? Good, good. We must get back to Montreal and we have a short time to go many kilometers.")
		self.caller.msg("Zoe hands you a change of clothes, with great joy you change out of the itchy prison uniform and follow Zoe across the fields of tall corn.")
		self.caller.msg("It is a long and arduous crossing to the train yard where you hop a freight train heading north. Zoe sketches a small ghost and scythe on the outside of the door before closing it.")
		self.caller.msg("|mZoe|n says: You can relax now, we have 'friends' that are in place at all the stops from here to the great north, we won't be bothered.")
		self.caller.msg("|mZoe|n says: Get some rest, I think you won't be in Montreal long.")
		self.caller.msg("The gentle rumbling of the train lulls you to sleep. Finally not having to worry about getting stabbed before you wake up, you close your eyes and enjoy a deep restful sleep.")
		self.caller.msg("|/|mZoe|n says: Wake up, we are here, you slept an entire day.")
		self.caller.msg("You hop off the train.")
		results = search_object("#2751")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)

class ZoeCmdSet(CmdSet):
	key = "ZoeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class zoe(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Zoe stands up in the grass wearing a ghillie suit."
		self.cmdset.add_default(ZoeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:attr(faction, cartel)")
		self.db.get_err_msg = "|/|mZoe|n says: I can just as easily say you never made it out of the sewers..."