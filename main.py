#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()



gripper_motor = Motor(Port.A)
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
elbow_motor.control.limits(speed=60, acceleration=120)
base_motor.control.limits(speed=60, acceleration=120)
base_switch = TouchSensor(Port.S1)
elbow_sensor = ColorSensor(Port.S2)
elbow_motor.run_time(-30, 1000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
elbow_motor.run(15)

COLORS = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]

while elbow_sensor.reflection() > 1:
  wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()
base_motor.run(-60)

while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)


def pick(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    elbow_motor.run_target(60,9)
    color = elbow_sensor.color()
    print(color)
    elbow_motor.run_target(80,0)

def release(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    gripper_motor.run_target(200, -90)
    elbow_motor.run_target(60, 0)


LEFT = 160
RIGHT = 0
MIDDLE = 100

def main():
  pick(LEFT)
  if (gripper_motor.angle()<0):
    rint("item present")
    ev3.speaker.beep(2)
  else: 
    ev3.speaker.beep()
    print("item missing")
  release(MIDDLE)

  pick(RIGHT)
  if (gripper_motor.angle()<0):
    print("item present")
    ev3.speaker.beep(2)
  else: 
    ev3.speaker.beep()
    print("item missing")
  release(MIDDLE)

if __name__ == "__main__":
  main()



