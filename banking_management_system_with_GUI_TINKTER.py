import tkinter as tk

root = tk.Tk()
root.title("Bank Management System")
root.geometry("500x500")

from database import conn , cursor
from tkinter import messagebox

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Account Number").pack()
acc_entry = tk.Entry(root)
acc_entry.pack()

tk.Label(root, text="PIN").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

def create_account():
    name=name_entry.get()
    acc=acc_entry.get()
    pin=pin_entry.get()
    cursor.execute(
        "SELECT * FROM accounts WHERE account_no=%s", (acc,)
                   )
    account=cursor.fetchone()
    if account:
        messagebox.showinfo("account already exists")
    else:
        cursor.execute(
            "INSERT INTO accounts (name , account_no , pin , balance) VALUES (%s , %s , %s , %s)",(name , acc , pin , 0)

        )
        conn.commit()
        messagebox.showinfo("Account created successfully")

# functions after login
def check_balance(acc):
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=%s", (acc,)
    )
    balance=cursor.fetchone()
    messagebox.showinfo("Balance", f"Your balance is: {balance[0]}")
def deposit_window(acc): ## hume new window kholni hai deposit ki
    deposit_page=tk.Toplevel(root) ## new window kholdi
    deposit_page.title("deposit")## upr ye text aa gya
    tk.Label(deposit_page , text="Enter amount to deposit").pack() ## ye lavbel hai ki kya kaam krna hai niche
    amount_entry=tk.Entry(deposit_page)## yha pe apna amount likhdo
    amount_entry.pack()
    tk.Button(
    deposit_page,
    text="Deposit",
    command=lambda: deposit(acc, amount_entry)
).pack()

def deposit(acc,amount_entry):
    amount=int(amount_entry.get()) ## amount entry ka text box in tkinter
    cursor.execute(
        "UPDATE accounts SET balance=balance+%s WHERE account_no=%s", (amount , acc))
    conn.commit()
    messagebox.showinfo("Deposit successful.")
def withdraw_window(acc):
    withdraw_page=tk.Toplevel(root)
    withdraw_page.title("withdraw")
    tk.Label(withdraw_page , text="Enter amount to withdraw").pack()
    amount_entry=tk.Entry(withdraw_page)
    amount_entry.pack()
    tk.Button(
    withdraw_page,
    text="Withdraw",
    command=lambda: withdraw(acc, amount_entry)
).pack()
def withdraw(acc,amount_entry):
    amount=int(amount_entry.get())
    cursor.execute(
             "SELECT balance FROM accounts WHERE account_no=%s", (acc,)
             )
    balance=cursor.fetchone()
    if balance[0]<amount:
        messagebox.showinfo("Insufficient balance.")
    else:
        cursor.execute(
            "UPDATE accounts SET balance=balance-%s WHERE account_no=%s", (amount , acc))
        conn.commit()
        messagebox.showinfo("Withdrawal successful.")
def login():
    acc=acc_entry.get()
    pin=pin_entry.get()
    cursor.execute(
        "SELECT *FROM accounts WHERE account_no=%s AND pin=%s", (acc , pin)
   )
    user=cursor.fetchone()
    if user:
        messagebox.showinfo("Login successful")
        dashboard = tk.Toplevel(root)
        dashboard.title("Dashboard")
        tk.Button(dashboard, text="Check Balance", command=lambda:check_balance(acc)).pack()
        tk.Button(dashboard, text="Deposit", command=lambda:deposit_window(acc)).pack()
        tk.Button(dashboard, text="Withdraw", command=lambda:withdraw_window(acc)).pack()
        tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack()
        
            
    else:
       messagebox.showinfo("Invalid account number or pin. Please try again.")  

def exit_app():
     messagebox.showinfo("Exit", "Thank you for using the Banking Management System.")
     root.destroy()

tk.Button(root,
          text="Create Account",
          command=create_account).pack()

tk.Button(root,
          text="Login",
          command=login).pack()
tk.Button(root,
          text="Exit",
          command=exit_app).pack()

root.mainloop()
