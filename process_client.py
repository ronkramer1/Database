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

        sema.release()

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
