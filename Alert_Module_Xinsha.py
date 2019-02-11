#It's the I/O documentation for Alert System

#Alert Sys
class alert:
	def __init__():
		self.fine_turn = 0
		self.bo_flag = 0
		self.bp_flag = 0
		self.pul _flag = 0

	def get_bo_data(data):
		if self.fine_turn > 20:
			self.bo_flag = 0

		if exceed(data):
			self.bo_flag += 1
		else:
			self.fine_turn += 1

	def get_bp_data(data):
		if self.fine_turn > 20:
			self.bp_flag = 0
		if exceed(data):
			self.bp_flag += 1
		else:
			self.fine_turn += 1 

	def get_pul_data(data):
		if self.fine_turn > 20:
			self.pul_flag = 0

		if exceed(data):
			self.pul_flag += 1
		else:
			self.fine_turn += 1


	def Alert_Output():
		"""
		Compare data with certain threthold
		send flags to user interface module.
		"""
		if self.bo_flag != 0:
			return 1
		elif self.bp_flag != 0:
			return 2
		elif self.pul_flag != 0:
			return 3
		else:
			return 0