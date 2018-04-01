# Test if the rover actually drives straight and calculate the speed differential needed to achieve straignt motion

# Initialize GPIO pins and necessary libraries
import robot.py
robot.SANDE_init()

# Define motor objects (will need to use actual pin numbers and uncomment these lines)
#left_motor = robot.Motor(in1, in2, enable)
#right_motor = robot.Motor(in1, in2, enable)

# define list of motor speeds
speeds_left = [10, 20, 30, 40, 50, 60, 70, 100]
speeds_right = speeds_left

# loop through list of speeds
for i in range(len(speeds_left)):
	# test if robot is going straight
	straight = 'n'
	while straight=='n':
		right_motor.drive_cw(speeds_right[i])
		left_motor.drive_ccw(speeds_left[i])
		time.sleep(10)
		right_motor.drive_cw(0)
		left_motor.drive_ccw(0)
		
		# Ask user if bot drove straight, left, or right
		adjust = input("Did SAND-E drive straight, left, or right: ")
		# Loop to next speed if it drove straight
		if adjust=='straight':
			straight='y'

		# Decrease the right motor speed if the bot drove left
		else if adjust=='left':
			speeds_right[i] -= 5

		# Decrease the left motor speed if the bot drove right
		else if adjust=='right':
			speeds_left[i] -= 5

# Print test results
print "Final motor speeds for straight driving"
print "Left Motor: ", speeds_left
print "Right Motor: ", speeds_right

# Disable motors
right_motor.delete()
left_motor.delete()
		
