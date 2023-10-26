from gpiozero import MCP3008, DistanceSensor, Button, LED
from time import sleep
from datetime import datetime

pot = MCP3008(7)
ultrasonic = DistanceSensor(echo=21, trigger=20)
button = Button(18)
led_rojo = LED(25)
file = open("/home/team3/Unit_Practice/distance_log.txt.", "w")

while True:
    button.wait_for_press()
    dist = ultrasonic.distance * 100
    span = pot.value * 100
    dist, span = round(dist, 3), round(span, 3)
    if dist <= span:
        print(f"scaled span : {span}, dist : {dist}")
        led_rojo.off()
        timestamp = datetime.now().strftime('%Y/%m/%d %HH %MM %SS')
        data = f"{timestamp} ---> " \
            f"distance : {dist}, span : {span}\n"
        file.write()
    else:
        print(f"Distance > span!! scaled span : {span}, dist : {dist}")
        led_rojo.on()

    sleep(1)
file.close()