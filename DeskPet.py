"""
# DeskPet.py
# MicroPython-compatible class skeleton for DeskPet
"""


class DeskPet:
    def __init__(self, name):
        # Private attributes initialized per UML specification
        self._name = name
        self._isOn = False
        self._mood = "neutral"

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def changeMood(self, newMood):
        pass

    def handleInteraction(self, action):
        pass


if __name__ == "__main__":
    # Verification of instantiation and method calls
    pet = DeskPet("DeskBuddy")
    pet.turnOn()
    pet.changeMood("happy")
    pet.handleInteraction("tap")
    pet.turnOff()
