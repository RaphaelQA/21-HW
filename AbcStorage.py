from abc import abstractmethod, ABC


class AbstractStorage(ABC):
    def __init__(self, items: dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    @abstractmethod
    def add(self, items, amount) -> None:
        pass

    @abstractmethod
    def remove(self, items, amount) -> None:
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

