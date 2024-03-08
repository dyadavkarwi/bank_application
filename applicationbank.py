#Banking application
acountNo = 0
CusName = ""
BCode = ""
Mobile = 0
Bal = 0

def createAccount():
    global acountNo, CusName, BCode, Mobile, Bal
    acountNo = int(input("Enter account number:"))
    CusName = input("Enter Name:")
    BCode = input("Enter branch code:")
    Mobile = int(input("Enter mobile number:"))
    Bal = int(input("Enter current Balance:"))

def showAccountDetails():
    print("Account No:", acountNo)
    print("Customer Name:", CusName)
    print("Branch Code:", BCode)
    print("Mobile number:", Mobile)

def deposit(amount):
    global Bal
    Bal += amount
    checkBalance()

def withdraw(amount):
    global Bal
    Bal -= amount
    checkBalance()

def checkBalance():
    print("Current Balance:", Bal)

# Main------------------------->
ch1 = 'y'
while ch1 == 'y':
    print("\t========================")
    print("\t BANK MANAGEMENT SYSTEM")
    print("\t========================")
    print("1. Create account\n2. Withdraw\n3. Deposit\n4. Check balance")
    print("\tSelect Your Option (1-4)")
    ch = int(input("\tEnter your choice : "))
    if ch == 1:
        createAccount()
    elif ch == 2:
        amnt = int(input("Enter amount to withdraw:"))
        withdraw(amnt)
    elif ch == 3:
        amnt = int(input("Enter amount to deposit:"))
        deposit(amnt)
    elif ch == 4:
        checkBalance()
    else:
        print("Please select any option available above")
    ch1 = input("Do you want to continue operation? Press 'y':")
