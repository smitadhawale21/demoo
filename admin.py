from lms import Lms
from libraryms import LibMgmt
def adminMenu():
    libraryms=LibMgmt()
    ch=0
    while(ch!=10):
        print('''
            1.Add Books
            2.Show all books
            3.Search book by Id
            4.Search book by book name
            5.Delete book by Id
            7.Edit book by Id
            8.Edit book by book name
            10.Exit
        ''')
        ch=int(input(" Enter your chioce: "))
        if(ch==1):
            id=int(input("Enter book id: "))
            name=input("Enter book name: ")
            author=input("Enter book author: ")
            a=Lms(id, name, author,status=1)
            libraryms.addBook(a)
        elif(ch==2):
            libraryms.showbook()
        elif(ch==3):
            id=input("Enter book id to search ")
            libraryms.searchbook(id)
        elif(ch==4):
            name=input("Enter book name to search ")
            libraryms.searchBookbyName(name)
        elif(ch==5):
            id=input("Enter book id to edit ")
            libraryms.deletebookbyId(id)
        elif(ch==7):
            id=input("Enter book id to edit ")
            libraryms.editBookbyId(id)
        elif(ch==8):
            name=input("Enter book name to edit ")
            libraryms.editBookbyName(name)

        
        elif(ch==10):
            print("Thank you..")
        else:
            print("Invalid Credentials...")
if(__name__ == "__main__"):
    adminMenu()