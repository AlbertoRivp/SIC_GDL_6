from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime

led_yellow = LED(20)
led_red = LED(21)
file = open("/home/team3/Toy_projects/cpu_usage_log.txt", 'w')

while True:
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    cpu_usage_mean = sum([i/len(cpu_usage) for i in cpu_usage])
    cpu_usage_mean = round(cpu_usage_mean, 3)
    print(f"cpu usage(%) : {cpu_usage_mean}%")
    if 60 > cpu_usage_mean > 30:
        led_yellow.on()
        led_red.off()
    elif cpu_usage_mean <= 60:
        led_yellow.on()
        led_red.on()
    else:
        led_yellow.off()
        led_red.off()
    data = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')}"\
           f"cpu_usage(%) : {cpu_usage_mean}%"
    file.write(data)
    sleep(1)
    
file.close()