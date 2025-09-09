from Character import Character

class Warrior(Character):
    def __init__(self):
        super().__init__()

    def attack(self):
        return "Я иду в атаку с мечом!"

    def defend(self):
        return "Я защищаюсь щитом!"