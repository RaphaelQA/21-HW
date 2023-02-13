from AbcStorage import AbstractStorage



class Request():

    def __init__(self, request: str, storages: dict[str, AbstractStorage]):
        parsed_request = request.lower().split(" ")
        if len(parsed_request) > 7:
            print("Неправильный ввод")
            return

        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]
        self.departure = parsed_request[4]
        self.destination = parsed_request[6]

        if self.departure not in storages or self.destination not in storages:
            print("Неизвестный склад")
            return