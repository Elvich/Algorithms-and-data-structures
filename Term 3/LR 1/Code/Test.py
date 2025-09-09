from CharacterCreator import CharacterCreator, WarriorCreator, MageCreator, ArcherCreator

creators = [
    WarriorCreator(),
    MageCreator(),
    ArcherCreator()
]


def client_code(creator: CharacterCreator):
    character = creator.create_character()
    print(character.attack())
    print(character.defend())

for creator in creators:
    print()
    client_code(creator)
    print("-" * 30)