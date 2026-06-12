#!/usr/bin/env python3

class CashRegister:
  def init(self,discount=0,total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
      return self._discount
  @discount.setter
  def discount(self,value):
      if isinstance(value,int) and 0 <= value <= 100:
        self._discount = value
      else: 
        print("Not valid discount")

  def add_item(self,item,price,quantity = 1):
      self.total += pricequantity
      self.items += [item]quantity
      self.previous_transactions.append((item,price,quantity))

  def apply_discount(self):
      if self._discount > 0:
        self.total -= self.total*(self._discount/100)
        print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
        print("There is no discount to apply.")

  def void_last_transaction(self):
      ln = len(self.previous_transactions)
      if ln != 0 :
        self.total -= (self.previous_transactions[ln-1][1]*self.previous_transactions[ln-1][2])
        self.previous_transactions.pop()
      else:
        print("There is no transaction to void.")