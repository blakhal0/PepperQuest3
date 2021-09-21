from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk minister"
	aliases = ["Talk Minister", "Talk minister", "talk Minister"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mMinister|n says: Welcome to our humble church of the bland. Please |cAttend Service|n with us this ok and mundane day.")

class confess(default_cmds.MuxCommand):
	key = "confess"
	aliases = ["Confess"]
	auto_help = False
	def func(self):
		if self.caller.tags.get("acolyte"):
			self.caller.msg("|/|mMinister|n says: I have shared all the knowledge I have to share. I know nothing more.")
			return
		if self.caller.tags.get("apostle"):
			self.caller.msg("|/|mMinister|n whispers: You are an apostle of the Great Hot Ones?")
			self.caller.msg("|mMinister|n says: By the commands of the Order of the Burning Ring I shall pass to you the knowledge that has been passed to me.")
			self.caller.msg("|mMinister|n says: This prison was built on top of an ancient ceremonial location, when the grounds were being excavated a book was discovered.")
			self.caller.msg("|mMinister|n says: The Spiceronomicon.")
			self.caller.msg("|mMinister|n says: I have searched for years, but never located it.")
			self.caller.msg("|mMinister|n says: Whispers rise up occasionally, the book is still here, somewhere.")
			self.caller.msg("|mMinister|n says: It is said with that book and the sacred seeds one can bring forth the return.")
			self.caller.msg("|mMinister|n says: That is all that I know and now that it has been said, I will not say it again.")
			self.caller.msg("|mMinister|n says: With this knowledge, you have attained the rank of Acolyte in the Order of the Burning Ring.")
			self.caller.tags.remove("apostle")
			self.caller.tags.add("acolyte")
			return

class service(default_cmds.MuxCommand):
	key = "attend service"
	aliases = ["Attend Service", "Attend service", "attend Service"]
	auto_help = True
	def func(self):
		self.caller.msg("|/As inmates file in and take their seats, the service begins.")
		self.caller.msg("|mMinister|n says: And now, this weeks sermon is from our beloved the Reverend Cleophis James.")
		self.caller.msg("|mReverend James|n says: And now people. And now people. When I woke up this morning, I heard a disturbing sound.")
		self.caller.msg("|mReverend James|n says: I said, when I woke up this morning I heard a disturbing sound.")
		self.caller.msg("Someone from the back hollers 'What was that sound?'")
		self.caller.msg("|mReverend James|n says: What I heard was the jingle-jangle of a thousand lost souls.")
		self.caller.msg("|mReverend James|n says: And I'm talking about the souls of all the men and women, swept into hell by that demon SPICE!!")
		self.caller.msg("|mReverend James|n says: Because it's too late... Too late yeah, too late for them to ever see again, the light they once chose not to follow.")
		self.caller.msg("|mReverend James|n says: Don't be lost when the time comes. Say NO to that devil, and stay in the light.")
		self.caller.msg("Suddenly a beam of light shines through the iron bar covered window and lands on Joliet Jake.")
		self.caller.msg("|mReverend James|n says: Do you SEE THE LIGHT?")
		self.caller.msg("|mElwood Blues|n says: What light?")
		self.caller.msg("|mReverend James|n says: Have you SEEN THE LIGHT!!")
		self.caller.msg("|mJoliet Jake|n says: Yes! YES! Sweet tapdancing tadpoles, YES, I'VE SEEN THE DAMNED LIGHT ALREADY!")
		self.caller.msg("Joliet Jake begins doing cartwheels down the center aisle.")
		self.caller.msg("|mGuard|n says: HEY!! CALM IT DOWN IN THERE DAMMIT! Reverend James, we've warned you about getting these assholes all riled up.")
		self.caller.msg("Guards swarm into the chapel and begin cracking heads.")
		self.caller.msg("The service has ended.")
		return

class MinisterCmdSet(CmdSet):
	key = "MinisterCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
		self.add(confess())
		self.add(service())

class minister(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "."
		self.cmdset.add_default(MinisterCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/|mMinister|n says: Please do not wrinkle my robes or I shall pray for a smiting upon you."