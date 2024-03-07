import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9711",
    database="testdb"
    )
mycursor = mydb.cursor()

def Update(old_username,old_password):
    username = input("Enter new username : ")
    email = input("Enter new email-id : ")
    password = input("Enter new password : ")
    mycursor.execute("UPDATE Auth SET Username = %s, Email = %s, U_Password = %s WHERE Username = %s AND U_Password = %s",(username,email,password,old_username,old_password))
    mydb.commit()
    print("Data Updated Successfully")

# =========LOGIN===========
def login():

    username = input("Enter username : ")
    password = input("Enter password : ")
    mycursor.execute("SELECT * FROM Auth where Username = %s AND U_Password = %s",(username,password))
    result=mycursor.fetchall()
    if result:
        print("User logged in\nDo you want to see your details?Y/N")
        decision=input()
        if decision=="Y":
            print(result)
            print("Do you want to update your details?Y/N")
            u_decision=input()
            if u_decision=="Y":
                Update(username,password)
        elif decision=="N":
            print("Do you want to update your details?Y/N")
            u_decision=input()
            if u_decision=="Y":
                Update(username,password)
        else :
            print("Invalid token")
    else:
        print("Data not found..... Do u want to register to our systems? Y/N")
        decision = input()
        if decision == "Y":
            register()
        else:
            print("Exiting the Application")        
            
# ============REGISTRATION==============
def register():
    username = input("Enter username : ")
    email = input("Enter email-id : ")
    password = input("Enter password : ")
    mycursor.execute("INSERT INTO Auth (Username,Email,U_Password) VALUES (%s,%s,%s)",(username,email,password))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print("Do you want to log in?Y/N")
    decision=input()
    if decision=="Y":
        login()
    

print("How do u want to proceed ?\n1. Login \n2. Register")
path=int(input())
if(path==1):
    login()
elif(path==2):
    register()
else:
    print("invalid token")


