import ctypes
import multiprocessing
import threading
import time

from saver import Saver


class Client:
    r_counter = 0
    lock = threading.Lock()

    def __init__(self, state=None):
        self.saver = Saver("dict.txt")

    # def get_value(self, key):
    #     if not self.saver.locked:
    #         self.saver.locked = True
    #         value = self.saver.get_value(key)
    #         if value is None:
    #             return 'No such key: {}'.format(key)
    #         else:
    #             return 'Key: {}, Value: {}'.format(key, value)
    #         self.saver.locked = False
    #     else:
    #         self.get_value(key)

    def increment(self):
        with self.lock:
            Client.r_counter += 1

    def decrement(self):
        with self.lock:
            Client.r_counter -= 1

    def get_value(self, key, sleep):
        if self.lock.locked() or Client.r_counter >= 10:
            print("cannot access the database currently")
            time.sleep(1)
            self.get_value(key, sleep)

        else:
            self.increment()
            acquired_flag = False
            try:
                time.sleep(sleep)
                # print(Client.r_counter)
                if Client.r_counter == 10:
                    self.lock.acquire()
                    acquired_flag = True
                    print("locked")

                value = self.saver.get_value(key)
                if value is None:
                    print('No value attached to the key: {}'.format(key))
                else:
                    print('Key: {}, Value: {}'.format(key, value))

            except Exception as e:
                print("Key does not exist")

            finally:
                print(str(Client.r_counter) + ". finished")
                if acquired_flag:
                    self.lock.release()

            self.decrement()
    # def get_value(self, key):
    #     if not self.sav
    #     er.locked and self.r_counter < 10:
    #         self.r_counter += 1
    #         print(self.r_counter)
    #         if self.r_counter == 10:
    #             self.saver.locked = True
    #         time.sleep(10)
    #         value = self.saver.get_value(key)
    #         if value is None:
    #             print('No such key: {}'.format(key))
    #         else:
    #             print('Key: {}, Value: {}'.format(key, value))
    #         self.saver.locked = False
    #         self.r_counter -= 1
    #     else:
    #         print("cannot access the database currently")

    # def set_value(self, key, value):
    #     if not self.saver.locked:
    #         self.saver.locked = True
    #         if self.saver.set_value(key, value):
    #             return 'Key: {}, Value: {}'.format(key, value)
    #         else:
    #             return 'Key: {} already exists'.format(key)
    #         self.saver.locked = False
    #     else:
    #         self.set_value(key, value)

    def set_value(self, key, value):
        if self.lock.locked():
            print("cannot access the database currently")
            time.sleep(1)
            self.set_value(key, value)

        else:
            self.lock.acquire()
            time.sleep(1)
            try:
                if self.saver.set_value(key, value):
                    print('Key: {}, Value: {}'.format(key, value))
                else:
                    print("Couldn't set the value")
            finally:
                self.lock.release()

    # def set_value(self, key, value):
    #     if not self.saver.locked:
    #         self.saver.locked = True
    #         time.sleep(10)
    #         if self.saver.set_value(key, value):
    #             print('Key: {}, Value: {}'.format(key, value))
    #         else:
    #             print('Key: {} already exists'.format(key))
    #         self.saver.locked = False
    #     else:
    #         print("cannot access the database currently")

    def del_value(self, key):
        if self.lock.locked():
            print("cannot access the database currently")
            time.sleep(1)
            self.del_value(key)

        else:
            self.lock.acquire()
            # time.sleep(1)
            try:
                value = self.saver.del_value(key)
                if value is None:
                    print('Error when deleting the value for the key: {}'.format(key))
                else:
                    print('Key: {}, Value: {}'.format(key, value))
                self.saver.locked = False
            finally:
                self.lock.release()

    # def del_value(self, key):
    #     if not self.saver.locked:
    #         self.saver.locked = True
    #         value = self.saver.del_value(key)
    #         if value is None:
    #             print('No such key: {}'.format(key))
    #         else:
    #             print('Key: {}, Value: {}'.format(key, value))
    #         self.saver.locked = False
    #     else:
    #         print("cannot access the database currently")
