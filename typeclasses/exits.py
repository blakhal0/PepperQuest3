from evennia import DefaultExit, search_object
from evennia.utils.evmenu import get_input
import random

class Exit(DefaultExit):
    """
    Exits are connectors between rooms. Exits are normal Objects except
    they defines the `destination` property. It also does work in the
    following methods:

     basetype_setup() - sets default exit locks (to change, use `at_object_creation` instead).
     at_cmdset_get(**kwargs) - this is called when the cmdset is accessed and should
                              rebuild the Exit cmdset along with a command matching the name
                              of the Exit object. Conventionally, a kwarg `force_init`
                              should force a rebuild of the cmdset, this is triggered
                              by the `@alias` command when aliases are changed.
     at_failed_traverse() - gives a default error message ("You cannot
                            go there") if exit traversal fails and an
                            attribute `err_traverse` is not defined.

    Relevant hooks to overload (compared to other types of Objects):
        at_traverse(traveller, target_loc) - called to do the actual traversal and calling of the other hooks.
                                            If overloading this, consider using super() to use the default
                                            movement implementation (and hook-calling).
        at_after_traverse(traveller, source_loc) - called by at_traverse just after traversing.
        at_failed_traverse(traveller) - called by at_traverse if traversal failed for some reason. Will
                                        not be called if the attribute `err_traverse` is
                                        defined, in which case that will simply be echoed.
    """

    pass

# Message Exits
class msgexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/Test|/"
		self.db.err_traverse = "|/You cannot go that way|/"
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				self.caller.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

# MazePortal Exits
class mazeport(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/|rThe Spiceronomicon glows red and emits a great heat as you pass through the portal, you are suddenly teleported.|n"
		self.db.err_traverse = "|/You cannot go that way|/"
		self.locks.add("traverse:holds(Spiceronomicon) and tag(acolyte)")
		self.locks.add("view:holds(Spiceronomicon) and tag(acolyte)")
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				self.caller.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

# Interactive Exit
class interexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "You knock on the door, a small metal slide whips open. What's the password?"
		self.db.answer = "yes"
		self.db.err_traverse = "|/Wrong answer.|/"
	def at_before_move(self, destination):
		self.msg("we got this far.")


# Has Object Exits
class hasobjectmsgexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/Test|/"
		self.db.err_traverse = "|/You cannot go that way|/"
		self.locks.add("traverse:holds(Needed Item)")
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				self.caller.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class hasobjectexit(DefaultExit):
	def at_object_creation(self):
		self.locks.add("traverse:holds(Needed Item)")
		self.db.err_traverse = "|/You are missing something you need.|/"
		self.db.desc = "It's an exit to another place."

# Tag Exits
class tagandcatexit(DefaultExit):
	def at_object_creation(self):
		self.locks.add("traverse:tag(tagname, tagcategory)")
		self.db.err_traverse = "You don't have the right tag."
		self.db.desc = "It's an exit to another place."

class singletagexit(DefaultExit):
	def at_object_creation(self):
		self.locks.add("traverse:tag(tagname)")
		self.db.err_traverse = "You don't have the right tag."
		self.db.desc = "It's an exit to another place."

class mazeexit(DefaultExit):
	def at_object_creation(self):
		self.locks.add("traverse:not tag(youmaynotpass)")
		self.db.err_traverse = "The Rat King steps in front of you blocking your path.|/You may not pass until you |canswer the riddle|n."
		self.db.desc = "It's an exit to another place."

class tagaddexit(DefaultExit):
	def at_object_creation(self):
		self.db.addtag = "test"
	def at_traverse(self, traversing_object, target_location):
		if not traversing_object.tags.get(self.db.addtag):
			traversing_object.tags.add(self.db.addtag)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				self.caller.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class tagremexit(DefaultExit):
	def at_object_creation(self):
		self.db.remtag = "test"
	def at_traverse(self, traversing_object, target_location):
		if traversing_object.tags.get(self.db.remtag):
			traversing_object.tags.remove(self.db.remtag)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				self.caller.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

