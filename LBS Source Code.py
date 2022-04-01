import mysql.connector as sqlcon
import random
from tabulate import tabulate
mycon=sqlcon.connect(host='localhost', user='root',password='aps',database = 'mydata')
#MySQL And Python Connectivity
if mycon.is_connected():
	print('Successfully Connected to MySQL database\n')
	print("*"*67)
cur = mycon.cursor()

#Manager
#To Add Book

def Addbook():
	print("*"*28,"ADD BOOK","*"*29,"\n")
	ab=True
	while ab:
		book_n = input("Enter Book Name: ")
		Book_N=book_n.title()
		cur.execute("select * from Books where Book_Name='{}'".format(Book_N))
		nam=cur.fetchall()
		if len(nam)>0:
			print("\nBook Name Is Already Present.")
			print("Enter New Name.\n")
		else:
			book_id = int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(book_id))
			bo=cur.fetchall()
			if len(bo)>0:
				print("\nBook ID Is Present.")
				print("Try Again.\n")
			else:
					book_t=input("Enter Book Type: ")
					book_q =int(input("Enter Quantity Of Books: "))
					Book_T=book_t.title()
					cur.execute("insert into Books values({},'{}','{}',{})".format(book_id,Book_N,Book_T,book_q))
					mycon.commit()
					print("\nBook Added \n")
					anp=input("Do You Want To Add More Records (y/n): ")
					if anp=='y':
						ab=True
					elif anp =='n':
						ab=False
					else:
							print("\nWrong Key.\n")
							ab= False

#To Search A Book

def Search():
	print("*"*26,"Search Book","*"*27,"\n")
	sea=True
	while sea:
		print("1. Search By Book ID\n2. Search By Book Name\n3. Back")
		inpu=int(input("Enter Your Choice: "))
		if inpu==1:
			id = int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(id))
			data = cur.fetchall()
			if len(data)<=0:
				print("\nNo Book With This ID Is Present.")
				print("Back To Main Menu.\n")
				sea = False
			else:
				head = ["Book ID","BookName","BookType","Quantity"]
				print(tabulate(data,headers=head,tablefmt='grid'))
				anp=input("Do You Want To Search More Records (y/n): ")
				if anp=='y':
					sea=True
				elif anp =='n':
					sea=False
				else:
						print("\nWrong Key.\n")
						sea = False
		elif inpu==2:
			nam=input("Enter Book Name: ")
			Nam=nam.title()
			cur.execute("select * from Books where Book_Name='{}'".format(Nam))
			data=cur.fetchall()
			if len(data)<=0:
				print("\nNo Book With This Name Is Present.")
				print("Back To Main Menu.\n")
				sea=False
			else:
				head = ["Book ID","BookName","BookType","Quantity"]
				print(tabulate(data,headers=head,tablefmt='grid'))
				anp=input("Do You Want To Search More Records (y/n): ")
				if anp=='y':
					sea=True
				elif anp =='n':
					sea=False
				else:
						print("\nWrong Key.\n")
						sea = False
		elif inpu==3:
			print("\nBack To Main Menu.\n")
			sea=False
		else:
			print("\nWrong Input\n")
			sea = False

#Delete Book Record

def Delete():
	print("*"*23,"Delete Books Record","*"*23,"\n")
	de=True
	while de:
		print("1.Delete By Book ID\n2. Delete By Book Name\n3. Back\n")
		inpu=int(input("Enter Your Choice(1-2): "))
		if inpu==1:
			id = int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(id))
			data = cur.fetchall()
			if len(data)<=0:
				print("\nNo Book With Book ID",id,"Is Present To Delete.")
				print("Back To Menu.\n")
				de = False
			else:
				cur.execute("delete from Books where Book_ID={}".format(id))
				print("Book ID",id,"Is Deleted.\n")
				mycon.commit()
				anp=input("Do You Want Delete More Records (y/n): ")
				if anp=='y':
					de=True
				elif anp =='n':
					de=False
				else:
						print("\nWrong Key.\n")
						de = False
		elif inpu==2:
			nme= input("Enter Book Name: ")
			Nme=nme.title()
			cur.execute("select * from Books where Book_Name='{}'".format(Nme))
			data = cur.fetchall()
			if len(data)<=0:
				print("\nNo Book With Name",Nme,"Is Present To Delete.")
				print('Back To Menu.\n')
				de=False
			else:
				cur.execute("delete from Books where Book_Name='{}'".format(Nme))
				print(nme,"Is Deleted.\n")
				mycon.commit()
				anp=input("Do You Want To Delete More Records (y/n): ")
				if anp=='y':
					de=True
				elif anp =='n':
					de=False
				else:
						print("Wrong Key.\n")
						de = False

		elif inpu==3:
			print("Back")
			de = False
		else:
			print("\nWrong Input\nTry Again \n")


