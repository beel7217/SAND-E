Hello! You've just stumbled upon the codebase for CUSEDs' 2018 Rover Challenge entry, SAND-E

If you have any questions feel free to shoot me an email at benjamin.elsaesser@colorado.edu

=============Included in repo=============
-python_code/
	-dev/: Development folder
		-simple_avoid_obstacle.py: Simple algorithm for avoiding an obstacle without an input heading
	
	-component_testing/: Code to use for component testing
		-robot.py: Library file that contains nescessary classes and methods to operate SAND-E hardware:
			-Motors
			-Ultrasonic Sensors
			-Compass (In works)
			-XBee (In works)
		-ul_test.py: Work with user to calculate the offset for each ultrasonic sensor
		-drive_straight_test.py: Drive SAND-E straight at varying speeds and check if a speed offset is 
								 required between the two motors

=========================================
