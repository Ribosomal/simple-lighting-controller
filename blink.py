from machine import Pin
from utime import sleep
import neopixel


#temp
fanPin: Pin = Pin(22) 
fanNum: int = 30

fanPixels: neopixel.NeoPixel = neopixel.NeoPixel(fanPin, fanNum)