import os
import pickle

from database import Database


class Saver(Database):

    def __init__(self, file_name):
        Database.__init__(self)
        self.file_name = file_name

    def save(self):
        with open(self.file_name, 'wb') as f:
            pickle.dump(self.dict, f)

    def load(self):
        data = {}
        if os.stat(self.file_name).st_size != 0:
            with open(self.file_name, 'rb') as f:
                data = pickle.load(f)
        return data

    def get_value(self, key):
        self.dict = self.load()
        return super().get_value(key)

    def set_value(self, key, value):
        self.dict = self.load()
        value = super().set_value(key, value)
        self.save()
        return value

    def del_value(self, key):
        self.dict = self.load()
        value = super().del_value(key)
        self.save()
        return value