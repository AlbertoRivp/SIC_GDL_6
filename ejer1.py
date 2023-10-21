from gpiozero import Button,LED
import psutil

monitoreo = psutil.disk_usage("/")


led_rojo = LED(17)
led_Amarillo = LED(18)


usando = monitoreo.percent
print(usando)


while True:
    if usando > 60.0:
        led_rojo.on()
        led_Amarillo.off()
    elif usando > 30.0:
        led_Amarillo.on()
        led_rojo.off()
        