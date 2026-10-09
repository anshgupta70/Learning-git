print("Welcome to ATM")
balance = 100000

print("1 to check balance")
print("2 to deposit money")
print("3 to withdraw money")
print("4 to Exit")
while True:
      n = int(input("Write Your Choice: "))
      
      if n == 4:
          print("Exiting ATM....")
          break   
      elif n == 1:
          print("Current Balance = ",balance)
      elif n == 2:
          new_amount = int(input("Enter Amount: "))
          balance = balance + new_amount
      elif n == 3:
          new_draw = int(input("Enter Amount: "))
          balance = balance - new_draw
      else:
          print("invalid Input !") 