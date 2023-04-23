#!/usr/bin/env pybricks-micropython

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()



claw_motor = Motor(Port.A)
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
claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
claw_motor.reset_angle(0)
claw_motor.run_target(200, -90)

def pick(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    claw_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    elbow_motor.run_target(60,9)
    color = elbow_sensor.color()
    print(color)
    elbow_motor.run_target(80,0)

def release(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    claw_motor.run_target(200, -90)
    elbow_motor.run_target(60, 0)

def pick_motion(pick_location, drop_location):
  pick(pick_location)
  print(claw_motor.angle())
  if (claw_motor.angle()<-10):
    print("item present")
    ev3.speaker.beep()
    wait()
  else: 
    ev3.speaker.beep()
    print("item missing")
  release(drop_location)

def time_start(start):
  now = time.localtime()
  current_time = time.strftime("%H:%M:%S", now)
  print(current_time)

LEFT = 200
MIDDLE_LEFT = 150
RIGHT = 0
MIDDLE = 100

def main():
  time_start(1)
  active = False
  while active is not True:
    pick_motion(LEFT, MIDDLE_LEFT)
    pick_motion(MIDDLE, MIDDLE_LEFT)
    pick_motion(RIGHT, MIDDLE_LEFT)
    wait(5000)


  

if __name__ == "__main__":
  main()



