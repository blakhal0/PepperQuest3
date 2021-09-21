from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class ytest(default_cmds.MuxCommand):
	key = "something"
	auto_help = True
	def func(self):
		answer = yield("Press enter to continue")
		self.caller.msg("Yay")
		return

class TestThingCmdSet(CmdSet):
	key = "TestThingCmdSet"
	def at_cmdset_creation(self):
		self.add(ytest())

class tester(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A comfy inviting bed with Star Wars themed sheets.|/Maybe you should get some sleep."
		self.cmdset.add_default(TestThingCmdSet, permanent=True)
		self.locks.add("get:false()")