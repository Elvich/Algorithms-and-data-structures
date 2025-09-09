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
