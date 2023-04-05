from database import Database


class BaseClass:
    database = Database()

    def __init__(self, name):
        self.name = name
        self.instance_database = Database()

    def __str__(self):
        return self.name
