# PA1473 - Software Development: Agile Project (Template)

## Template information
This template should help your team write a good readme-file for your project. (The file is called README.md in your project directory.)
You are of course free to add more sections to your readme if you want to.

Readme-files on GitHub are formatted using Markdown. You can find information about how to format using Markdown here: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Your readme-file should include the following sections:


## Introduction

This Code functions so that the robot will do different tasks such as pick up objects, read their colors and sort them accordingly, Drop off on different locations. This code builds on a lego mindstorms robot arm to do the previously mentioned tasks. 

## Getting started

You need ev3 micropython extension in vscode. You also need the parts Motor, TouchSensor, ColorSensor, Ports, to build the Robot arm h25.
Connection to robot, in this case through Bluetooth or cable.


## Building and running

Send the code to the robot via bluetooth then the calibration will start before asking for user input via display.
User has to input time manually via the robot display for the program to run. Only one user input is asked at a time, press the right and left buttons to change from hours, minutes and seconds. Use the up and down buttons to set the time and once the time is correct press the center button to start. Then wait inputed time.

## Features
- [x] US01: As a customer, I want the robot to pick up items
- [x] US01B: As a customer, I want the robot to pick up items from a designated position
- [x] US02: As a customer, I want the robot to drop off items
- [x] US02B: As a customer, I want the robot to drop items off at a designated position.
- [x] US03: As a customer, I want the robot to be able to determine if an item is present at a given location 
- [x] US04: As a customer, I want the robot to tell me the color of an item.
- [x] US04B: As a customer, I want the robot to tell me the color of an item at a designated position. 
- [x] US05: As a customer, I want the robot to drop items off at different locations based on the color of the item.
- [x] US06: As a customer, I want the robot to be able to pick up items from elevated positions.
- [] US08 As a customer, I want to be able to calibrate maximum of three different colors and assign them to specific drop-off zones.
- [] US08B As a customer, I want to be able to calibrate items with three different colors and drop the items off at specific drop-off zones based on color
- [x] US09: As a customer, I want the robot to check the pickup location periodically to see if a new item has arrived
- [x] US10: As a customer, I want the robot to sort items at a specific time
- [] US11: As a customer, I want two robots to communicate and work together on sorting items without colliding with eachother 
- [] US12: As a customer, I want to manually set the  locations and heights of one pick-up zone and two drop-off zones 