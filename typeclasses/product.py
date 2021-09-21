from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class reup(default_cmds.MuxCommand):
	key = "Distribute"
	auto_help = True
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		target = self.caller.search(self.item, candidates=self.caller.location.contents, quiet=True)
		if not target:
			self.caller.msg("|/There's no one by that name to give product to.")
			return
		if target[0].key in ["Leia", "Eduardo", "Natasha", "Vivian"]:
			self.caller.msg("|/|m%s|n says: You knob head, I don't need this, get it to the dealers!" % (target[0].key))
			return
		if target[0].db.faction == "fed":
			self.caller.msg("|/|rWHAT ARE YOU DOING??!?!?!?! THAT'S A FED!!!")
			return
		if not target[0].tags.get("dealer"):
			self.caller.msg("|/|m%s|n says: WOW that's a lot of spice!! Thanks!" % (target[0].key))
			self.caller.msg("|rOH NO!!! You just accidentally gave product to a random stranger!!|n")
			self.caller.msg("You've just cost the cartel money and product.")
			return
		if target[0].tags.get("dealer"):
			if self.caller.tags.get(target[0].db.distnum):
				self.caller.msg("|/You've already distributed the product to this dealer.")
				return
			self.caller.msg("|/|m%s|n says: Great, we were just about out. Thanks!" % (target[0].key))
			self.caller.msg("|rYou hand the re-up package to the dealer.|n")
			self.caller.tags.add(target[0].db.distnum)
			self.caller.db.distributed += 1
		if self.caller.db.distributed == 5:
			self.caller.msg("|/|rYou've delivered all the product, the dealers are restocked.|n")
			self.caller.tags.add("distributor")
			for o in self.caller.contents:
				if o.key == "Product":
					o.delete()
			return
		return

class ProductCmdSet(CmdSet):
	key = "ProductCmdSet"
	def at_cmdset_creation(self):
		self.add(reup())
	
class product(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Packages of Spice. |cDistribute|n them."
		self.cmdset.add_default(ProductCmdSet, permanent=True)
		self.locks.add("drop:false()")