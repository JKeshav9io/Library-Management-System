import mysql.connector as sqlcon
mycon=sqlcon.connect(host='localhost', user='root',password='aps',database = 'mydata')
#MySQL And Python Connectivity
if mycon.is_connected():
	print('Successfully Connected to MySQL database\n')
	print("*"*67)
cur = mycon.cursor()

cur.execute("create table StuRec (ID int(3),Name varchar(30),Email varchar(50),Phone_Number bigint(10))")
cur.execute("create table Books (Book_ID int(3),Book_Name varchar(50),Type char(20),Quantity int)")
cur.execute("create table Lender (ID int(3),Name char(20),Book_ID int,L_Date date,R_Date date,Fine int)")
mycon.commit()
print("TABLE CREATED")
