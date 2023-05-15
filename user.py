from libraryms import LibMgmt
from lms import Lms
from libraryms import issue_Book
def userMenu():
    libraryms=LibMgmt()
    ch=2

    while(ch!=5):
        print('''
              1.show  all books 
              2.search book by Id
              3.Issue the Book
              4.Return the Book
              5.exit''')
        ch=int(input("Enter your choice:"))    
        if (ch==1):
            libraryms.showbook()
        elif (ch==2):
            id=input("Enter book ID to search ")
            libraryms.searchbook(id)
    
        elif (ch==3):
            id=input("Enter the Id of the book:")
            libraryms.issue_Book(id)

        elif (ch==4):
            id=input("Enter the id of the book to Return:")
            libraryms.returnBook(id)
        elif (ch==5):
           print("Exit")


        
        
if(__name__=="__main__"):
    userMenu() 
