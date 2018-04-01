####################################### SAND-E Library Modules ########################################
# Purpose: Collect functionality needed to operate SAND-E into a single place
# Includes: Motor driver, get ultrasonic range, get compass heading, get beacon heading
#
# Classes: Motor:
#			 -drive_cw(speed): Drive motor clockwise at a given speed (0-100)
#			 -drive_ccw(speed): Drive motor counter-clocwise at a given speed (0-100)
#			 -delete: Disable motor
#		   Ultrasonic:
#			 -get_range: Returns distance to nearest sensed object
# Methods: 
#		-SANDE_init: import dependencies and set up GPIO pins
#
# Authors: Benjamin Elsaesser (benjamin.elsaesser@colorado.edu)
########################################################################################################

def SANDE_init():
	# Import dependencies
	import RPi.GPIO as io

	# Set up general GPIO stuff
	io.setmode(io.BOARD)
	io.setwarnings(False)
	
# Define a motor class
class Motor:

	def __init__(self, inp1, inp2, enable):
		import RPi.GPIO as io
		# Make pin numbers object variables
		self.in1 = inp1
		self.in2 = inp2
		self.enable = enable

		# Give the motor an identifiable name
		self.name = "motor_" + str(self.in1) + "_" + str(self.in2) + "_" + str(self.enable)

		# Initialize motor pins (here's where you'd check for errors
		print("(Initializing {})".format(self.name))
		
		try:
			io.setup(self.in1, io.OUT)
			io.setup(self.in2, io.OUT)
			io.setup(self.enable, io.OUT)
		
			# Set to use PWM
			self.pwm = io.PWM(self.enable, 100)

			# Start PWM with a 0 duty cycle so it does not run yet
			self.pwm.start(0)

		except:
			print("Error setting up pins of {}".format(self.name))

	def drive_cw(self,speed):
		import RPi.GPIO as io
		# Set the GPIO pins such that the motor turns clockwise
		io.output(self.in1, True)
		io.output(self.in2, False)
		io.output(self.enable, False)

		# Attempt to change motor duty cycle
		try:
			self.pwm.ChangeDutyCycle(speed)
			io.output(self.enable, True)
		except:
			print("Changing speed failed. Make sure the input value is <100")


	def drive_ccw(self,speed):
		import RPi.GPIO as io
		# Set the GPIO pins such that the motor turns clockwise
		io.output(self.in2, True)
		io.output(self.in1, False)
		io.output(self.enable, False)

		# Attempt to change motor duty cycle
		try:
			self.pwm.ChangeDutyCycle(speed)
			io.output(self.enable, True)
		except:
			print("Changing speed failed. Make sure the input value is <100")

	def delete(self):
		import RPi.GPIO as io
		io.output(self.enable, False)
		self.pwm.stop()

class Ultrasonic:

	# Initialize ultrasonic sensor given echo and trig pin numbers
	def __init__(self,echo,trig):
		import RPi.GPIO as io
		import time

		self.echo = echo
		self.trig = trig
		io.setup(self.echo,io.IN)
		io.setup(self.trig,io.OUT)

		io.output(self.trig, False)
		print("Waiting for sensor to Settle")
		time.sleep(2)

	def get_range(self,offset):
		import RPi.GPIO as io
		import time
		
		# Send 10 microsecond pulse to trig pin
		io.output(self.trig, True)
		time.sleep(0.00001)
		io.output(self.trig, False)

		# Time the response
		while io.input(self.echo)==0:
			pulse_start = time.time()

		while io.input(self.echo)==1:
			pulse_end = time.time()

		# Calculate distance
		self.pulse_duration = pulse_end-pulse_start
		self.distance = self.pulse_duration*17150
		self.distance = round(self.distance,2) + offset

		# Return distance
		return (self.distance, self.pulse_duration)

# Get compass heading
def comp_heading():
	from i2clibraries import i2c_hmc5883l
	import time

	# select i2c port
	hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)

	hmc5883l.setContinuousMode()

	# set magnetic declination
	hmc5883l.setDeclination(8,22)

	heading_list = hmc5883l.getHeading()
	minutes = heading_list[1]/60
	heading = heading_list[0] + minutes
	return (heading)
