print("Welcome to ATM")
balance = 100000
correct_pin = "9926"

pin = input("Enter pin ")
if pin != correct_pin:
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
                  print("Current Balance:", balance)  
              elif n == 2:
                  new_amount = int(input("Enter Amount: "))
                  if new_amount < 0:
                      print("Negative Amount Could Not Be Deposit!!")
                  else:    
                      balance = balance + new_amount
              elif n == 3:
                  new_draw = int(input("Enter Amount: "))
                  if new_draw < 0:
                      print("Please Enter a Suitable Amount !!")
                  elif new_draw > balance:
                      print("There is not enough Balance !")    
                  else:    
                     balance = balance - new_draw
              else:
                  print("invalid Input !") 
          else:
              print("Please Enter Appropriate choice")        