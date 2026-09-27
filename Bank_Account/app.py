
from datetime import datetime

class InsufficientFundsError(Exception):
  pass

class InvalidAmountError(Exception):
  pass

class BankAccount:
  def __init__(self,balance):
    self.balance = balance
    self.load_balance()

  def deposite(self,amount):
    if amount <=0:
      raise InvalidAmountError("Amount must be greater than 0")

    self.balance +=amount
    self.save_balance()
    print("Deposite Successful")

    self.save_transaction(
      f"Deposite: {amount}, Balance: {self.balance}")
    

  def withdraw(self,amount):
    if amount <=0:
      raise InvalidAmountError("Amount must be greater than 0")

    if amount > self.balance:
      raise InsufficientFundsError("Insufficient fund")

    self.balance -=amount
    self.save_balance() # call method
    print("Withdraw Successful")

    self.save_transaction(
      f"Withdraw: {amount}, Balance: {self.balance}")  # call method
    

  def check_balance(self):
    print(f"current balance: {self.balance}")

  # save transaction histry
  def save_transaction(self,transaction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("transactions.txt","a") as file:
      file.write(f"{transaction} - {timestamp}\n")

  # current balance 
  def save_balance(self):
    with open("balance.txt","w") as file:
      file.write(str(self.balance))
    
  # retrive balance
  def load_balance(self):
    try:
      with open ("balance.txt","r") as file:
        self.balance = int(file.read())

    except FileNotFoundError:
      pass

    except ValueError:
      print("Invalid balance file. Using default balance.")



account = BankAccount(1000)

while True:
  print("1.Deposite")
  print("2.Withdraw")
  print("3.Check Balance")
  print("4.Exit")

  try:
    choice = int(input("Choose an option: "))

    if choice == 1:
      amount = int(input("Enter a deposite amount: "))
      account.deposite(amount)

    elif choice == 2:
      amount = int(input("Enter a withdraw amount: "))
      account.withdraw(amount)

    elif choice == 3:
      account.check_balance()

    elif choice == 4:
      print("GoodBye!")
      break

    else:
      print("Invalid choice. Please choose 1-4.")

  except ValueError:
    print("Please enter a valid number.")


  except InvalidAmountError as e:
    print(e)

  except InsufficientFundsError as e:
    print(e)












