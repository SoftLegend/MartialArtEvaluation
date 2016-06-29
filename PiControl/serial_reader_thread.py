import threading
import serial


class SerialReadThread(object):

    BUFFER_SIZE = 10

    def initialize_buffer(self):
        self.data = [0] * self.BUFFER_SIZE
        self.CANCEL = False

    def cancel(self):
        self.CANCEL = True

    def __init__(self):
        self.lock = threading.Lock()
        self.initialize_buffer()
        self.position = 0

    def serial_read(self, usb_port):
        print("Serial reader thread started\n")

        ser = serial.Serial(usb_port,
                            9600,
                            timeout=2,
                            xonxoff=False,
                            rtscts=False,
                            dsrdtr=False)

        ser.flushInput()
        ser.flushOutput()
        while not self.CANCEL:
            read_data = ser.readline()
            read_data = read_data.strip()
            #print(read_data)

            try:
                float(read_data)
            except:
                read_data = 0.0

            self.lock.acquire()
            self.data[self.position % self.BUFFER_SIZE] = float(read_data)
            self.position += 1
            self.lock.release()

    def get_data(self):
        self.lock.acquire()

        return_data = self.data
        self.initialize_buffer()

        self.lock.release()

        return return_data

    def start_thread(self):
        self.thread = threading.Thread(target=self.serial_read, args=('/dev/ttyUSB0',))
        self.thread.start()

        #return self.thread