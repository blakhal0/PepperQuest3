from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chat(default_cmds.MuxCommand):
	key = "talk agent"
	aliases = ["Talk Agent", "Talk agent", "talk Agent", "talk agent"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You pull out the chair across from the agent and sit down.")
		self.caller.msg("You look her in the eyes and she gives you a lethal stare.")
		self.caller.msg("|mAgent Orxata|n says: Hello inmate %s, how are you enjoying your complimentary stay at the old grey bar hotel?" % (self.caller.key))
		self.caller.msg("|mAgent Orxata|n says: Not that you don't have the free time, but I'll get straight to business.")
		self.caller.msg("Agent Orxata pokes the file folder hard and stares at you intently.")
		self.caller.msg("|mAgent Orxata|n says: You are never leaving this facility alive, 67 years is a long time, and even if you managed live that long, which you won't, you'd be destitute.")
		self.caller.msg("|m%s|n says: So let me guess, this is where I tell you everything I know about everyone I know and maybe I get out of here right? That's how it works right?" % (self.caller.key))
		self.caller.msg("|mAgent Orxata|n says: No, this is where I tell you that we have an open position in the agency that's perfect for someone of your, shall we say, qualifications.")
		self.caller.msg("|m%s|n says: Qualifications like tech savvy, smart, and good at getting into places?" % (self.caller.key))
		self.caller.msg("|mAgent Orxata|n says: No, qualifications like being completely screwed and expendable.")
		self.caller.msg("|mAgent Orxata|n says: So here's your choices, stay in here and eventually get violently murdered by one of the cartels, or work for us and maybe get to the other side of this entire mess one day.")
		self.caller.msg("|mAgent Orxata|n says: So, what's it going to be?")
		answer = yield("Take the offer from the feds? (yes, no, think on it)")
		if answer.lower() in ["yes", "y"]:
			self.caller.db.faction = "fed"
			if self.caller.tags.get("reaperinvite"):
				self.caller.tags.remove("reaperinvite")
			self.caller.msg("|/|mAgent Orxata|n says: Well, it appears you're a lot smarter than I anticipated. There might be hope for you yet.")
			self.caller.msg("Agent Orxata looks towards the camera and nods, the blinking red light shuts off.")
			self.caller.msg("|mAgent Orxata|n says: Now that we have some privacy...")
			self.caller.msg("Agent Orxata opens the file folder and spins it to face you.")
			self.caller.msg("|mAgent Orxata|n says: The dealer you got the peppers from, he's a low level street distributor and part of the Faucheurs Fantomes, or Ghost Reapers, pepper cartel operating out of Quebec.")
			self.caller.msg("|mAgent Orxata|n says: We've been trying to infiltrate the cartel but they are a very close nit crew and every operative we've sent has disappeared.")
			self.caller.msg("|mAgent Orxata|n says: Since then we've shifted our focus to infiltration of the Naga Vipers, the second most powerful cartel and direct rival of the Ghost Reapers.|/They've been our best source of info on the Ghost Reapers.")
			self.caller.msg("|mAgent Orxata|n says: One of our agents has been embedded here in this facility and has worked their way up the chain of command and is now a shot caller.")
			self.caller.msg("|mAgent Orxata|n says: The problem is that the handler for that agent was kidnapped and killed last week and we can't decrypt the files to find the agents identity.")
			self.caller.msg("|mAgent Orxata|n says: We need you to gain the trust of the Naga Vipers, infiltrate their organization, find our operative, and get the information they've gathered out of here.")
			self.caller.msg("|mAgent Orxata|n says: Needless to say, after today we can't exactly just call you in to debrief, unless you want to be bled out in the showers.")
			self.caller.msg("|mAgent Orxata|n says: We'll help out when and where we can without blowing your cover, but you're going to be on your own for the most part.")
			self.caller.msg("|mAgent Orxata|n says: Their gang colors are red and black, they run the kitchen, respect shows of aggression, and their leader goes by the street name 'Atropos'.")
			self.caller.msg("|mAgent Orxata|n says: Welcome to the National Spice Agency. Get out there and make the country proud.")
			self.caller.msg("|mAgent Orxata|n says: Oh yeah, one last thing I forgot to mention...")
			self.caller.msg("Agent Orxata slams a fist on the door 3 times, the light on the camera starts to blink again.")
			self.caller.msg("|mAgent Orxata|n says: ALRIGHT ASSHOLE, YOU WANNA BE TOUGH, WE'LL SEE HOW TOUGH YOU ARE AFTER A WEEK IN THE HOLE. YOU SHOULDA TOOK THE OFFER.")
			self.caller.msg("The door opens and a slew of guards come in and start beating you.")
			self.caller.msg("|mAgent Orxata|n whispers: Sorry, but we gotta sell your cover. Have fun.")
			results = search_object("#398")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.tags.remove("interview")
			return
		else:
			self.caller.msg("|/|mAgent Orxata|n says: Okay wise ass, maybe you like it here at club fed.|/If you decide to get a brain cell talk to the guard outside your cell and come see me, but be aware this offer has an expiration date")
			self.caller.tags.remove("interview")
			self.caller.msg("Agent Orxata looks at the camera 'We're done here, the inmate can leave now.' The door buzzes and opens.")
			return

class IntAgeCmdSet(CmdSet):
	key = "IntAgeCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())
	
class interrogationagent(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A woman in a midrange pant suit sits at the table tapping a thick file folder, eying you with hostility.|/'Have a seat inmate, today's your lucky day if you have half a brain.'"
		self.cmdset.add_default(IntAgeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "The agent stands up, puts you in an arm bar, and slams your head off the table."