from request import Request
from shop import Shop
from store import Store
from AbcStorage import AbstractStorage

store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    },
)


shop = Shop(
    items={
        "печенька": 1,
        "собачка": 2,
        "елка": 2,
        "пончик": 3,
        "зонт": 2,
    },
)


storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print("\nДобрый день\n")

    while True:

        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            '\nВведите запрос в формате "Доставить з печеньки из склад в магазин"\n'
            '\nВведите "стоп" или "stop", если хотите закончить:\n')

        if user_input in ('stop', 'стоп'):
            break

        request = Request(request=user_input, storages=storages)

        if storages[request.departure].remove(request.product, request.amount):
            print(f"Курьер забрал {request.amount} {request.product} из {request.departure}")

            if storages[request.destination].add(request.product, request.amount):
                print(f"Курьер доставил {request.amount} {request.product} в {request.destination}")
            else:
                storages[request.departure].add(request.product, request.amount)
                print(f"Курьер вернул {request.amount} {request.product} в {request.departure}")



print(main())