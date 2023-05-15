from datetime import datetime 
from os import path
from lms import Lms

class LibMgmt:

    def addBook(self,b):
        fp=open("bookinfo.txt","a")
        fp.write(str(b))
        fp.write("\n")
        fp.close()
    def showbook(self):
        try:
            fp=open("bookinfo.txt","r")
        except:
            print(" file not found..")
        else:
            data=fp.read()
            print(data)

    def searchBookbyName(self,book_name):
        if(path.exists("bookinfo.txt")):
            with open("bookinfo.txt","r") as fp:
                flag=False
                for line in fp:
                    data=line.split(" , ")
                    #if(data[1] == book_name):
                    if(book_name in line):
                        print("Record found.\n",data)
                        flag=True
                        break
                #else:
            if(flag==False):
                    print("Record not found...")
        else:
            print("file not found..")

    def editBookbyId(self,id):
            Booklist=[]
            flag=False
            if(path.exists("bookinfo.txt")):
                with open("bookinfo.txt", "r") as fp:
                   for line in fp:
                        data=line.split(",")
                        if(id in line):
                            print("Record found",line.strip())
                            flag=True
                            ans=input("Do you want to cahnge Book name?(y/n): ")
                            if(ans.lower()=='y'):
                                data[1]=input("Enter the new Book name: ")
                                data[2]=input("Enter the Author name: ")
                            line=','.join(data)
                            line+='\n'
                        Booklist.append(line)
                if(flag==True):
                    with open("bookinfo.txt", "w") as fp:
                        for book in Booklist:
                            fp.write(book)
                else:
                    print("Record not found")                        
            else:
                print("File does not exist")  


    def editBookbyName(self,book_name):
        booklist=[]
        flag=False
        if(path.exists("bookinfo.txt")):
            with open("bookinfo.txt","r") as fp:
               
                for line in fp:
                
                    data=line.split(",")
                    if(book_name in line):
                        print("Record found.\n",line)
                        flag=True
                        ans=input(" Do you wish to change book name?(y/n):")
                        if(ans.lower()=='y'):
                            data[1]=input("Enter book name")
                        ans=input(" Do you wish to change book author name?(y/n):")
                        if(ans.lower()=='y'):
                            data[2]=input("Enter book author name")
                            line=",".join(data)
                            line += "\n"
                            
                        booklist.append(line)
                        print(booklist)
                
            if(flag==False):
                    print("Record not found...")
            else:
                with open("bookinfo.txt","a") as fp:
                    for book in booklist:
                        fp.write(book)
        else:
            print("file not found..")

    def deletebookbyId(self,id):
        book=[]
        found=False
        with open("bookinfo.txt","r")as fp:
            for line in fp:
                try:
                    line.index(str(id))
                except:
                    book.append(line)
                else:
                    found=True
        if (found):
            with open("bookinfo.txt","w")as fp:
                for bk in book:
                    fp.write(bk)
        else:
            print("Record not found.")

    def searchbook(self,id):
        found=False
        with open("bookinfo.txt","r")as fp:
            for line in fp:
                if(id in line):
                    found=True
                    print(" book found",line.strip())
                
                    break
        if(found==False):
            print("book not found")  
    
    def issue_Book(self,id):
        Booklist=[]
        flag=False
        with open("bookinfo.txt","r") as fp:
                for line in fp:
                    data=line.split(",")
                    if(int(data[0])==str(id)):
                    
                        print("Book Found: ",line.strip())
                        if(int(data[3])==1):
                            name=input("Enter the name of Borrower: ")
                            dateOfIssue=input("Enter the date of the issue(dd/mm/yyyy): ")
                            book=str(id)+","+name+","+dateOfIssue
                            print("Book issued successfully to",name)
                            with open("IssueBookinfo.txt","a") as fp1:
                                fp1.write(book)
                                fp1.write("\n")            
                                flag=True
                            data[3]="0\n"
                    
                        else:
                            print("Book is already issued.")
                    line=",".join(data)
                    Booklist.append(line)

        if(flag==True):
            with open("bookinfo.txt","w") as fp:
                for book in Booklist:
                    fp.write(book)        
                  
        else:
            print("File does not exist")

    def returnBook(self,id):
        Booklist=[]
        flag=False
        with open("IssueBookinfo.txt","r") as fp:
            for line in fp:
                data=line.split(",")
                if(data[0]==str(id)):
                    print("Book found ")
                    dateOfIssue = data[2]
                    dateOfIssue = dateOfIssue.split("/")                    
                    dateOfSubmit=input("Enter the date of the submit(dd/mm/yyyy): ")
                    dateOfIssue = datetime(int(dateOfIssue[2]),int(dateOfIssue[1]),int(dateOfIssue[0]))
                    dateOfSubmit = dateOfSubmit.split("/")
                    dateOfSubmit = datetime(int(dateOfSubmit[2]),int(dateOfSubmit[1]),int(dateOfSubmit[0]))
                    days = (dateOfSubmit - dateOfIssue).days
                    if(days > 5):
                        fine = (days-5)*20
                        print("Please pay Rs."+str(fine)+"\-")
                    else:
                        print("No fine applicaple")

                    flag = True                    
                else:
                    Booklist.append(data)
            

            if(flag):                
                with open("IssueBookinfo.txt","w") as fp:
                    for book in Booklist:
                        book = ",".join(book)
                        fp.write(book)
                
                bookData = []
                with open("bookinfo.txt","r") as fp:
                    for line in fp:
                        if(str(id) in line):
                            line = line.split(",")
                            line[3] = "1\n"
                            line = ",".join(line)
                        bookData.append(line)

                with open("bookinfo.txt","w") as fp:
                    for book in bookData:
                        fp.write(book)