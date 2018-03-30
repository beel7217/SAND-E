# Move straight -> avoid obstacle -> move straight
import robot.py

def init():
	# Initialize SAND-E
	robot.SANDE_init()
	
	# Initialize motors (Will need to add actual pin numbers and uncomment)
	left_motor = robot.Motor(in1, in2, enable)
	right_motor = robot.Motor(in1, in2, enable)

	# Initialize Ultrasonic sensors (Will need to add actual pin numbers and uncomment)
	left_ul = robot.Ultrasonic(echo, trig)
	right_ul = robot.Ultrasonic(echo, trig)


def drive_straight():
	while (left_range > 20 and right_range > 20):
		# Drive straight for 0.1 seconds
		left_motor.drive_ccw(40)
		right_motor.drive_cw(40)
		time.sleep(0.1)

		# Check ultrasonic sensors
		left_range = left_ul.get_range()
		right_range = right_ul.get_range()

	if (left_range < 20 and right_range < 20):
		return 'both'
	else if left_range < 20:
		return 'left'
	else if right_range < 20:
		return 'right'
	else:
		return 'wrong'


def avoid_obs(direction):
	
