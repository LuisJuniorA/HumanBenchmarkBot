from abc import ABC, abstractmethod

class GameBase(ABC):
    @abstractmethod
    def start(self) -> bool:
        pass

    @abstractmethod
    def set_settings(self) -> bool:
        pass

    @abstractmethod
    def play(self)-> None:
        pass
