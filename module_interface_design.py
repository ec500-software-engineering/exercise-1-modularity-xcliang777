#It's the I/O documentation for the Health_Monitor_system


#Wire Definition

#Input Analyzer
# Input -- Data from sensors.

def Input_Analyzer_get_data():
	"""
	receive data from monitor devices
	Format: ((tuple),int type_of_data)
	integer type_of_data represent the source of the data.(blood oxygen or pressure or else)
	(tuple) defines the data we get from sensors
	"""

#Storage System
def Storage_sys_get_data((data_pakage),type_of_data):
	"""
	Save the data_pakage into three different table according to type_of_data
	Format: 
	type_of_data:
		blood oxygen: (double percent,time time)
		blood presure: (double pressure,time time)
		pulse: (double frequency, time time)
	"""

#AI Module
def AI_module_input(bo,bp,pul)：
	"""
	bo,bp,pul are three lists represent the value of blood oxygen,blood pressure and pulse
	bo,bp,pul: list [double value]
	"""

def AI_module_output():
	"""
	output format:
		a double value for estimated health score
	"""

#User Interface
def get_data():
	"""
	Get_data_from alert sys
		format: three flags to trigger alert display

	Get_data_from_data_base:
		format:double values to display on screen
	"""

#Alert Sys
def Alert_input():
	"""
	get data for each type from database.
	format:
		(double value,int type)
	"""

def Alert_Output():
	"""
	Compare data with certain threthold
	send flags to user interface module.
	"""
