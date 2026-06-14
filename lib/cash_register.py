#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append((item, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            item, price, quantity = self.previous_transactions.pop()
            self.total -= price * quantity
            self.items = self.items[:-quantity]
        else:
            print("There is no transaction to void.")