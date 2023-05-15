from admin import adminMenu
from user import userMenu

#if( __name__ == " __main__"):
print(''' 1.Admin Menu 
 2.User Menu
              ''')
        
ch=int(input(" Enter your choice: "))
if(ch==1):
    uname=input("Enter Admin name: ")
    passwd=input("Enter password: ")
    if(uname=="Admin" and passwd=="Admin123"):
        adminMenu()
    else:
        print(" Invalid Credentials..")
elif(ch==2):
    username=input("Enter user name: ")
    passwd=input("Enter password: ")
    if(username=="User" and passwd=="User123"):
        userMenu()
    else:
        print(" Invalid Credentials..")