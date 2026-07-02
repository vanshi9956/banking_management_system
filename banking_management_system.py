from test import conn , cursor
def create_account():
    name=input("Enter your name: ")
    acc=input("Enter your account number: ")
    pin=input("Enter your pin: ")
    cursor.execute(
        "SELECT * FROM accounts WHERE account_no=%s", (acc,)
                   )
    account=cursor.fetchone()
    if account:
        print("Account number already exists. Please try again.")
    else:
        cursor.execute(
            "INSERT INTO accounts (name , account_no , pin , balance) VALUES (%s , %s , %s , %s)",(name , acc , pin , 0)

        )
        conn.commit()
        print("Account created successfully")

def login():
    acc=input("Enter you account number: ")
    pin=input("enter you pin: ")
    cursor.execute(
        "SELECT *FROM accounts WHERE account_no=%s AND pin=%s", (acc , pin)
   )
    user=cursor.fetchone()
    if user:
        print("login successful")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        
        while True:
                choice=input("Enter your choice: ")
            
                if choice=="1":
                    cursor.execute(
                        "SELECT balance FROM accounts WHERE account_no=%s", (acc,)
                    )
                    balance=cursor.fetchone()
                    print("Your balance is: ", balance[0])
                elif choice=='2':
                    
                        cursor.execute(
                            "UPDATE accounts SET balance=balance+%s WHERE account_no=%s", (amount , acc))
                        conn.commit()
                        print("Deposit successful.")
                elif choice=='3':
                    amount=int(input("enter amount to withdraw: "))
                    
                    cursor.execute(
                             "SELECT balance FROM accounts WHERE account_no=%s", (acc,)
                             )
                    balance=cursor.fetchone()
                    if balance[0]<amount:
                        print("Insufficient balance.")
                    else:
                        cursor.execute(
                            "UPDATE accounts SET balance=balance-%s WHERE account_no=%s", (amount , acc))
                        conn.commit()
                
                    print("Withdrawal successful. New balance is: ", user['balance'])
                    
                elif choice=='4':
                    print("Logout successful")
                    break      
    else:
        print("Invalid account number or pin. Please try again.")        

while True:
    print("WELCOME TO THE BANKING MANAGEMENT SYSTEM")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice=input("Enter your choice: ")
    if choice=='1':
        create_account()
       
    elif choice=='2':
        login()
    elif choice=='3':
        print("Thank you for using the Banking Management System.")
        break
    else:
        print("Invalid choice. Please try again.")