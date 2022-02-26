class ATM(object):
  """
    blueprint for ATM
  """

  def __init__(self, CashWithdrawal, BalanceEnquiry, CashRegister):
    self.CashWithdrawal = CashWithdrawal
    self.BalanceEnquiry = BalanceEnquiry
    self.CashRegister = CashRegister

  def start(self):
    print("Cash Registered")

  def stop(self):
    print("Cash Withdrawed")

  def enquiry(self):
    print("Balance is 500$")

Pranav = ATM(60,1500,75)
thing = ATM(70, 800,80)

print(thing.start())
print(Pranav.enquiry())