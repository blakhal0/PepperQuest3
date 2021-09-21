from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class sleep(default_cmds.MuxCommand):
	key = "Tango Acquired"
	auto_help = True
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		target = self.caller.search(self.item, candidates=self.caller.location.contents)
		if not target:
			self.caller.msg("|/There's no one named %s nearby." % (self.item))
			return
		if target.tags.get("cartelasset"):
			self.caller.msg("|/|mLowe|n says: Copy that, proceeding to engage target now.")
			yield 3
			self.caller.msg("The target suddenly swats at their neck, as if a fly bit them.")
			self.caller.msg("As the target starts to go limp, a member of Lowe's extraction team pops up from nearby cover and drags them off into the trees.")
			self.caller.msg("|mLowe|n says: Target extraction success, returning to HQ.")
			results = search_object("#2990")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.tags.add("subjectextracted")
			self.caller.tags.remove("earwig")
			for o in self.caller.contents:
				if o.key == "TBASR":
					o.delete()
			self.caller.msg("|/You head back to HQ and into the Q Branch.")
			self.caller.msg("|mAlgernop|n says: Okay... let's see if this works better than last time...")
			self.caller.msg("Algernop successfully removes the TBASR, you only drool for a little while.")
			return
		if not target.tags.get("talkative", category="npc") and not target.tags.get("specialnpc") and not target.has_account:
			self.caller.msg("|/|mLowe|n says: What have you been smoking agent? You're attempting to extract a inanimate object.")
			return
		self.caller.msg("|/|mLowe|n says: Copy that, proceeding to engage target now.")
		yield 3
		self.caller.msg("|/|mLowe|n says: GOD DAMMIT, Agent %s, that's a civilian, not that it really matters, they're all guilty of something if we dig deep enough." % (self.caller.key))
		self.caller.msg("|mLowe|n says: Pull your head out of your ass, you're making me look bad.")
		return


class EarwigCmdSet(CmdSet):
	key = "EarwigCmdSet"
	def at_cmdset_creation(self):
		self.add(sleep())
	
class earwig(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "You feel a small bump behind your ear, that's the TBASR."
		self.cmdset.add_default(EarwigCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("drop:false()")