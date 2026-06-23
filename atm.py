attempts=3
pin="1234"
while attempts > 0:
    entered_pin=input("Enter your PIN: ")
    if entered_pin == pin:
        print("Logim Sucess")
        break
    else:
        attempts -= 1
        print("Invalid PIN\nRe-Enter valid PIN")
if attempts == 0:
    print("PLease contact your branch manager")
    exit()
balance=1000
history=[]
while True:
    print("\n1.check balance")
    print("2.Deposit")
    print("3.Withdrawl")
    print("4.Transaction history")
    print("5.Exit")


    choice=int(input("Enter your choice:"))
    if choice ==1:
        print("Balance:  ",balance)
    elif choice==2:
        amount=int(input("Enter amount to deposit: "))
        balance += amount
        history.append(f"Deposited:₹ {amount}")
        print("Amount deposited successfully")
        print(f"Current balance: {balance}")
    elif choice==3:
        amount=int(input("Enter amount to withdraw:  "))
        if amount<=balance:
            balance -=amount
            print("Amount Withdraw sucess")
            history.append(f"withdrawn amount:₹ {amount}")
            print(f"Current balance: {balance}")
        else:
            print("Insufficient amount in account")
    elif choice == 4:
        if len(history) == 0:
            print("No Transactions done yet..")
        else:
            print("Transactions history..\n")
            for i in history:
                print(i)
    elif choice==5:
        print("Sucessfully exited.\nThank you")
        break

    else:
        print("Invalid choice.\nplease Enter valid choice:")