from serial_reader_thread import SerialReadThread
from time import sleep

ser = SerialReadThread()
thread = ser.start_thread()

while True:
    print(ser.get_data())
    sleep(0.25)

thread.join()
print("Serial reader thread exit")