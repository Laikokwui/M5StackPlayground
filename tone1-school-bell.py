from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)

Title = M5Title(title="Example M5 Stack", x=3, fgcolor=0xf1f0f0, bgcolor=0x000048)
circle0 = M5Circle(78, 90, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(235, 90, 15, 0xFFFFFF, 0xFFFFFF)
label1 = M5TextBox(255, 218, "i am Siri", lcd.FONT_Default, 0xFFFFFF, rotate=0)


while True:
  speaker.sing(698, 1)
  speaker.sing(889, 1)
  speaker.sing(784, 1)
  speaker.sing(523, 2)
  wait(0.5)
  speaker.sing(698, 1)
  speaker.sing(784, 1)
  speaker.sing(889, 1)
  speaker.sing(698, 2)
  wait(0.5)
  speaker.sing(889, 1)
  speaker.sing(698, 1)
  speaker.sing(784, 1)
  speaker.sing(523, 2)
  wait(0.5)
  speaker.sing(523, 1)
  speaker.sing(784, 1)
  speaker.sing(889, 1)
  speaker.sing(698, 2)
  wait(0.5)
  wait_ms(2)

  