def Showbook():
	print("*"*20,"Showing All Book Records","*"*21,"\n")
	cur.execute("select * from Books")
	data = cur.fetchall()
	if len(data)<=0:
		print("No Books To Show.\n")
	else:
		head=["Book ID", "Book Name", "Book Type","Quantity"]
		print(tabulate(data, headers=head, tablefmt='grid'))
		anp=input("Do You Want To Group It By Type(y/n): ")
		if anp=='y':
				inpu=input("Enter Book Type: ")
				Inpu=inpu.title()
				cur.execute("select Book_ID, Book_Name from Books where Type='{}'".format(Inpu))
				data=cur.fetchall()
				if len(data)<=0:
					print("No Book With This Type Is Present.\n")
				else:
					head = ["Book ID", "Book Name"]
					print(tabulate(data,headers = head,tablefmt = 'grid'))
		elif anp =='n':
					print("\nYou Can Proceed Further.\n")
		else:
						print("\nWrong Key.\n")
		
				
#Update Book ID,Book Name, Book Type

def Update():
	print("*"*23,"Update Book Records","*"*23,"\n")
	upd= True
	while upd:
		print("\n 1. Update Book Name\n 2. Update Book ID\n 3. Update Book Type\n 4. Update Book Quantity\n 5. Back\n")
		inpu=int(input("Enter Your Choice: "))
		if inpu==1:
			id = int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(id))
			data = cur.fetchall()
			if len(data)<=0:
				print("\nNo Such Record Is Present To Update.\n")
				upd = False
			else:
				n = input("Enter Updated Book Name: ")
				N=n.title()
				cur.execute("select * from Books where Book_Name='{}'".format(N))
				if len(cur.fetchall())<=0:
					cur.execute("update Books set Book_Name='{}' where Book_id={}".format(N,id))
					print("\nRecord Updated.\n")
					mycon.commit()
					anp=input("Do You Want To Update More Records (y/n): ")
					if anp=='y':
						upd=True
					elif anp =='n':
						upd=False
					else:
						print("\nWrong Key.\n")
						upd = False
				else:
					print("Book Name Is Already Present.")
					upd = False
		elif inpu==2:
			nam=input("Enter Book Name: ")
			Nam = nam.title()
			cur.execute("select * from Books where Book_Name='{}'".format(Nam))
			data=cur.fetchall()
			if len(data)<=0:
				print("\nNo Record To Update.\n")
				upd= False
			else:
				ID =int(input("Enter Updated Book ID: "))
				cur.execute("select * from Books where Book_ID={}".format(ID))
				d = len(cur.fetchall())
				if d<=0:
					cur.execute("update Books set Book_ID={} where Book_Name='{}'".format(ID,Nam))
					print("\nRecord Updated.\n")
					mycon.commit()
					anp=input("Do You Want To Update More Records (y/n): ")
					if anp=='y':
						upd=True
					elif anp =='n':
						upd=False
					else:
						print("\nWrong Key.\n")
						upd = False
				else:
					print('\nBook ID Is Already Present.\n')
					upd=False
		elif inpu==3:
			ID = int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(ID))
			d = len(cur.fetchall())
			if d<=0:
				print("\nNo Record Is Present.\n")
				upd=False
			else:
				ty=input("Enter Updated Type Of Book: ")
				Ty=ty.title()
				cur.execute("update Books set Type='{}' where Book_ID={}".format(Ty,ID))
				print("\nRecord Updated.\n")
				mycon.commit()
				anp=input("Do You Want To Update More Records (y/n): ")
				if anp=='y':
					upd=True
				elif anp =='n':
					upd=False
				else:
					print("Wrong Key.")
					upd = False
				
		elif inpu==4:
			id=int(input("Enter Book ID: "))
			cur.execute("select * from Books where Book_ID={}".format(id))
			li=cur.fetchall()
			if len(li)<=0:
				print("\nNo Book With Book ID",id,"Is Present.")
			else:
				qu=int(input("Enter Updated Quantity Of Book: "))
				cur.execute("update Books set Quantity={} where Book_ID={}".format(qu,id))
				print("\nRecord Updated.\n")
				mycon.commit()
				anp=input("Do You Want To Update More Records (y/n): ")
				if anp=='y':
					upd=True
				elif anp =='n':
					upd=False
				else:
					print("\nWrong Key.\n")
					upd = False
		elif inpu==5:
			print("\nExit\n")
			upd=False
		else:
			print("\nWrong Key.\n")
			upd=False

#Show Lender's Record

