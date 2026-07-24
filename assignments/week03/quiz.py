# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age <= 12:
    print("child")
elif age  <=19:
    print("Teenager")
elif age <=59:
    print("Adult") 
else:
    print("Senior")       





# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")

balance = 1000
pin = "1234"

enterd_pin = input("Enter PIN: ")

if enterd_pin == pin:
    print("PIN accepted")

    while True:
    print("\n1. check Balance", balance)

elif choice == "2":
    amount = float(input("Enter amount to withdraw:"))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining Balance",balance)
    
    else:
        print("Insufficient balance")

elif choice == "3":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful")
    print("Current Balance:", balance)

elif choice == "4":
    print("Thank you for using the ATM")
    break

else:
   print("Invalid option. Please choose 1-4.")

else:
print("Invalid PIN")
           