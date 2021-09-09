import books
import DateTime

def store():
    firstName = input("Enter your first name :")
    print("")
    lastName = input("Enter your last name :")
    print("")
    fileName = firstName+"_"+lastName+"-borrow.txt"
    file = open(fileName, "w+")
    fullName = firstName+" "+lastName

    borrowedListNames = []
    borrowAgain = "y"
    while borrowAgain == "y":
        books.printBooks()
        try:
            print("")
            selectedBookIndex = int(input("Please select the book you want to borrow: "))
            print("")

            if selectedBookIndex >= 0 and selectedBookIndex < len(books.getBooksList()):
                allBooks = books.getBooksList()
                book = allBooks[selectedBookIndex]

                if book[0] not in borrowedListNames:
                    allBooks[selectedBookIndex][2] = str(int(allBooks[selectedBookIndex][2]) - 1)
                    books.changeQuantity(allBooks)
                    insertDataToFile(book, file, fullName)
                    borrowedListNames.append(book[0])
                    print("")
                    print("Book Borrowed Successfully")
                    print("")
                else:
                    print("")
                    print("You have already borrrowed this book")
                    print("")
            else:
                print("")
                print("Incorrect value input . Please enter correct value and try again")
                print("")
        except Exception as e:
            print("")
            print("Please enter correct value and try again")
            print("")
        
        print("")
        borrowAgain = input("Enter (Y) / y to borrow again and any other key to exit: ").lower()
        print("")


def insertDataToFile(book, borrowFile, fullName):   

    details = "Name:", fullName,", ","Book:", book[0],", ","Cost:",book[3],", ","Date and Time:", DateTime.currentDate(),"/",DateTime.currentTime(),"\n"
    borrowFile.writelines(details)

        
