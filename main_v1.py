from hmc5883l import HMC5883L
from machine import SoftI2C, Pin
import time

Scl=Pin(4)
Sda=Pin(0)

i2c1 = SoftI2C(scl=Scl, sda=Sda, freq=100000, timeout=250)

sensor = HMC5883L(i2c1)

x, y, z = sensor.read()
print(sensor.format_result(x, y, z))

while True:
    time.sleep(0.5)
    x, y, z = sensor.read()
    print(sensor.format_result(x, y, z))