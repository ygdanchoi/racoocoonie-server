#!/usr/bin/python3

import json
import requests
from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('/dev/ttyACM0')
board.digital[9].mode = SERVO

def rotate_servo(angle):
    board.digital[9].write(angle)
    sleep(0.01)

for i in range(0, 180):
    rotate_servo(i)
for i in range(180, 1, -1):
    rotate_servo(i)

while True:
    try:
        response = requests.get('http://ec2-44-210-136-200.compute-1.amazonaws.com:3000/get')
        data = json.loads(response.text)
        angle = int(max(0, min(180, 180 - (abs(data[0]) + abs(data[1]) + abs(data[2])) * 30)))
        rotate_servo(angle)
        # sleep(0.1)
    except:
        print('oh no')