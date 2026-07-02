import mysql.connector
conn=mysql.connector.connect(
    host="localhost",   
    user="root",
    password="Bu@#1234",
    database="banking_management_sytem")
cursor=conn.cursor()
print("connection successful")