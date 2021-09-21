from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class sentence(default_cmds.MuxCommand):
	key = "talk judge"
	aliases = ["Talk Judge", "talk Judge", "Talk judge"]
	auto_help = True
	def func(self):
		if not self.caller.search("Prison Wallet", location=self.caller, quiet=True):
			wallet_proto = {
			"key": "Prison Wallet",
			"typeclass": "typeclasses.wallet.wallet",
			"location": self.caller
			}
			spawn(wallet_proto)
		if self.caller.tags.get("caught"):
			crime = "Felony possession of an outlawed substance with intent to distribute."
		if self.caller.tags.get("gotawayclean"):
			crime = "Misdemeanor association with deviants, Felony occupying a residence used in commission of a crime, and Felony assumed destruction of evidence."
		self.caller.msg("|mJudge|n says: %s, you stand assumed guilty of: %s" % (self.caller.key, crime))
		answer = yield("|mJudge|n says: How do your plead? Guilty or Not Guilty?")
		if answer.lower() in ["guilty"]:
			self.caller.msg("|/|mJudge|n says: %s has plead Guilty.|/|mJudge|n says: The court has determined that a sentence of 67 years, without the chance of parole, and a fine of $1.2 million is appropriate and proportional to the crimes committed." % (self.caller.key))
			self.caller.msg("|mJudge|n says: %s is to be transferred to the Ultra Max section of the prison immediately." % (self.caller.key))
			self.caller.msg("Eyes wide and jaw on the floor you attempt to sputter a protest as a black bag is pulled over your head and blow lands in your ribs.")
			yield 8
			self.caller.msg("You kick and struggle as you're drug down a seemingly endless amount of hallways, up and down stairs, finally you hear a cell door open and you're thrown in.|/The relief of the shackles and chains coming off is short lived as a booted foot slams into your back.")
			results = search_object("#292")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif answer.lower() in ["not guilty"]:
			self.caller.msg("|/|mJudge|n says: %s has plead Not Guilty, which is a lie. Based on the evidence provided, the court finds you Guilty.|/|mJudge|n says: The court has determined that a sentence of 67 years, without the chance of parole, and a fine of $1.2 million is appropriate and proportional to the crimes committed." % (self.caller.key))
			self.caller.msg("|mJudge|n says: %s is to be transferred to the Ultra Max section of the prison immediately." % (self.caller.key))
			self.caller.msg("Eyes wide and jaw on the floor you attempt to sputter a protest as a black bag is pulled over your head and blow lands in your ribs.")
			yield 8
			self.caller.msg("You kick and struggle as you're drug down a seemingly endless amount of hallways, up and down stairs, finally you hear a cell door open and you're thrown in.|/The relief of the shackles and chains coming off is short lived as a booted foot slams into your back.")
			results = search_object("#292")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/|mJudge|n roars: LISTEN HERE, YOUR BULLSHIT WILL NOT BE TOLERATED!! BAILIFF, ENCOURAGE %s TO SHOW PROPER RESPECT TO THE COURT!!" % (self.caller.key.upper()))
			yield 5
			self.caller.msg("The bailiff grabs you by the shirt, you double over and gasp in pain as the punch lands hard in your ribs.")
			self.caller.msg("|mJudge|n says: Now, lets try this again.")
			return

class JudgeCmdSet(CmdSet):
	key = "JudgeCmdSet"
	def at_cmdset_creation(self):
		self.add(sentence())
	
class judge(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A figure sits, hooded and robed in white, on a dais staring at you."
		self.cmdset.add_default(JudgeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "The death sentence is NOT off the table...."