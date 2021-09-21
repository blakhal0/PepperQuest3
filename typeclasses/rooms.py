"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from random import randint


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    pass

class vroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "A normal room"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class morsedash(vroom):
	def at_object_creation(self):
		self.db.desc = "You are in a plain white room. On the wall in front of you is a glowing sign in the shape of a lengthwise rectangle.|/Below the sign is a button."

class morsedot(vroom):
	def at_object_creation(self):
		self.db.desc = "You are in a plain white room. On the wall in front of you is a glowing sign in the shape of a circle.|/Below the sign is a button."

class morseblank(vroom):
	def at_object_creation(self):
		self.db.desc = "You are in a plain white room. Unlike the other rooms, there is no button here, this appears to be nothing but a hallway."

class sewer(vroom):
	def at_object_creation(self):
		self.db.desc = "The sewer is dark, feet slipping and sliding in the sludge as you make your way in the gloom.|/Your eyes, finally adjusted to the dark, take in what appears to be a brick semi-circular roof and walls.|/Occasionally dust and dirt sprinkle down onto your head from the ancient bricks."

class highsewer(vroom):
	def at_object_creation(self):
		self.db.desc = "The higher section of the sewer is drier, but just as dark.|/Your vision has become attuned to the dark, drag marks and tracks are pressed into the muck.|/Based on their size, you're confident there's nothing to worry about.|/The brick semi-circular roof and walls are different somehow, they don't seem newer, just maintained."

class warren(vroom):
	def at_object_creation(self):
		self.db.desc = "The rat warren is very cramped, you're forced to squirm and wriggle through the narrow passages.|/The occasional feeling of fur quickly brushing against you as the rats scurry past has your skin crawling."

class thallway(vroom):
	def at_object_creation(self):
		self.db.desc = "Golden braziers provide ample light in the hallway. The light dances and flickers on the polished stone walls and floors, illuminating an undecipherable script carved into the walls."

