# (State Interface)

from abc import ABC, abstractmethod

class AccountState(ABC):
  @abstractmethod
  def handle(self, account):
    pass

  @abstractmethod
  def next_state(self, account):
     pass





#(Concrete States)


class OpenState(AccountState):
  def handle(self, account):
    print("حساب باز است. بررسی مدارک.")
    # منطق برای بررسی مدارک
    if account.documents_complete:
      account.state = ActiveState()
    else:
      print("مدارک ناقص است. حساب نمیتواند فعال شود.")

  def next_state(self, account):
    if account.documents_complete:
       account.state = ActiveState()
    else:
       print("مدارک ناقص است. حساب نمیتواند فعال شود.")

#حالت Active (فعال)
class ActiveState(AccountState):
   def handle(self, account):
     print("حساب فعال است. بررسی موجودی.")
     # منطق برای بررسی موجودی
     if account.balance == 0:
        account.state = DormantState()
     elif account.balance < -500:
        account.state = ClosedState()

   def next_state(self, account):
      if account.balance == 0:
         account.state = DormantState()
      elif account.balance < -500:
          account.state = ClosedState()

#حالت Dormant (راکد)
class DormantState(AccountState):
    def handle(self, account):
     print("حساب راکد است. بررسی موجودی.")
     # منطق برای بررسی موجودی
     if account.balance > 0:
        account.state = ActiveState()
     elif account.balance < -500:
       account.state = ClosedState()

    def next_state(self, account):
        if account.balance > 0:
          account.state = ActiveState()
        elif account.balance < -500:
          account.state = ClosedState()

#حالت Closed (بسته)
class ClosedState(AccountState):
        def handle(self, account):
           print("حساب بسته شده است.")

        def next_state(self, account):
           print("حساب در حالت بسته است. هیچ انتقالی وجود ندارد.")

#(Context)



class Account:
   def __init__(self, balance, documents_complete):
     self.balance = balance
     self.documents_complete = documents_complete
     self.state = OpenState()

   def process(self):
     self.state.handle(self)
     self.state.next_state(self)



# Use


account = Account(balance=100, documents_complete=True)
account.process()  # حساب باز است. بررسی مدارک.
account.process()  # حساب فعال است. بررسی موجودی.
account.balance = 0
account.process()  # حساب راکد است. بررسی موجودی.
account.balance = -600
account.process()  # حساب بسته شده است.
