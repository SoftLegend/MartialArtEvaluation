import threading
import serial


class SerialReadThread(object):

    BUFFER_SIZE = 40  # 10

    def cancel(self):
        self.CANCEL = True

    def __init__(self):
        self.CANCEL = False
        self.lock = threading.Lock()
        self.data = [0] * self.BUFFER_SIZE
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

            try:
                float(read_data)
            except:
                read_data = 0.0

            self.lock.acquire()
            self.data[self.position % self.BUFFER_SIZE] = float(read_data)
            self.position += 1
            self.lock.release()

        ser.close()

    def get_data(self):
        self.lock.acquire()

        return_data = self.data[:]

        current_pos = self.position % self.BUFFER_SIZE
        tmp = current_pos
        # In punch, look for previous 0.0
        if self.data[tmp] > 0.0:
            while (tmp > (current_pos - self.BUFFER_SIZE)) and (self.data[tmp] > 0.0):
                tmp -= 1

        # Clear buffer
        for i in xrange(1, self.BUFFER_SIZE):
            if i in xrange(tmp + 1, current_pos):
                return_data[i] = 0.0
            else:
                self.data[i] = 0.0

        self.lock.release()

        return return_data

    def start_thread(self):
        f = open("config.txt")
        usb_port = f.readline()
        f.close()
        self.thread = threading.Thread(target=self.serial_read, args=(usb_port,))
        self.thread.start()
