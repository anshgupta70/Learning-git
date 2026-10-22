balance = 100000
print("Welcome to ATM")
correct_pin = "9926"
def check_balance():    
    print("Current Balance:",balance)


def deposit(new_amount):
    global balance
    if new_amount <= 0:
        print("The Amount Should be greater than Zero !")
        return

    balance = balance + new_amount

    print(f"₹{new_amount} deposited successfully.")
    print(f"Current balance: ₹{balance}") 

def withdraw(amount):
    global balance

    if amount <= 0:
        print("Amount Should be greater than zero  !")
        return

    if amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance}")
    else:
        print("Insufficient balance.")


def valid_attempts(correct_pin):
    counter = 0
    while counter < 3:
        pin = input("Enter pin ")
        if correct_pin == pin:
            return True
        
        counter += 1
    return False    

if  not valid_attempts(correct_pin):
    print("Login Failed Access Denied!")
    
else:
    print("login Successfull!!")    


    print("1 to check balance")
    print("2 to deposit money")
    print("3 to withdraw money")
    print("4 to Exit")
    while True:
          try:
             n = int(input("Write Your Choice: "))
          except ValueError:
             print("Please Write a Suitable choice!")
             continue    
          if  1 <= n <=4:
              
              if n == 4:
                  print("Exited ATM")
                  break   
              elif n == 1: 
                   check_balance() 
              elif n == 2:
                  try:
                     new_amount = int(input("Enter Amount: "))
                  except ValueError:
                      print("please Enter a valid Amount !")
                      continue
                  deposit(new_amount)
              elif n == 3:
                  new_draw = int(input("Enter Amount: "))
                  withdraw(new_draw)
              
          else:
              print("Please Enter Appropriate choice")        