#!/usr/bin/python

import broadlink
import pdb
devices = broadlink.discover(timeout=5)

for i in devices:
    i.auth()
    isPowerOn = i.check_power()
    print("check power:" + str(isPowerOn))
    if not isPowerOn:
        print("set power")
        i.set_power(True)
        print("check power:" + str(i.check_power()))
    isLightOn = i.check_nightlight()
    print("get nightlight:" + str(isLightOn))
    if not isLightOn:
        print("set night light")
        i.set_nightlight(True)
        print("now current night light: " + str(i.check_nightlight()))
