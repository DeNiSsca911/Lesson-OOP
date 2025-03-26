class Account():
    def __init__(self,id,balance=0):
        self.id = id
        self.balance = balance

    def deposit(self,money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счету - {self.balance}")

    def withdraw(self,money):
        if money > self.balance:
            print(f"недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"вы успешно сняли {money}руб.Остаток на счете :{self.balance}")

    def all_balance(self):
        print(f"текущий баланс - {self.balance}")

man = Account(1232323,600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)