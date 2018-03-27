# Script to test range of ultrasonic sensors and calculate appropriate offset for each
import robot.py

# Initialize gpio pins and required libraries
robot.SANDE_init()

# Update these with correct pins
#echo = PINNUM
#trig = PINNUM

# Define ultrasonic sensor object
ul = robot.Ultrasonic(echo,trig)

offset = 0
ans = 'n'

while ans=='n':
	# Get range with a given offset until the range is currect
	dist = ul.get_rage(offset)

	# Check if range is correct
	print("Measured distance = {} cm".format(dist))
	ans = input("Is this the correct distance [y/n] ")

	# Update the offset
	if ans=='n':
		real_range = input("What is the correct distance in centimeters: ")
		offset += real_range

# Print final result
print("The final range is {} cm using an offset of {} cm".format(dist,offset))


