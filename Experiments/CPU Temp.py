#import numpy
#import matplotlib.pyplot as plt
import json
#from psutil import sensors_temperatures
#import time

import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)

cpuTemps = []

def save(data, filename="toDo.json"):
    f = open(filename, "w")
    json.dump(data, f)
    f.close()

def load(filename="toDo.json"):
    f = open(filename, "r")
    data = json.load(f)
    f.close()


#save(cpuTemps, "cpuTemps.json")

#cpuTemps = load("cpuTemps.json").append(cpu)

print(wmi.sensors_temperatures())