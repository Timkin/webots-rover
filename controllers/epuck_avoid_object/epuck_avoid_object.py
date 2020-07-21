"""epuck_avoid_object controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot. DistanceSensor, Motor

# get the time step of the current world.
#timestep = int(robot.getBasicTimeStep())

TIME_STEP = 64
NUM_DISTSENS = 8
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()


# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
# initialise devices
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i = range(NUM_DISTSENS):
    ps.append(robot.getDistanceSensor(psNames[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    psVal = []
    for i in range(NUM_DISTSENS):
        psVal.append(ps[i].getValue())

    # Process sensor data here.
    right_obstacle = psVal[0] > 80.0 or psVal[1] > 80.0 or psVal[2] > 80.0
    left_obstacle = psVal[5] > 80.0 or psVal[6] > 80.0 or psVal[7] > 80.0

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    leftWheelSpd = 0.5 * MAX_SPEED
    rightWheelSpd = 0.5 * MAX_SPEED
    
    if left_obstacle:
        leftWheelSpd += 0.5 * MAX_SPEED
        rightWheelSpd -= 0.5 * MAX_SPEED
    elif right_obstacle:
        leftWheelSpd -= 0.5 * MAX_SPEED
        rightWheelSpd += 0.5 * MAX_SPEED
        

    leftMotor.setVelocity(leftWheelSpd)
    rightMotor.setVelocity(rightWheelspd)
    
    pass

# Enter here exit cleanup code.
