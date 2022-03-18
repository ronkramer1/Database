import multiprocessing
import threading
import time
from multiprocessing import Process

lock = multiprocessing.Lock()


class Try:
    # r_counter = multiprocessing.Value('i', 0)
    r_counter = multiprocessing.Manager().Value('i', 0)

    def __init__(self):
        None

    def is_locked(self):
        locked = lock.acquire(block=False)

        if not locked:
            return True
        else:
            lock.release()
            return False

    def inc_r(self, sleep):
        if not self.is_locked():
            time.sleep(sleep)
            with Try.r_counter.get_lock():
                Try.r_counter.value += 1
            print(Try.r_counter.value)

        else:
            print("locked, cannot access")


if __name__ == "__main__":
    t1 = Process(target=Try().inc_r, args=(0,))
    t2 = Process(target=Try().inc_r, args=(0,))
    t3 = Process(target=Try().inc_r, args=(0,))
    t4 = Process(target=Try().inc_r, args=(0,))
    t5 = Process(target=Try().inc_r, args=(0,))
    t6 = Process(target=Try().inc_r, args=(0,))

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
