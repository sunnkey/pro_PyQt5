import threading


def fun_print():
    print(1)


i = 0
timer1 = threading.Timer(0.1, fun_print)
timer1.start()
while True:
    pass
timer1.cancel()
