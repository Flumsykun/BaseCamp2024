class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.password = password
        self.balance = balance

    def display_balance(self):
        print(f"{self.owner:8s}'s balance: {self.balance:5d} euros")

    def deposit(self, amount:int):
        self.balance += amount

    def withdrawal(self, amount:int):
        if amount > self.balance:
            print(f"{self.owner} does not have enough funds to withdraw {amount} euros.")
        else:
            self.balance -= amount

    def transfer(self, amount:int, other_account):
        if amount > self.balance:
            print(f"{self.owner} does not have enough funds to transfer {amount} euros.")
        else:
            self.withdrawal(amount)
            other_account.deposit(amount)
            print(f"{self.owner} transferred {amount} euros to {other_account.owner}.")



if __name__ == "__main__":
    frans = BankAccount("Frans", "reimf", 80)
    karlijn = BankAccount("Karlijn", "hoffk", 120)

    frans.display_balance()
    karlijn.display_balance()

    frans.transfer(30, karlijn)

    frans.display_balance()
    karlijn.display_balance()