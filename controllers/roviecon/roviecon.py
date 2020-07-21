"""roviecon controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor

TIME_STEP = int(64)
NUM_WHEELS = 4
NUM_DS = 2
WHEEL_SPEED = -1.5

# create the Robot instance.
robot = Robot()

dsens = []
wheel = []

dsName = ['ds_left', 'ds_right']
wheelName = ['wheel_fl', 'wheel_fr', 'wheel_rl', 'wheel_rr']

for i in range(NUM_DS):
    dsens.append(robot.getDistanceSensor(dsName[i]))
    dsens[i].enable(TIME_STEP)
    
for i in range(NUM_WHEELS):
    wheel.append(robot.getMotor(wheelName[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    
avoidObsCounter = 0
 
 


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:

    # init loop
    leftSpeed = 1.0
    rightSpeed = 1.0
    if avoidObsCounter > 0:
        avoidObsCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:
        for i in range(NUM_DS):
            if dsens[i].getValue() < 950.0:
                avoidObsCounter = 100;
    wheel[0].setVelocity(leftSpeed)
    wheel[2].setVelocity(leftSpeed)
    wheel[1].setVelocity(rightSpeed)
    wheel[3].setVelocity(rightSpeed)


# Enter here exit cleanup code.
