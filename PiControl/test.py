from serial_reader_thread import SerialReadThread
from time import sleep

ser = SerialReadThread()
thread = ser.start_thread()

while True:
    print(ser.get_data())
    #sleep(0.25)

thread.join()
print("Serial reader thread exit")

"""
import serial
from time import sleep

ser = serial.Serial('/dev/ttyUSB0',
                    9600,
                    timeout=2,
                    xonxoff=False,
                    rtscts=False,
                    dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while True:
  data_raw = ser.readline()
  print(data_raw.strip())
  sleep(0.02)
"""

"""
import usb.core
import usb.util

# Find our device
dev = usb.core.find(find_all=True)
busses = usb.busses()
# Was it found?
if dev is None:
    raise ValueError('Device not found')

for bus in busses:
    devices = bus.devices
    for dev in devices:
        try:
            _name = usb.util.get_string(dev.dev, 19, 1)
        except:
             continue
        dev.set_configuration()
        cfg = dev.get_active_configuration()
        interface_number = cfg[(0,0)].bInterfaceNumber
        alternate_settting = usb.control.get_interface(interface_number)
        print "Device name:",_name
        print "Device:", dev.filename
        print "  idVendor:",hex(dev.idVendor)
        print "  idProduct:",hex(dev.idProduct)
        for config in dev.configurations:
            print "  Configuration:", config.value
            print "    Total length:", config.totalLength
            print "    selfPowered:", config.selfPowered
            print "    remoteWakeup:", config.remoteWakeup
            print "    maxPower:", config.maxPower
        print ""
"""