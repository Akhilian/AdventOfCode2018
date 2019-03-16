from Day1.Chronal_Calibration import Device
from utils.FileReader import FileReader

sequence = FileReader.read('../sources/day1.txt')

device = Device()
device.calibrate(sequence)

print('Final frequency state        :', device.final_frequency)
print('Frequency that occured twice :', device.frequency)