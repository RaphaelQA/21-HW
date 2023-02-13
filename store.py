from AbcStorage import AbstractStorage


class Store(AbstractStorage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        self.__items = items
        self.__capacity = capacity
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_free_space() < amount:
            print("Не хватает места")

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

        return True

    def remove(self, name, amount) -> None:
        if name not in self.__items:
            print("Такого товара нет")
            return False

        if self.__items[name] < amount:
            print("Товар закончился :(")
            return False

        self.__items[name] -= amount
        if self.__items[name] <= 0:
            self.__items.pop(name)

        return True

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
