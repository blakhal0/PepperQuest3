from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chat(default_cmds.MuxCommand):
	key = "talk algernop"
	aliases = ["Talk Algernop", "Talk algernop", "talk Algernop" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("qscan"):
			self.caller.msg("|/|mAlgernop|n says: Hello Agent %s." % (self.caller.key))
			self.caller.msg("|mAlgernop|n says: We've got the Sweeper 9000 all loaded up and ready for you.")
			self.caller.msg("|mAlgernop|n says: It's hand held, discrete, simple to use, and runs forever due to the miniature nuclear battery.")
			self.caller.msg("|mAlgernop|n says: I'd keep it a good distance from any vital organs you're fond of.")
			scan_proto = {
			"key": "Sweeper 9000",
			"typeclass": "typeclasses.scan.scanner",
			"location": self.caller
			}
			spawn(scan_proto)
			self.caller.tags.remove("qscan")
			self.caller.msg("Algernop hands you the Sweeper 9000")
			self.caller.msg("|mAlgernop|n says: All you have to do is |cScan|n and if an identified device is near it'll tell you. You need to find the device from three locations to be able to triangulate it.")
			self.caller.msg("|mAlgernop|n says: Please do bring the equipment back in pristine condition. Good Luck.")
			return
		if self.caller.tags.get("earwig"):
			self.caller.msg("|/|mAlgernop|n says: Hello Agent %s." % (self.caller.key))
			self.caller.msg("|mAlgernop|n says: Go ahead and have a seat right over here. Yeah, that's it. Right there.")
			self.caller.msg("A series of metal clamps snap shut around your arms, legs, chest, and head.")
			self.caller.msg("|m%s|n says: HEY!! What the hell is this??!!?! LET ME OUT OF THIS CHAIR!!" % (self.caller.key))
			self.caller.msg("|mAlgernop|n says: Hey buddy, just relax, the restraints are just there to make sure you don't twitch during the installation process.")
			self.caller.msg("|m%s|n says: What do you mean INSTALLATION PROCESS?" % (self.caller.key))
			self.caller.msg("|mAlgernop|n says: Ooooh, you're going to want to keep that heart rate down. It'll be over in a minute.")
			self.caller.msg("Algernop rolls over something that looks like a gigantic laser syringe and lines it up right behind your ear.")
			self.caller.msg("You hear a high pitched electrical noise then a jolt of pain.")
			self.caller.msg("|mAlgernop|n says: See that wasn't so bad. Now if I could just get the uninstallation process to cause a litttle teeny bit less brain damage...")
			self.caller.msg("|mAlgernop|n says: There you go, state of the art transducer based audio sending and receiving, you'll barely know it's there.")
			self.caller.msg("|mAlgernop|n says: Just say |cTango Acquired|n and the name of the target and E.D. Lowe's team will extract them.")
			scan_proto = {
			"key": "TBASR",
			"typeclass": "typeclasses.earwig.earwig",
			"location": self.caller
			}
			spawn(scan_proto)
			self.caller.tags.remove("earwig")
			return
		self.caller.msg("|/|mAlgernop|n says: Hello Agent %s, I haven't gotten any requests to ready equipment for you. I can't just hand things out, there's dangerous things in here you know." % (self.caller.key))
		return

class AlgernopCmdSet(CmdSet):
	key = "AlgernopCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class algernop(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Algernop is busy fiddling with a large sci-fi looking table mounted cannon."
		self.cmdset.add_default(AlgernopCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.nostunmsg = "|/|mAlgernop|n says: Oh, you want to play? I assume you're familiar with 'The Brown Note'.|/Algernop flips a switch on the device on the table and you instantly crap your pants."
		self.db.get_err_msg = "|/|mAlgernop|n says: You have no idea the amount I could get selling you piece by piece on the black market, or at the deli."
