from Character import Character

class Mage(Character):
    def __init__(self):
        super().__init__()

    def attack(self):
        return "Я атакую магией!"

    def defend(self):
        return "Я защищаюсь магическим щитом!"