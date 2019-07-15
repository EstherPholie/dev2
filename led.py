from gpiozero import LED
from time import sleep

led = LED(18)#red
led1 = LED(17)#white
led2 = LED(27)#blue
buzz = LED(22)

while True:
    led.on()
    sleep(0.03)
    buzz.on()
    sleep(1)
    buzz.off()
    sleep(1)
    led.off()
    sleep(0.03)
    
    
    
    led1.on()
    sleep(0.03)
    buzz.on()
    sleep(1)
    buzz.off()
    sleep(1)
    led1.off()
    sleep(0.03)
    
    led2.on()
    sleep(0.03)
    buzz.on()
    sleep(1)
    buzz.off()
    sleep(1)
    led2.off()
    sleep(0.03)
