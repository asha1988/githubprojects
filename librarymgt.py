class Library:

    def __init__(self, list, name):
        self.booklist = list
        self.libname = name
        self.lendict = {}


    def display(self):
        print(f"The list of books in {self.libname}")
        for book in self.booklist:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendict.keys():
            self.lendict.update({book: user})
            print(f"Successfully updated", "you can take book now")
        else:
            print(f"Book is already taken by {self.lendict[book]}")

    def add_book(self, book):
        self.booklist.append(book)
        print("The book is added successfully")

    def return_book(self, book):
        self.lendict.pop(book)


if __name__ == '__main__':
    mylibrary = Library(['Python', 'Java', 'C++', 'C'], "National Library")
    while (True):
        print(f"**********Welcome to {mylibrary.libname}**********")
        input1 = input(
            "what you want to do?\nselect your option\n 1:Display Book\n 2:Lend Book\n 3:Add a Book\n 4:Return Book\n 5:Quit\n")
        if input1 == '1':
            mylibrary.display()
        elif input1 == '2':
            book = input("Enter book name you want to lend\n")
            user = input("Enter your name\n")
            mylibrary.lend_book(user, book)
        elif input1 == '3':
            book = input("Enter book which you want to add\n")
            mylibrary.add_book(book)
        elif input1 == '4':
            book = input("Enter book which you want to return\n")
            mylibrary.return_book(book)
        elif input1 == '5':
            print("Thank you for using our Library")
            exit()
        else:
            print("Invalid choice,Enter [1,2,3,4,5]")
