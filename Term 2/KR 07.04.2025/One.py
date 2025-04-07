class Client:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display_info(self):
        raise NotImplementedError("This method should be overridden in child classes")

    def matches_date(self, search_date):
        return self.date == search_date


class Depositor(Client):
    def __init__(self, name, open_date, deposit_amount, deposit_rate):
        super().__init__(name, open_date)
        self.deposit_amount = deposit_amount
        self.deposit_rate = deposit_rate

    def display_info(self):
        print(f"Вкладчик: {self.name}")
        print(f"Депозит открыт: {self.date}")
        print(f"Размер вклада: {self.deposit_amount} руб.")
        print(f"Процент по вкладу: {self.deposit_rate}%")

class Creditor(Client):
    def __init__(self, name, issue_date, credit_amount, credit_rate, debt_balance):
        super().__init__(name, issue_date)
        self.credit_amount = credit_amount
        self.credit_rate = credit_rate
        self.debt_balance = debt_balance

    def display_info(self):
        print(f"Кредитор: {self.name}")
        print(f"Дата выдачи кредита: {self.date}")
        print(f"Размер кредита: {self.credit_amount} руб.")
        print(f"Процент по кредиту: {self.credit_rate}%")
        print(f"Остаток долга: {self.debt_balance} rub.")

class Organization(Client):
    def __init__(self, name, account_open_date, account_number, account_balance):
        super().__init__(name, account_open_date)
        self.account_number = account_number
        self.account_balance = account_balance

    def display_info(self):
        print(f"Организация: {self.name}")
        print(f"Дата открытия счета: {self.date}")
        print(f"Номер счета: {self.account_number}")
        print(f"Сумма на счету: {self.account_balance} руб.")

def display_clients_info(clients):
    for client in clients:
        client.display_info()
        print("-" * 30)


def search_by_date(clients, search_date):
    matching_clients = [client for client in clients if client.matches_date(search_date)]
    if not matching_clients:
        print("Ни один клиент не открыл счет в эту дату.")
    else:
        print(f"Клиенты открывшие счет в эту дату {search_date}:")
        display_clients_info(matching_clients)



clients = [
    Depositor("Иванов", "10.05.2023", 100000, 7),
    Creditor("Петров", "15.06.2023", 50000, 12, 20000),
    Organization("ООО 'Рога и Копыта'", "20.07.2023", "123456789", 500000),
    Depositor("Сидоров", "10.05.2023", 200000, 8),
    Creditor("Кузнецов", "15.06.2023", 80000, 10, 30000)
]


print("Вся информация о клиентах:")
display_clients_info(clients)


search_date = input("Введите дату для поиска в формате дд.мм.гггг: ")
search_by_date(clients, search_date)