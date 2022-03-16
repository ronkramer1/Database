import threading
import time


class Try:
    r_counter = 0
    lock = threading.Lock()

    def __init__(self):
        None

    def inc_r(self, sleep):
        time.sleep(sleep)
        with self.lock:
            Try.r_counter += 1
        print(Try.r_counter)


if __name__ == "__main__":
    t1 = threading.Thread(target=Try().inc_r(0))
    t2 = threading.Thread(target=Try().inc_r(2))
    t3 = threading.Thread(target=Try().inc_r(6))
    t4 = threading.Thread(target=Try().inc_r(4))
    t5 = threading.Thread(target=Try().inc_r(2))
    t6 = threading.Thread(target=Try().inc_r(0))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