def Show_IB():
	print("*"*23,"Showing Issued Book","*"*23,"\n")
	cur.execute("select * from Lender")
	data = cur.fetchall()
	if len(data)<=0:
		print("\nNo Record To Show.\n")
	else:
		head =["Student ID", "Student Name","BookID","LendingDate","ReturningDate","Fine"]
		print(tabulate(data,headers=head,tablefmt='grid'))
		ss=int(input("To Get Details About Student Press 1 else Press 0 To Continue: "))
		if ss==1:
			search=True
			while search:
				id=int(input("Enter Student ID: "))
				cur.execute("select * from StuRec where ID={}".format(id))
				data=cur.fetchall()
				head=["ID","Name","Email","Phone Number"]
				print(tabulate(data,headers=head,tablefmt='grid'))
				ans=input("Do You Want To Search More Data(y/n): ")
				if ans=='y':
					search=True
				elif ans=='n':
					search = False
				else:
					print("\nWrong Key\n")
					search = False
		elif ss== 0:
			print("\nContinue\n")
		else:
			print("\nWrong Key\n")
def MSRec():
	print("*"*21,"Managing Student Record","*"*21,"\n")
	ms = True
	while ms:
		print("1. Add Student Data\n2. Delete Student Data\n3. Back\n")
		inpu=int(input("Enter Your Choice (1-2): "))
		if inpu==1:
			arec=True
			while arec:
				na=input("Enter Your Name: ")
				Na=na.title()
				mail = input("Enter Your Email ID: ")
				ph = int(input("Enter Phone Number: "))
				a= random.randint(1,9)
				b=random.randint(1,9)
				c=a= random.randint(1,9)
				co=(a,b,c)
				a=list(co)
				random.shuffle(a)
				x =str(a[0])
				y=str(a[1])
				z=str(a[2])
				c=x+y+z
				rt=int(c)
				print("Student's ID Is",rt)
				cur.execute("insert into StuRec (ID, Name,Email,Phone_Number) values({},'{}','{}',{})".format(rt,Na,mail,ph))
				mycon.commit()
				print("\nNew Record Added\n")
				anp=input("Do You Want To Add more Records (y/n): ")
				if anp=='y':
					arec=True
				elif anp =='n':
					arec=False
				else:
					print("\nWrong Key.\n")
					arec= False
		elif inpu==2:
			der = True
			while der:
				id = int(input("Enter Student ID: "))
				cur.execute("select * from StuRec where ID={}".format(id))
				data = cur.fetchall()
				if len(data)<=0:
					print("\nNo Record To Delete.")
					print("Back To Menu.\n")
					der = False
				else:
					cur.execute("delete from StuRec where ID={}".format(id))
					mycon.commit()
					print("Student ID",id,"Is Deleted.\n")
					anp=input("Do You Want To Delete more Data (y/n): ")
					if anp=='y':
						der=True
					elif anp =='n':
						der=False
					else:
						print("\nWrong Key.\n")
						der= False
		else:
			print("\nBack\n")
			print()
			ms =False			

#Student
#Issue Book

def lend():
	cur.execute("select Book_ID, Book_Name,Type from Books")
	data = cur.fetchall()
	head = ["Book ID",'BookName',"Book Type"]
	print(tabulate(data,headers=head,tablefmt="grid"))
	inpu = int(input("Enter Book ID: "))
	cur.execute("select * from Books where Book_ID ={}".format(inpu))
	inp = cur.fetchall()
	if len(inp)<=0:
		print("\nNo Book With This ID Is Present.")
		print("Try Agai\n")
	else:
		cur.execute("select Quantity from Books where Book_ID={}".format(inpu))
		data = cur.fetchone()
		m=list(data)
		n=m[0]
		if n>0:
			name = input("Enter Student Name: ")
			Name=name.title()
			sid = int(input("Enter Student ID: "))
			cur.execute("select Name from StuRec where ID={}".format(sid))
			me = cur.fetchall()
			if len(me)<=0:
				print("\nYou Entered Wrong ID Or Name.\n")
			else:
							bo=True
							while bo:
								try:
									query=("insert into Lender (ID,Name,Book_ID,L_Date,R_Date,Fine) values({},'{}',{},curdate(),curdate()+7,0)".format(sid,Name,inpu))
									cur.execute(query)
									mycon.commit()
									cur.execute("update Books set Quantity={} where Book_ID ={}".format(n-1,inpu))
									mycon.commit()
									print("Book Issued\nCollect It From Librarian\n")
									cur.execute("select R_Date from Lender where ID={}".format(sid))
									date = cur.fetchone()
									print("You ",Name,"Issued Book ID ",inpu,"Returning Date Is ",date[0])
									print("Return Book On Time Otherwise Rs.2/day Fine Will Be Collected.")
									break
								except sqlcon.errors.IntegrityError:
									print("\nYou Are Not Allowed To Borrow Book.")
									print("You Already Issued A Book.")
									print("Back To Menu\n")
									bo=False
							
			
		else:
			print("Book Not Available.\n")

