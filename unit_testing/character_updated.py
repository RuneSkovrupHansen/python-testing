#!/bin/python3

class Character:

    _MIN_LEVEL = 1
    _MAX_LEVEL = 100

    def __init__(self) -> None:
        self.name = ""
        self.level = self._MIN_LEVEL

    def set_level(self, level):

        if level < self._MIN_LEVEL:
            self.level = self._MIN_LEVEL

        elif level > self._MAX_LEVEL:
            self.level = self._MAX_LEVEL

        else:
            self.level = level

    def level_up(self):

        if self.level < self._MAX_LEVEL:
            self.level += 1

    @classmethod
    def contains_proanity(self, string):

        return any(s.lower() in string.lower() for s in ["bugger", "damn", "asshat"])

    def set_name(self, name):

        if not isinstance(name, str):
            raise TypeError

        if Character.contains_proanity(name):
            return False

        self.name = name
        return True
