from abc import ABC, abstractmethod

class AbstractBook(ABC):

    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def published_at(self):
        pass
