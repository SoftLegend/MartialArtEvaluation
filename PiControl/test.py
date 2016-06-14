import time
from threading import Timer

remaining_time = 60.0

def print_time():
    global remaining_time
    remaining_time = remaining_time - 0.25
    print("%f\t\t%s" % (remaining_time, time.time()))

    thread = Timer(0.25, print_time, ())
    thread.start()


def print_some_times():
    print time.time()
    thread = Timer(0.25, print_time, ())
    thread.start()

print_some_times()