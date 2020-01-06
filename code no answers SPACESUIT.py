"""Welcome to a THIS IS MY SPACESUIT. workshop!
This is the file you will use to code with your device.
There is pseudocode to give hints to the code.
After completing an example, you must comment out previous examples by using # on each line with code."""


"""EXAMPLE 1: CHECK CHECK. This example prints "THIS IS MY SPACESUIT. to the serial. Use the two lines of code below"""
from adafruit_circuitplayground import cp
print("THIS IS MY SPACESUIT.") #you can change the text to write whatever you want


'''EXAMPLE 2: THE MIGHTY LED BLINK.
This example has a single LED blink.'''

'''import statements - use 2 lines of code below'''
#from adafruit_circuitplayground import cp
#import time

#to do: create a while loop that runs when it is true

    #to do: reassign new variable cp.red_led to set it to True

    #to do: use time.sleep() function to tell the light how long to stay on for. Choose number 0-1.

    #to do: reassign new variable to cp.red_led to set it to False

    #to do: use time.sleep() function to tell the light how long to stay on for. Choose number 0-1.





"""EXAMPLE 3: RAINBOW MAGIC. This example lights up the first NeoPixel red. The rest of the example will have you light up the entire board!"""
""" Things to know:
(255, 0, 0) = colors from a range of 0-255. You must input a number from 0-255 to represent Red,Green,Blue"""

'''import statements - use 2 lines of the code below'''
from adafruit_circuitplayground import cp
import time

'''#sets the brightness of the LEDs- use the code below'''
#cp.pixels.brightness = 0.1

#to do: create a while loop that runs when it is true

#how to access the first LEDon the circle of your board - use the code below
    #cp.pixels[0] = (255, 0, 0)

    #to do: make more LEDs light up on the board by using the same notation as above. What will change? What color do you want to make?


'''EXAMPLE 4: I HAVE THE WORLD IN MY FINGERPRINTS.
This example lights up the entire board based on your touch'''

'''import statements - use 2 lines of code below'''
#from adafruit_circuitplayground import cp
#import time


'''sets the brightness of the LEDs- use the code below'''
#cp.pixels.brightness = 0.1

#to do: create a while loop that runs when it is true

    # creates if statement if you touch the A1 port - use 1 line of code below
    #if cp.touch_A1:
        #fills all pixels to one color - use 1 line of code below
        #cp.pixels.fill((255, 0, 0))
    # to do: create an if statement if you touch the A2 port

        #to do fill all pixels to one color




'''EXAMPLE 5: DJ IN THE HOUSE.
This example plays a tone and shows an LED when you press a button'''

'''import statements - use 2 lines of code below'''
#from adafruit_circuitplayground import cp
#import time

'''sets the brightness of the LEDs- use the code below'''
#cp.pixels.brightness = 0.2

#to do: create a while loop that runs when it is true
#while True:
    #to do: create an if statement for cp.button_a

        #to do: access the 1st pixel like example 3 and set a color to it

        #to do: use cp.start_tone() to tell the device how long to ring a tone. Insert number from 0-400

    #to do: create an elif statement for cp.button_b

        #to do: access the 2nd pixel like example 3 and set a color to it

        #to do: use cp.start_tone() to tell the device how long to ring a tone. Insert number from 0-400

    #to do: create an else statement

        #to do: access the 1nd pixel like example 3 and set the color to (0,0,0)

        #to do: access the 2nd pixel like example 3 and set the color to (0,0,0)

        #stop the tone - use 1 line of the code below
        #cp.stop_tone()



