from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class prisonwallet(default_cmds.MuxCommand):
	key = "Check Wallet"
	aliases = ["check wallet", "Check wallet", "check Wallet"]
	auto_help = True
	def func(self):
		self.caller.msg("You open up your wallet, you've got %s books of stamps." % (self.caller.db.stamps))
		return

class WalletCmdSet(CmdSet):
	key = "WalletCmdSet"
	def at_cmdset_creation(self):
		self.add(prisonwallet())

class wallet(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A dirty brown leather wallet. Use |cCheck Wallet|n to see how many stamps you have."
		self.cmdset.add_default(WalletCmdSet, permanent=True)
		self.locks.add("drop:false()")