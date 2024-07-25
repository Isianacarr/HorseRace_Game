

class Player():
    def __init__(self,Name, account):
        self.account = account
        self.name = Name

    def select_horse(self):
        pass

    def make_bid(self):
        bid = int(input("How much would you like to bid?"))
        self.update_account(-bid)

    def update_cash(self, amount):
        self.account = self.account + amount

    def check_balance(self):
        print(self.account)
        return self.account

player = Player(500)
player.make_bid()
player.check_balance()