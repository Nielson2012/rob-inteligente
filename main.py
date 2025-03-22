from microbit import *
import music

# Definindo os pinos para os motores
motor_a_forward = pin0
motor_a_backward = pin1
motor_b_forward = pin2
motor_b_backward = pin3

def move_forward():
    motor_a_forward.write_digital(1)
    motor_a_backward.write_digital(0)
    motor_b_forward.write_digital(1)
    motor_b_backward.write_digital(0)

def move_backward():
    motor_a_forward.write_digital(0)
    motor_a_backward.write_digital(1)
    motor_b_forward.write_digital(0)
    motor_b_backward.write_digital(1)

def turn_left():
    motor_a_forward.write_digital(0)
    motor_a_backward.write_digital(1)
    motor_b_forward.write_digital(1)
    motor_b_backward.write_digital(0)

def turn_right():
    motor_a_forward.write_digital(1)
    motor_a_backward.write_digital(0)
    motor_b_forward.write_digital(0)
    motor_b_backward.write_digital(1)

def stop():
    motor_a_forward.write_digital(0)
    motor_a_backward.write_digital(0)
    motor_b_forward.write_digital(0)
    motor_b_backward.write_digital(0)

while True:
    if button_a.is_pressed():
        move_forward()
    elif button_b.is_pressed():
        move_backward()
    elif pin4.is_touched():  # Use pin4 to turn left
        turn_left()
    elif pin5.is_touched():  # Use pin5 to turn right
        turn_right()
    else:
        stop()