class droom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "A normal room"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class street(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You're on Grove Street / Telegraph Avenue / Shady Lane which runs East - West / North - South|/|/The neighborhood is alive with the sounds of the city.|/You can hear children running through the yards and alleys, screeching and laughing as they play their games.|/Neighbors are gathered in small groups, in whatever shade they can find, playing cards or chess and passing the time with idle chatter.|/The apartment buildings and town houses block the view of the rest of the city making you feel almost trapped if not for the fact that this is home."
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class singleplayerroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "A normal room"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class tagroom(DefaultRoom):
	def at_object_creation(self):
		self.db.initdesc = "initial desc"
		self.db.desc = "normal desc"
		self.db.tagname = ""
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.desc
		if not looker.tags.get(self.db.tagname):
			desc = self.db.initdesc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class factionroom(DefaultRoom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "A fed room"
		self.db.desccartel = "A cartel room"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.faction == "none":
			desc = self.db.descnone
		if looker.db.faction == "fed":
			desc = self.db.descfed
		if looker.db.faction == "cartel":
			desc = self.db.desccartel
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class factionsingleplayerroom(DefaultRoom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "A fed room"
		self.db.desccartel = "A cartel room"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.faction == "none":
			desc = self.db.descnone
		if looker.db.faction == "fed":
			desc = self.db.descfed
		if looker.db.faction == "cartel":
			desc = self.db.desccartel
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class nsahallway(vroom):
	def at_object_creation(self):
		self.db.desc = "Your steps echo down the sterile white hallway.|/The dull glare of overhead florescent lights making the marble floor shine."

class cubefarm(vroom):
	def at_object_creation(self):
		self.db.desc = "The cubicle farm surrounds a glass walled meeting room.|/Various agents are hard at work at their desks, typing in searches, analyzing data, creating case files, looking at all the nudes people have sent their significant other, and random strangers.|/Various motivational posters and regulatory guidelines are posted on the cube walls."

class grafactionroom(DefaultRoom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "A fed room"
		self.db.desccartel = "|/A cartel room"
		self.db.desccartelus = "|g           ██████████|n          |r████|/|g       ████|[w          ████|n     |r███ ██|/|g     ██|[w                  ██|n  |r██ ██ ██|/|g   ██|[w                      ███|n   |r██ ██|/|g   ██|[w                      ██|n     |r██ ██|/|g ██|[w    |x████|[w    |x████|[w          ██|n    |r███|/|g ██|[w  |x██████|[w    |x██████|[w        ██|n     |r██|/|g ██|[w  |x██████|[w    |x██████|[w        ██|n    |r██|/|g ██|[w  |x████|[w        |x████|[w        ██|/|g ██|[w                          |g██|/|g ██|[w        |x████|[w      |x████|[w    ██|/|g   ██|[w      |x████|[w    |x██|[w        ██|/|g     ██|[w            |x██|[w  |x██|[w      ██|/|g       ████|[w        |x████|[w          ██|/|g     |r██|g    ██████|[w              ██|/|g    |r██|g            ██████████████|n"
		self.db.desccartelthem = "|r                     __|/|r       ---_ ...... _/_ -|/|r      /  .      ./ .'*\ \|/|r      : '         /__-'   \.|/|r     /                      )|/|r   _/                  >   .'|/|r /   .   .       _.-\" /  .'|/|r \           __/\"     /.'/|||/|r   \ '--  .-\" /     //' ||\|||/|r    \||  \ || /     //_ _ ||/|||/|r     `.  \:     //||_ _ _||\|||/|r     || \/.    //  || _ _ ||/|||/|r      \_ || \/ /    \ _ _ \\\|/|r          \__/      \ _ _ \||\|n"
		self.db.graffitinum = "#tagged"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.faction == "none":
			desc = self.db.descnone
		if looker.db.faction == "fed":
			desc = self.db.descfed
		if looker.db.faction == "cartel":
			if self.db.graffitinum == looker.tags.get(self.db.graffitinum):
				desc = self.db.desccartelus
				desc += self.db.desccartel
			else:
				desc = self.db.desccartelthem
				desc += self.db.desccartel
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class peluca(factionroom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "You are in the Peluca Alley.|/The roar of traffic from the overpass echo's off the buildings in the dark cramped alley."
		self.db.desccartel = "You are in the Peluca Alley.|/The roar of traffic from the overpass echo's off the buildings in the dark cramped alley."

class florida(factionroom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "You are on Florida Ave, which runs East and West.|/Bustling streets lined with parked cars and business people criss cross the capitol area.|/Flags adorning every possible location shift lazily in the slow breeze.|/Surveillance cameras take in every movement, providing you with a wealth of data back at HQ."
		self.db.desccartel = "You are on Florida Ave, which runs East and West.|/Bustling streets lined with parked cars and business people criss cross the capitol area.|/Flags adorning every possible location shift lazily in the slow breeze.|/Surveillance cameras take in your every movement, always watching."

class sixteenth(factionroom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "You are on 16th St, which runs North and South.|/Traffic struggles past, stopping and starting with each cycle of the lights.|/The cameras catch every license plate, record every face, and measure every speed, feeding the data beast."
		self.db.desccartel = "You are on 16th St, which runs North and South.|/Traffic struggles past, stopping and starting with each cycle of the lights.|/Pedestrians play the ultimate game of frogger attempting to get to their next meeting."

class fourteenth(factionroom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "You are on 14th St, which runs North and South.|/Traffic struggles past, stopping and starting with each cycle of the lights.|/The cameras catch every license plate, record every face, and measure every speed, feeding the data beast."
		self.db.desccartel = "You are on 14th St, which runs North and South.|/Traffic struggles past, stopping and starting with each cycle of the lights.|/Pedestrians play the ultimate game of frogger attempting to get to their next meeting."

class belmont(factionroom):
	def at_object_creation(self):
		self.db.descnone = "Something has gone horribly wrong if you're seeing this. Contact blahal0."
		self.db.descfed = "You are on Belmont Way, which runs East and West.|/Large stone buildings, some blazoned with marketing others suspiciously overly nondescript, line the road on each side."
		self.db.desccartel = "You are on Belmont Way, which runs East and West.|/Large stone buildings, some blazoned with marketing others suspiciously overly nondescript, line the road on each side."

class mazeguardroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "The higher section of the sewer is drier, but just as dark.|/Your vision has become attuned to the dark, drag marks and tracks are pressed into the muck.|/Based on their size, you're confident there's nothing to worry about.|/The brick semi-circular roof and walls are different somehow, they don't seem newer, just maintained."
		self.db.gdesc = "|/The Rat King stands before you, his army of tiny henchmen blocking your path.|/You must |canswer the riddle|n to pass."
	def at_object_receive(self, character, source_location):
		chance = randint(1, 3)
		if chance == 2:
			character.tags.add("youmaynotpass")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.has_account:
				users.append(key)
			elif con.tags.get("talkative", category="npc"):
				npc.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		# get description, build string
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get("youmaynotpass"):
			desc = self.db.gdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou look around and see:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string