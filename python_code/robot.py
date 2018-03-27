####################################### SAND-E Library Modules ########################################
# Purpose: Collect functionality needed to operate SAND-E into a single place
# Includes: Motor driver, get ultrasonic range, get compass heading, get beacon heading
#
# Authors: Benjamin Elsaesser (benjamin.elsaesser@colorado.edu)
########################################################################################################

def SANDE_init():
	# Import dependencies
	import RPi.GPIO as io
	from time import sleep

	# Set up general GPIO stuff
	io.setmode(GPIO.BOARD)
	io.setwarnings(False)
	
# Define a motor class
class Motor:

	def __init__(self, in1, in2, enable):
		# Make pin numbers object variables
		self.in1 = inp1
		self.in2 = inp2
		self.enable = enable

		# Give the motor an identifiable name
		self.name = "motor_" + string(self.in1) + "_" + string(self.in2) + "_" + string(self.enable)

		# Initialize motor pins (here's where you'd check ofor errors
		print("(Initializeing {})".format(self.name))
		
		try:
			io.setup(self.in1, io.OUT)
			io.setup(self.in2, io.OUT)
			io.setup(self.enable, io.OUT)
		
			# Set to use PWM
			self.pwm = io.pwm(self.enable, 100)

			# Start PWM with a 0 duty cycle so it does not run yet
			self.pwm.start(0)

		except:
			print("Error setting up pins of {}".format(self.name))

	def drive_cw(self,speed):
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
		io.output(self.enable, False)
		self.pwm.stop()

