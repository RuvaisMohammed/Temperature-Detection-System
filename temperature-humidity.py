from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
sense.clear()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def temperature():
    temp = sense.get_temperature()
    print(temp)
    if temp > 34:
        sense.clear(red)
    elif 24 < temp <= 34:
        sense.clear(green)
    elif 0 <= temp <= 24:
        sense.clear(blue)
    sleep(1)
    sense.show_message(str(round(temp, 2)))

def humidity():
    humidity_value = sense.get_humidity()
    print(humidity_value)
    if humidity_value > 40:
        sense.clear(blue)
    elif 30 < humidity_value <= 40:
        sense.clear(green)
    elif 0 <= humidity_value <= 30:
        sense.clear(red)
    sleep(1)
    sense.show_message(str(round(humidity_value, 2)))

while True:
    temperature()
    humidity()