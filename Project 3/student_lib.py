'''
                    ***STUDENT LIBRARY***

Implement a Student library system using OOPs where Students can borrow a book from the list of Books'
Create a separate library and student class.
Your borrow must be menu driven.
You are free to choose methids and attributes of your choice to implement this Functionally.
'''
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Available Books in this Library:")
        for book in self.books:
            print("* ", book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued: {bookName}. Please keep it safe and return it in 30 Days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has Already been issued to Someone else or it not present in Library right now. Please wait till the book is returned or been added in the Library.")
            return False

    def returnbook(self,bookName):
        self.books.append(bookName)
        print(f"Thanks For returning the book {bookName}. Hope You Enjoy reading it. Have a Great Day Ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return/add: ")
        return self.book
 

if __name__ == "__main__":
    centralLibary = Library(["Algorithm", "CSS", "Code With Harry", "Django", "Clrs"])
    student = Student()
    # centralLibary.displayAvailableBooks()
    while(True):
        welcomeMSG = '''****** Welcome to Central Library ******
        Please Choose an Option: 
        1. List Of Books Available In The Library
        2. Request A Book
        3. Return/Add A Book
        4. Exit The Library
        '''
        print(welcomeMSG)
        a = int(input("Enter your Choice: "))

        if a == 1:
            centralLibary.displayAvailableBooks()
        elif a == 2:
            centralLibary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibary.returnbook(student.returnBook())
        elif a == 4:
            print("Thank You For Coming In The Central library.Have A Great Day!")
            exit()
        else:
            print("Invalid Choice.")