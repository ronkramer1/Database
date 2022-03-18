import ctypes
import multiprocessing
import threading
import time

from saver import Saver


class Client:
    def __init__(self):
        self.saver = Saver("dict.txt")

    def get_value(self, key, sema, name, sleep=1):
        sema.acquire()
        print('process {} starting doing business'.format(name))

        try:
            time.sleep(sleep)

            value = self.saver.get_value(key)
            if value is None:
                print('No value attached to the key: {}'.format(key))
            else:
                print('Key: {}, Value: {}'.format(key, value))

        except Exception as e:
            print("Key does not exist")

        # print(sema)
        sema.release()

    # def get_value(self, key):
    #     if not self.sav
    #     er.locked and self.counter < 10:
    #         self.counter += 1
    #         print(self.counter)
    #         if self.counter == 10:
    #             self.saver.locked = True
    #         time.sleep(10)
    #         value = self.saver.get_value(key)
    #         if value is None:
    #             print('No such key: {}'.format(key))
    #         else:
    #             print('Key: {}, Value: {}'.format(key, value))
    #         self.saver.locked = False
    #         self.counter -= 1
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

    def set_value(self, key, value, sema, name):
        sema.acquire()
        print('process {} starting doing business'.format(name))

        try:
            if self.saver.set_value(key, value):
                print('Key: {}, Value: {}'.format(key, value))
            else:
                print("Couldn't set the value")
        except Exception as e:
            print(e)

        sema.release()

    # def set_value(self, key, value):
    #     if self.is_locked():
    #         print("cannot access the database currently")
    #         time.sleep(1)
    #         self.set_value(key, value)
    #
    #     else:
    #         self.lock.acquire()
    #         time.sleep(1)
    #         try:
    #             if self.saver.set_value(key, value):
    #                 print('Key: {}, Value: {}'.format(key, value))
    #             else:
    #                 print("Couldn't set the value")
    #         finally:
    #             self.lock.release()

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

    def del_value(self, key, sema, name):
        sema.acquire()
        print('process {} starting doing business'.format(name))

        try:
            value = self.saver.del_value(key)
            if value is None:
                print('Error when deleting the value for the key: {}'.format(key))
            else:
                print('Deleted value: Key: {}, Value: {}'.format(key, value))

        except Exception as e:
            print(e)

        sema.release()

    # def del_value(self, key):
    #     if self.is_locked():
    #         print("cannot access the database currently")
    #         time.sleep(1)
    #         self.del_value(key)
    #
    #     else:
    #         self.lock.acquire()
    #         # time.sleep(1)
    #         try:
    #             value = self.saver.del_value(key)
    #             if value is None:
    #                 print('Error when deleting the value for the key: {}'.format(key))
    #             else:
    #                 print('Key: {}, Value: {}'.format(key, value))
    #             self.saver.locked = False
    #         finally:
    #             self.lock.release()

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
