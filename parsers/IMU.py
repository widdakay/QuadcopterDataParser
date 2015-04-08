import re, datetime, utils



class IMU:
	regex = re.compile(r'#IMU:(\d+),([-+]?\d+\.\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+),([-+]?\d+)')
	def parse(self, string):
		m = self.regex.match(string)
		if not m:
			return
		millis = int(m.group(1))
		return (millis)

