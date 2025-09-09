# Отчет по лабораторной работе 1

## Задание
Реализовать паттерн "Фабричный метод" для создания различных персонажей (воин, маг, лучник) с уникальными методами атаки и защиты.

## Структура проекта

1. Абстрактный класс `Character` определяет интерфейс для всех персонажей.
2. Для каждого типа персонажа реализован свой класс с уникальными методами атаки и защиты.
3. Абстрактный класс `CharacterCreator` определяет фабричный метод `create_character`, который реализуется в наследниках для создания конкретного персонажа.
4. В файле `Test.py` создается список фабрик, для каждой из которых вызывается клиентский код, демонстрирующий работу паттерна.

## Подробное описание файлов

### Character.py
Абстрактный класс, определяющий интерфейс для всех персонажей:
```python
import abc

class Character(abc.ABC):
	def __init__(self):
		pass

	@abc.abstractmethod
	def attack(self):
		pass
    
	@abc.abstractmethod
	def defend(self):
		pass
```
Задает методы `attack` и `defend`, которые должны быть реализованы в наследниках.

### Characters/Warrior.py
Класс воина, реализующий методы атаки и защиты:
```python
from Character import Character

class Warrior(Character):
	def __init__(self):
		super().__init__()

	def attack(self):
		return "Я иду в атаку с мечом!"

	def defend(self):
		return "Я защищаюсь щитом!"
```
Воин атакует мечом и защищается щитом.

### Characters/Mage.py
Класс мага, реализующий методы атаки и защиты:
```python
from Character import Character

class Mage(Character):
	def __init__(self):
		super().__init__()

	def attack(self):
		return "Я атакую магией!"

	def defend(self):
		return "Я защищаюсь магическим щитом!"
```
Маг атакует магией и защищается магическим щитом.

### Characters/Archer.py
Класс лучника, реализующий методы атаки и защиты:
```python
from Character import Character

class Archer(Character):
	def __init__(self):
		super().__init__()

	def attack(self):
		return "Я стреляю из лука!"

	def defend(self):
		return "Я уклоняюсь!"
```
Лучник стреляет из лука и уклоняется от атак.

### CharacterCreator.py
Абстрактный класс создателя персонажа и его наследники:
```python
from Characters.Mage import Mage
from Characters.Archer import Archer
from Characters.Warrior import Warrior
import Character

import abc

class CharacterCreator(abc.ABC):
	@abc.abstractmethod
	def create_character(self) -> Character:
		pass

class WarriorCreator(CharacterCreator):
	def create_character(self) -> Character:
		return Warrior()
    
class MageCreator(CharacterCreator):
	def create_character(self) -> Character:
		return Mage()
    
class ArcherCreator(CharacterCreator):
	def create_character(self) -> Character:
		return Archer()
```
Каждый наследник реализует фабричный метод для создания конкретного персонажа.

### Test.py
Клиентский код, демонстрирующий работу фабрик:
```python
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
```
Создается список фабрик, для каждой вызывается функция, которая создает персонажа и вызывает его методы.


## Результаты выполнения
При запуске программы выводятся сообщения о действиях каждого персонажа:

```
Я иду в атаку с мечом!
Я защищаюсь щитом!
------------------------------
Я атакую магией!
Я защищаюсь магическим щитом!
------------------------------
Я стреляю из лука!
Я уклоняюсь!
------------------------------
```
