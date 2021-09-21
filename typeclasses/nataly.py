from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk nataly"
	aliases = ["Talk Nataly", "Talk nataly", "talk Nataly"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("natalydone") or not self.caller.db.faction == "fed":
			self.caller.msg("There's no one here by that name to talk to.")
			return
		else:
			if self.caller.tags.get("rumbledone"):
				self.caller.msg("|/|mNataly|n says: Ah, you got our property back. Good work.")
				for o in self.caller.contents:
					if o.key == "Debt Book":
						o.delete()
				self.caller.msg("|mNataly|n says: Now we can get our gambling operations and debt collections back up and running.")
				self.caller.db.cartel = "vipers"
				self.caller.msg("|mNataly|n says: You're now officially a member of the Naga Vipers. There's a couple things you need to know.")
				self.caller.msg("|mNataly|n says: On the second floor of the cell block you need to stay on the west side, that's our turf, the Ghost Reapers don't take kindly to our people wandering around on their side and are likely to give you a boot party if they don't just outright kill you if you go over there.")
				self.caller.msg("|mNataly|n says: We run the kitchen, you're allowed in there now.")
				self.caller.msg("|mNataly|n says: You're allowed to enter the cells of other Naga Vipers members, but don't try and pull anything. We don't tolerate thieves.")
				self.caller.msg("|mNataly|n says: Welcome to the crew. Your life expectancy just doubled.")
				self.caller.msg("|mNataly|n says: See you around.")
				self.caller.msg("Nataly casually gets up and heads out of the dayroom.")
				self.caller.msg("|mNataly|n says: Hey, since you're not busy, go to the kitchen and pick up the boss's food.")
				self.caller.tags.remove("rumbledone")
				self.caller.tags.remove("gracedone")
				self.caller.tags.add("natalydone")
				return
			elif self.caller.tags.get("rumble"):
				self.caller.msg("|/|mNataly|n says: What are you waiting for, go find Pierre in the yard and get our property back.")
				return
			elif self.caller.tags.get("shoplifting"):
				if self.caller.tags.get("handle") and self.caller.tags.get("metal"):
					self.caller.msg("|/|mNataly|n says: Excellent, you've gotten everything.")
					self.caller.msg("Nataly does some quick work fashioning brass knuckles.")
					knuckles_proto = {
					"key": "Brass Knuckles",
					"typeclass": "typeclasses.objects.DefaultObject",
					"desc": "A crudely made set of brass knuckles.",
					"location": self.caller
					}
					spawn(knuckles_proto)
					self.caller.msg("Nataly hands you the brass knuckles.")
					self.caller.msg("|mNataly|n says: Go retrieve our property, you pull this off and you're as good as in.")
					self.caller.tags.remove("shoplifting")
					self.caller.tags.remove("handle")
					self.caller.tags.remove("metal")
					self.caller.tags.remove("bin")
					for o in self.caller.contents:
						if o.key == "Handle" or o.key == "Metal":
							o.delete()
					self.caller.tags.add("rumble")
					return
				if not self.caller.tags.get("handle") and not self.caller.tags.get("metal"):
					self.caller.msg("|/|mNataly|n says: What are you waiting for, head to the workshop and see if you can find a piece of metal and a handle.")
					return
				if self.caller.tags.get("handle") and not self.caller.tags.get("metal"):
					self.caller.msg("|/|mNataly|n says: Well, you're half way there, go find a piece of metal.")
					return
				if not self.caller.tags.get("handle") and self.caller.tags.get("metal"):
					self.caller.msg("|/|mNataly|n says: Well, you're half way there, go find a handle.")
					return
			else:
				self.caller.msg("|/|mNataly|n says: We like the way you handled yourself in the cafeteria. We appreciate an aggressive mindset.")
				self.caller.msg("Nataly flashes her arm tattoo of a snake with a pepper in its mouth.")
				self.caller.msg("|mNataly|n says: Look here, no one leaves this place alive, and if you want to stay alive long enough to die, you're going to want someone watching your back.")
				self.caller.msg("|mNataly|n says: I've been authorized to extend an invitation to apply for membership in our crew, the Naga Vipers.")
				self.caller.msg("|mNataly|n says: What do you say?")
				answer = yield("Yes or no?")
				if answer.lower() in ["yes", "y"]:
					self.caller.msg("|/|mNataly|n says: Great choice, now it's not just as simple as saying yes and you're in, you gotta prove yourself.")
					self.caller.msg("|mNataly|n says: There's a, shall we say, issue that needs to be handled. You're going to handle it.")
					self.caller.msg("|mNataly|n says: One of the Ghost Reapers took something that belongs to us, you know how to play fetch right?")
					self.caller.msg("|mNataly|n says: His name is Pierre, and he spends most of his time in the yard. You're no match for him straight up, you're going to need something to encourage compliance, if you get my drift.")
					self.caller.msg("|mNataly|n says: Look around in the workshop, it's just a bit to the north of here, and see if you can't find a piece of metal and a handle and bring them back to me and I'll work my magic.")
					self.caller.tags.add("shoplifting")
					return
				elif answer.lower() in ["no", "n"]:
					self.caller.msg("|/|mNataly|n says: I'm not sure you've really thought through the offer in front of you. I'll let you reconsider for a minute...")
					return
				else:
					self.caller.msg("|/|mNataly|n says: What? Was that even english? Yes or no, is that too hard for you to figure out?")
					return

class NatalyCmdSet(CmdSet):
	key = "NatalyCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class nataly(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Nataly is watching TV, occasionally an inmate will approach and whisper something and hands over some stamps. Nataly clicks her tongue twice and another member of the Naga Vipers approaches and hands something to the buyer."
		self.cmdset.add_default(NatalyCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(dayroom) and tag(gracedone) and not attrib(cartel, vipers) and attrib(faction, fed)")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/Nataly spits out a razor blade and slices your hand.|/|mNataly|n says: Keep your hands to yourself if you want to keep them."