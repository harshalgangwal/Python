Account_Balance = int(input("Enter the Account Balance: "))
flag = True
while flag:
    Withdrawal_Amount = int(input("Enter The Amount which you want to withdraw: "))
    if Account_Balance > Withdrawal_Amount:
        if Withdrawal_Amount % 10 == 0:
            Account_Balance = Account_Balance - Withdrawal_Amount
            print("After Withdrawal Account Balance is ", Account_Balance)
        else:
            print("Withdrawal Amount Should be Multiple of 10")
    else:
        print("Insufficient Balance")
    Answer = int(input("Enter 1 or withdraw more amount else Enter 0 for Exit"))
    if Answer==1:
        flag = True
    else:
        print("Thank You! Have a Nice day")
        flag = False