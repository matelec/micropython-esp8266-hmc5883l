from hmc5883l import HMC5883L
from machine import SoftI2C, Pin
import time

Scl=Pin(4)
Sda=Pin(0)

i2c1 = SoftI2C(scl=Scl, sda=Sda, freq=100000, timeout=250)

sensor = HMC5883L(i2c1)


Xmin=1000
Xmax=-1000
Ymin=1000
Ymax=-1000

while True:
    try:
        time.sleep(0.2)
        x, y, z = sensor.read()
        Xmin=min(x,Xmin)
        Xmax=max(x,Xmax)
        Ymin=min(y,Ymin)
        Ymax=max(y,Ymax)
        print(sensor.format_result(x, y, z))
        print("Xmin="+str(Xmin)+"; Xmax="+str(Xmax)+"; Ymin="+str(Ymin)+"; Ymax="+str(Ymax))

    except KeyboardInterrupt:
        print()
        print('Got ctrl-c')
        
        xs=1
        ys=(Xmax-Xmin)/(Ymax-Ymin)
        xb =xs*(1/2*(Xmax-Xmin)-Xmax)
        yb =xs*(1/2*(Ymax-Ymin)-Ymax)
        print("Calibration corrections:")
        print("xs="+str(xs))
        print("xb="+str(xb))
        print("ys="+str(ys))
        print("yb="+str(yb))
        break
