#!/usr/bin/env pybricks-micropython

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color, Button
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

def display():
  press = True
  selected = 0
  time = [0,0,0]
  while press:
    ev3.screen.clear()
    ev3.screen.draw_text(0,0,"Set timer: ")
    ev3.screen.draw_text(0,50, str(time[0]) + ":" + str(time[1]) + ":" +  str(time[2]))
    for i in ev3.buttons.pressed():
      if ev3.buttons.pressed()[0] == Button.CENTER:
        press = False
      if ev3.buttons.pressed()[0] == Button.UP and time[selected] < 24:
        time[selected] = time[selected] + 1
      if ev3.buttons.pressed()[0] == Button.DOWN and time[selected] < 0:
        time[selected] = time[selected] - 1
      if ev3.buttons.pressed()[0] == Button.LEFT and selected != 0:
        selected = selected - 1
      if ev3.buttons.pressed()[0] == Button.RIGHT and selected != 2:
        selected = selected + 1


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
    if (claw_motor.angle()<-10):
      color = elbow_sensor.color()
      rgb = elbow_sensor.rgb()
      print("red:", rgb[0])
      print("green:", rgb[1])
      print("blue:", rgb[2])
      if rgb[0] > 10 and rgb[1] >10:
        print("Yellow")
      if rgb[0] > 10 and rgb[1] < 10:
        print("RED")
      if rgb[2] > 10 and rgb[1] > 10:
        print("green")
      if rgb[2] > 10 and rgb[1] < 10:
        print("blue")
    elbow_motor.run_target(80,0)

def release(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    claw_motor.run_target(200, -90)
    elbow_motor.run_target(60, 0)

def pick_motion(pick_location, drop_location):
  pick(pick_location)
  if (claw_motor.angle()<-10):
    print("item present")
    ev3.speaker.beep()
    wait(300)
    ev3.speaker.beep()
  else: 
    ev3.speaker.beep()
    print("item missing")
  release(drop_location)

def time_start():
  start_time = "15:01:00"
  print(time.strftime("%H:%M:%S"))



LEFT = 200
MIDDLE_LEFT = 150
RIGHT = 0
MIDDLE = 100

def main():
  display()
  time_start()
  active = False
  while active is not True:
    pick_motion(MIDDLE, MIDDLE)
    pick_motion(MIDDLE, MIDDLE)
    pick_motion(MIDDLE, MIDDLE)
    pick_motion(MIDDLE, MIDDLE)
    pick_motion(MIDDLE, MIDDLE)
    pick_motion(LEFT, LEFT)
    wait(5000)




if __name__ == "__main__":
  main()



