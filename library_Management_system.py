# class library:
#     def __init__(self, listofbooks):
#         self.books = listofbooks
#
#     def displayAvailablebooks(self):
#         print("Books present in this library are:")
#         for book in self.books:
#             print(" *" + book)
#     def borrowbook(self, bookname):
#         if bookname in self.books:
#             print(f"you have been issued {bookname}. please keep it safe and return it within 30 days")
#             self.books.remove(bookname)
#             return True
#         else:
#             print("sorry this book has issued to someone else. please wait until when the book is returned")
#             return False
#     def returnbook(self, bookname):
#         self.books.append(bookname)
#         print("thanks for returning this book")
#
# class student:
#     def __init__(self):
#         self.book = []
#     def requestbook(self):
#         self.book = input("enter the name of the book you want to borrow")
#         return self.book
#     def returnbook(self):
#         self.book = input("enter the name of the book you want to return")
#         return self.book
#
# if __name__ == '__main__':
#     centralLibrary = library(["Algorithms", "Django", "Flask", "python"])
#     #centralLibrary.displayAvailablebooks()
#     student = student()
#     while(True):
#         welcomemsg = """******Welcome to central library*******
#         please choose an option:
#         1. listing all the book
#         2. request a book
#         3. return a book
#         4. exit the library
#         """
#         print(welcomemsg)
#
#         a = int(input("enter a choice"))
#         if a == 1:
#             centralLibrary.displayAvailablebooks()
#         elif a == 2:
#             centralLibrary.borrowbook(student.requestbook)
#         elif a == 3:
#             centralLibrary.returnbook(student.returnbook)
#         elif a == 4:
#             print("Thanks for choosing us")
#             exit()
#         else:
#             print("invalid choice")


















