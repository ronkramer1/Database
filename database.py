import copy


class Database:

    def __init__(self):
        self.dict = {}

    def get_value(self, key):
        try:
            return self.dict[key]
        except Exception as e:
            print(e)
            return None

    def set_value(self, key, value):
        try:
            self.dict[key] = value
            return True
        except Exception as e:
            print(e)
            return False

    def del_value(self, key):
        try:
            value = copy.deepcopy(self.dict[key])
            self.dict[key] = None
            return value
        except Exception as e:
            print(e)
        return None
