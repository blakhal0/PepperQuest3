from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class scan(default_cmds.MuxCommand):
	key = "scan"
	auto_help = True
	def func(self):
		macs = ["CC:93:41:B9:CE:96", "FE:E4:49:14:88:FB", "FC:13:8F:25:BB:8F", "D3:99:12:F1:0D:55", "66:9F:E9:AD:5B:0E", "A3:36:EB:5B:EE:5F", "04:01:25:68:BF:79", "82:7E:D7:C8:AF:E9", "A3:48:29:72:E8:30", "D9:89:90:21:29:FF", "1B:7B:A5:44:99:CB", "24:D0:C1:09:A9:23", "95:5B:E4:AF:02:BA", "7F:F0:8B:BB:F9:BB", "AC:54:57:8E:CD:9B", "13:A1:55:CD:5B:DD", "69:86:24:1C:06:05", "E8:3A:5C:57:F0:85", "54:2A:FF:86:80:CA", "4D:64:47:92:FC:C5", "82:C8:24:D7:9F:28", "EA:E7:AA:1F:88:3C", "FD:EE:9A:32:CF:AE", "47:6D:68:54:24:BC", "ED:B6:5F:24:C0:25", "B6:77:51:69:8C:6E", "4C:36:0E:2E:BE:50", "D7:49:87:E3:D6:A2", "70:C0:C2:E0:E1:6E", "09:DB:72:C4:90:D1", "7B:44:1F:79:F3:9C", "57:C4:93:29:CF:43", "10:7B:14:C8:F1:D1", "04:AF:73:BC:A8:03", "B3:C7:21:A4:11:F2", "5B:B4:C8:5C:CF:C3", "27:FD:F0:0A:3D:15", "EB:9F:C8:21:4D:60", "5B:D1:B9:4D:03:A0", "3B:A6:8C:C6:75:54", "E7:52:4B:29:7F:A2", "8E:F9:2A:95:53:CD", "F8:37:D8:BB:00:D4", "C0:E3:F8:58:74:19", "EA:E3:DA:0D:23:40", "CF:BC:F9:0B:9E:E8", "73:0E:81:76:B5:A9", "0A:62:EA:2A:9E:68", "76:40:52:8C:69:AE", "A1:46:6E:F6:95:97"]
		if not self.caller.location.db.scan == "yes":
			list = ""
			list += "%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			self.caller.msg("|/You fire up the scanner.")
			yield 3
			self.caller.msg("|rSweeper 9000 Output|n|/%s" % (list))
			self.caller.msg("|/None of the identified MAC addresses were found nearby.")
			return
		else:
			if self.caller.location.db.scanloc == 1 and self.caller.tags.get("scan1"):
				self.caller.msg("|/You've already scanned this area, move on to another location.")
				return
			if self.caller.location.db.scanloc == 1 and not self.caller.tags.get("scan1"):
				self.caller.tags.add("scan1")
			if self.caller.location.db.scanloc == 2 and self.caller.tags.get("scan2"):
				self.caller.msg("|/You've already scanned this area, move on to another location.")
				return
			if self.caller.location.db.scanloc == 2 and not self.caller.tags.get("scan2"):
				self.caller.tags.add("scan2")
			if self.caller.location.db.scanloc == 3 and self.caller.tags.get("scan3"):
				self.caller.msg("|/You've already scanned this area, move on to another location.")
				return
			if self.caller.location.db.scanloc == 3 and not self.caller.tags.get("scan3"):
				self.caller.tags.add("scan3")
			list = ""
			list += "%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			list += "|/|y00:8C:3F:67:2A:65|n"
			list += "|/%s" % random.choice(macs)
			list += "|/%s" % random.choice(macs)
			self.caller.msg("|/You fire up the scanner.")
			yield 3
			self.caller.msg("|rSweeper 9000 Output|n|/%s" % (list))
			self.caller.msg("|/TARGET MAC ADDRESS FOUND NEARBY.")
			self.caller.db.scanned += 1
			if self.caller.db.scanned == 1:
				self.caller.msg("|/You've found one point, you need two more to triangulate the cartel members location.")
				return
			if self.caller.db.scanned == 2:
				self.caller.msg("|/You've found two points, you need one more to triangulate the cartel members location.")
				return
			if self.caller.db.scanned >= 3:
				self.caller.msg("|/You mark down the three locations on the map, looks like the cartel member is in the park somewhere.")
				self.caller.tags.add("scanned")
				self.caller.msg("You head back to headquarters and return the scanner to Q Branch.")
				for o in self.caller.contents:
					if o.key == "Sweeper 9000":
						o.delete()
				self.caller.tags.remove("scan1")
				self.caller.tags.remove("scan2")
				self.caller.tags.remove("scan3")
				self.caller.db.scanned = 0
				results = search_object("#2920")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.msg("|/|mAlgernop|n says: Ah, you're back, and with hardly a scratch, excellent.")
				return
			return

class ScanCmdSet(CmdSet):
	key = "ScanCmdSet"
	def at_cmdset_creation(self):
		self.add(scan())

class scanner(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Sweeper 9000."
		self.cmdset.add_default(ScanCmdSet, permanent=True)
		self.locks.add("drop:false()")