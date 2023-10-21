from gpiozero import MCP3008
from time import sleep

pot = MCP3008(7)

while True:
    print(pot.value * 100)
    sleep(1)