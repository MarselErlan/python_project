import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREAETE TABLE customers(name VARCHAR(255), adress VARCHAR(255)")


mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)


mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)")


mycursor.execute("ALTER TABLE   customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



