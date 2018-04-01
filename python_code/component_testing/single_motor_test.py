import robot
robot.SANDE_init()

m1 = robot.Motor(16, 18, 12)

m1.drive_cw(10)

time.sleep(10)

m1.drive_cw(0)
