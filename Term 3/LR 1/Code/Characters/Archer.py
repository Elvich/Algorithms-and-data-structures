from Character import Character

class Archer(Character):
    def __init__(self):
        super().__init__()

    def attack(self):
        return "Я стреляю из лука!"

    def defend(self):
        return "Я уклоняюсь!"