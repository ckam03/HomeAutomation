from abc import ABC, abstractmethod


class Client(ABC):
    @abstractmethod
    def on_or_off(self, state):
        pass
