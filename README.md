# Banking Management System

A console-based **Banking Management System** built using **Python** and
**MySQL**. This project demonstrates CRUD operations, user
authentication, and database connectivity using
`mysql-connector-python`.

## Features

-   Create Account
-   Login with Account Number and PIN
-   Check Balance
-   Deposit Money
-   Withdraw Money
-   Logout
-   Data stored permanently in MySQL

## Technologies Used

-   Python 3
-   MySQL
-   mysql-connector-python
-   VS Code

## Concepts Practiced

-   Functions
-   Loops
-   Conditional Statements
-   MySQL CRUD Operations
-   Python--MySQL Connectivity

## Database

Table: `accounts`

Fields: - `account_no` - `name` - `pin` - `balance`

## How to Run

1.  Install MySQL and create the database.
2.  Install the MySQL connector:

``` bash
pip install mysql-connector-python
```

3.  Update your database credentials in `database.py`.
4.  Run:

``` bash
python banking_management_system.py
```

## Future Improvements

-   Transaction History
-   Change PIN
-   Fund Transfer
-   Tkinter GUI
-   OOP Version using `BankAccount` class
## Also made a GUI of this using Tinkter
- use the same database file for it
- it will show a user interface through which inputs are taken from windows now instead directly from console
- sending our entry amount to the sql database and it is updated in the database the moment user clicks deposit
## Author

**Vanshika Jain**