def Return():
	sid=int(input("Enter Your ID: "))
	nam=input("Enter Your Name: ")
	cur.execute("select* from Lender where(ID={} AND Name='{}')".format(sid,nam))
	data = cur.fetchall()
	if len(data)<=0:
		print("ID Or Name Doesn't Match With The Record.\n")
	else:
		cur.execute("select Book_ID from Lender where ID ={}".format(sid))
		bid=cur.fetchone()
		cur.execute("delete from Lender where ID={}".format(sid))
		cur.execute("update Books set Quantity=Quantity+1 where Book_ID={}".format(bid[0]))
		mycon.commit()
		print("\n Book Returned \n")
		print("Submit Book To librarian.\t")

#Calculate Fine

def fc():
	print("*"*27,"Show Fine","*"*27,"\n")
	id=int(input("Enter Your ID:"))
	cur.execute("select ID from StuRec")
	pp=cur.fetchall()
	if len(pp)>0:
		cur.execute("select * from Lender where ID={}".format(id))
		lf=cur.fetchall()
		if len(lf)>0:
			cur.execute("select Book_ID,R_Date,Fine from Lender where ID={}".format(id))
			ipo=cur.fetchall()
			print("\nYou Issue Book With Book ID: ",ipo[0][0])
			print('Your Returning Date Is: ',ipo[0][1])
			print("Your Fine Is: ",ipo[0][2],"\n")
#Updating Fines
def update():
			cur.execute("select ID from Lender")
			ch=cur.fetchall()
			for i in ch:
				po=i[0]
				cur.execute("select L_Date from Lender where ID={}".format(po))
				b=cur.fetchall()
				cur.execute("select R_Date from Lender where ID={}".format(po))
				rd=cur.fetchall()
				cur.execute("select curdate()")
				cd=cur.fetchall()
				if cd[0][0]>=b[0][0] and cd[0][0]<=rd[0][0]:
					cur.execute("update Lender set Fine={} where ID={}".format(0,po))
				elif cd[0][0]>b[0][0] and cd[0][0]>rd[0][0]:
					b=nod(rd[0][0],cd[0][0])
					fine=b*2
					cur.execute("update Lender set Fine={} where ID={}".format(fine,po))
					mycon.commit()
				
	
def nod(date_1, date_2):
       return (date_2 - date_1).days 
#Main Program

update()
print("*"*64,":)")
print(" \t \t Welocome To Library Management System \t \t")
print("*"*64,":)")
print("Library Menu")
menu = True
while menu:
	print("\n 1. Manager \n 2. Student \n 3. Exit \n")
	a=int(input("Enter Your Choice (1-3):"))
	if a == 1:
		id=input("Enter Your ID: ")
		pa = int(input("Enter Your Password: "))
		if id == "Keshav":
			if pa ==1230:
				print("Login Successfull.")
				manage=True
				while manage:
					print("\n 1. Add Book Record \n 2. Show All Book Record \n 3. Search Book Record \n 4.Update Book Record \n 5. Deletion Book Record\n 6. Show Issued Book Data\n 7. Manage Student Record\n 8. Exit/Back\n")
					b = int(input("Enter Your Choice (1-7): "))
					if b ==1:
						Addbook()
					elif b ==2:
						Showbook()
						
					elif b == 3:
						Search()
					elif b == 4:
						Update()
					elif b == 5:
						Delete()
					elif b==6:
						Show_IB()
					elif b==7:
						MSRec()
					elif b==8:
						print("Back/Exit")
						manage = False
					else:
						print("WRONG KEY")
						
		elif id!="Keshav":
			print("Invalid ID or Password.")
			menu= False
		elif pa!= 1230:
			print("Invalid Password Or ID")
			menu = False
	elif a==2:
		stu = True
		while stu:
			print("\n 1. Request A Book \n 2. Return A Book \n 3. Fine Calculator \n 4. Back")
			z=int(input("Enter Your Choice(1-3): "))
			if z==1:
				lend()
			elif z==2:
				Return()
			elif  z==3:

				fc()
			elif z==4:
				print("Back\n")
				stu=False
			else:
				print("WRONG KEY")
			
	elif a==3:
		print("Exited")
		menu=False
	else:
		print("\nWRONG KEY\nYou Are EXITED...")
		menu = False
