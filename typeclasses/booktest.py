from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class addbook(default_cmds.MuxCommand):
	key = "booktest"
	auto_help = False
	def func(self):
		target = search_object("#2623")
		target[0].db.story += "|/%s" % (self.caller.key)
		return

class AddBookCmdSet(CmdSet):
	key = "AddBookCmdSet"
	def at_cmdset_creation(self):
		self.add(addbook())
	
class booktest(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(AddBookCmdSet, permanent=True)
		self.locks.add("get:false()")