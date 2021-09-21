from evennia import default_cmds, InterruptCommand, search_object, search_tag
import random
from random import randint
from evennia.utils import interactive
from evennia.prototypes.spawner import spawn
from evennia.utils.evmenu import EvMenu
import string

class read(default_cmds.MuxCommand):
	"""
	Read books and stuff

	Usage:
	Read (object) i.e. Read Tutorial

	Used to read books, signs, etc. Provides more info than just Look.
	"""
	key = "Read"
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		bookshelves = search_tag("bookshelf").filter(db_location=self.caller.location)
		if not bookshelves:
			target = self.caller.search(self.item)
		else:
			bookshelf = bookshelves[0]
			target = self.caller.search(self.item, candidates=self.caller.location.contents + bookshelf.contents)
		if not target:
			self.caller.msg("There's not a %s here to read." % (self.item))
			return
		if not target.tags.get("readable", category="isreadable"):
			self.caller.msg("This item can't be read, just Look at it")
			return
		if target.tags.get("single", category="isreadable"):
			self.desc = target.db.story
			self.caller.msg("|/|g%s|n|/%s" % (target.key, self.desc))

class changefact(default_cmds.MuxCommand):
	key = "faction"
	def parse(self):
		self.faction = self.args.lstrip()
	def func(self):
		if self.faction == "none":
			self.caller.db.faction = "none"
			self.caller.msg("You are now unaligned.")
			return
		if self.faction == "fed":
			self.caller.db.faction = "fed"
			self.caller.msg("You are now a fed.")
			return
		if self.faction == "cartel":
			self.caller.db.faction = "cartel"
			self.caller.msg("You are now a cartel member.")
			return

class changecart(default_cmds.MuxCommand):
	key = "cartel"
	def parse(self):
		self.cartel = self.args.lstrip()
	def func(self):
		if self.cartel == "none":
			self.caller.db.cartel = "none"
			self.caller.msg("You are now unaligned to cartels.")
			return
		if self.cartel == "vipers":
			self.caller.db.cartel = "vipers"
			self.caller.msg("You are now a member of the Naga Vipers cartel.")
			return
		if self.cartel == "reapers":
			self.caller.db.cartel = "reapers"
			self.caller.msg("You are now a member of the Ghost Reapers cartel.")
			return

class givetag(default_cmds.MuxCommand):
	key = "tag"
	def parse(self):
		self.tagname = self.args.lstrip()
	def func(self):
		if not self.caller.tags.get(self.tagname):
			self.caller.tags.add(self.tagname)
			self.caller.msg("|rYou've added a tag named %s|n" % (self.tagname))
			return
		else:
			self.caller.msg("|rYou already have a tag named %s|n" % (self.tagname))

class remtag(default_cmds.MuxCommand):
	key = "untag"
	def parse(self):
		self.tagname = self.args.lstrip()
	def func(self):
		if self.caller.tags.get(self.tagname):
			self.caller.tags.remove(self.tagname)
			self.caller.msg("|rYou've removed a tag named %s|n" % (self.tagname))
			return
		else:
			self.caller.msg("|rYou don't have a tag named %s|n" % (self.tagname))

class shtag(default_cmds.MuxCommand):
	key = "shtag"
	def func(self):
		taglist = self.caller.tags.all()
		self.caller.msg("|rYou've got the following tags:|/%s" % (taglist))
		return

class talkNPC(default_cmds.MuxCommand):
	"""
	Talk to NPC's (non-playable characters).

	Usage:
	Talk <NPC Name>

	Checks if the NPC has something to say.
	Some NPC's might have more than just one thing to say,
	Try talking to them more than just once.
	"""
	key = "Talk"
	auto_help = True

	def parse(self):
		self.npcname = self.args.lstrip()

	def func(self):
		target = self.caller.search(self.npcname)
		if not target:
			self.caller.msg("There's no one here by that name to talk to.")
			return
		elif not target.tags.get("talkative", category="npc"):
			self.caller.msg("You're trying to talk to an inanimate object...|/Might be time to refill that prescription.")
			return
		if not target.access(self.caller, "view"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
# Single
		elif target.tags.get("single", category="talkative"):
			if not target.db.msg:
				self.caller.msg("They don't appear to have anything to say.")
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
			return
# Multi
		elif target.tags.get("multi", category="talkative"):
			if not target.db.msg:
				self.caller.msg("They don't appear to have anything to say.")
			else:
				self.text = "%s" % random.choice(target.db.msg)
				self.caller.msg("|/|m%s|n says: %s" % (target.key, self.text))
			return
# If tag
		elif target.tags.get("tagnpc", category="talkative"):
			if self.caller.tags.get(target.db.tag):
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.taggedresp))
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.untaggedresp))
			return
# Add tag
		elif target.tags.get("addtagnpc", category="talkative"):
			if not self.caller.tags.get(target.db.addtag):
				self.caller.tags.add(target.db.addtag)
			self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
# Faction
		elif target.tags.get("faction", category="talkative"):
			if self.caller.db.faction == "none":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgnone))
				return
			if self.caller.db.faction == "fed":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgfed))
				return
			if self.caller.db.faction == "cartel":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgcartel))
				return
# Inmate - Cartel
		elif target.tags.get("cartel", category="talkative"):
			if self.caller.db.cartel == "none":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgnone))
				return
			if self.caller.db.cartel == "vipers":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgvipers))
				return
			if self.caller.db.cartel == "reapers":
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msgreapers))
				return
#EvMenu
		elif target.tags.get("evm", category="talkative"):
			EvMenu(self.caller, "typeclasses.talking_spiceeasy", startnode="menu_start_node")
			return