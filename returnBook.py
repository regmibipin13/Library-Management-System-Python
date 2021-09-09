import books
import DateTime
from DateTime import timedelta
from DateTime import datetime
from datetime import datetime

def getBorrowedBooks(fileName):
    file = open(fileName, "r")
    borrowBooks = file.readlines()
    for i in range(len(borrowBooks)):
        borrowBooks[i] = borrowBooks[i].strip("\n").split(',')
    return borrowBooks

def printBorrowedBooks(file, alreadyBorrowedList):
    books = getBorrowedBooks(file)
    for i in range(len(books)):
        if books[i][1].split(":")[1] not in alreadyBorrowedList:
            print(books.index(books[i]), "--->", books[i][1].split(":")[1])

def calculateLateAmount(book):
    lateAmount = 0
    diffOfDate = 0

    borrowedDate = book[3].split(':')[1].split('/')[0]
    borrowedDate = datetime.strptime(borrowedDate, "%Y-%m-%d")
    endingDate = borrowedDate + timedelta(days=10)
    endingDate = datetime(endingDate.year, endingDate.month, endingDate.day)

    currentDate = DateTime.currentDate()
    currentTime = DateTime.currentTime()
    currentDate = datetime.strptime(currentDate, "%Y-%m-%d")
    currentDate = datetime(currentDate.year, currentDate.month, currentDate.day)

    if currentDate > endingDate:  
        diffOfDate = (currentDate - endingDate).days
        #Only actual amount
        price = book[2].split(':')[1]
        price = float(price.strip("$"))
        # Only extra fine amount
        lateAmount = 2 * diffOfDate
        # Fine amount and actual amount
        actualAmount = price + lateAmount
        print("")
        print("You are ",diffOfDate," days late to return the book")
        print("")
        print("Hence You will be fined extra ",lateAmount,"$")
        print("")
        print("Therefore your total will be ",actualAmount)

    return {
        "lateAmount":lateAmount,
        "diffOfDate": diffOfDate
    }


def store():
    firstName = input("Enter your first name :")
    lastName = input("Enter your last name :")
    borrowFileName = firstName+"_"+lastName+"-borrow.txt"
    fullName = firstName+" "+lastName

    returnFileName = firstName +"_"+ lastName+"-return.txt"

    try:
        borrowFile = open(borrowFileName, "r+")
        returnFile = open(returnFileName, "w+")
        returnedListNames = []

        returnAgain = "y"

        while returnAgain == "y":
            print("")
            printBorrowedBooks(borrowFileName, returnedListNames)
            print("")
            allBorrowedBooks = getBorrowedBooks(borrowFileName)
            try:
                print("")
                userSelectedIndex = int(input("Select one of the book which you want to return: "))

                if userSelectedIndex < len(allBorrowedBooks) and allBorrowedBooks[userSelectedIndex][1].split(":")[1] not in returnedListNames:
                    bookFromBorrow = allBorrowedBooks[userSelectedIndex]
                    allBooks = books.getBooksList()
                    bookFromActualList = []
                    for i in range(len(allBooks)):
                        if allBooks[i][0] == bookFromBorrow[1].split(":")[1]:
                            bookFromActualList = allBooks[i]
                            allBooks[i][2] = str(int(allBooks[i][2]) + 1)

                    returnedListNames.append(bookFromActualList[0])
                    lateDetails = calculateLateAmount(bookFromBorrow)
                    lateAmount = lateDetails["lateAmount"]   

                    details = "Name:", firstName," ",lastName,", ","Book:", bookFromActualList[0],", ","Cost:",bookFromActualList[3],", ","Fined Amount:","$",str(lateAmount),", ","Date and Time:", str(DateTime.currentDate()),"/",str(DateTime.currentTime()),"\n"
                    returnFile.writelines(details)
                    books.changeQuantity(allBooks)

                    print("")
                    print("Book Returned Successfully")
                    print("")
                
                else:
                    print("")
                    print("This Book is either not valid or already returned. Please try another one")
                    print("")

            except:
                print("")
                print("Please Select the correct value and try again")
                print("")
            
            returnAgain = input("Enter (Y)/y to return book again and any other key to exit: ").lower()

    except:
        print("")
        print("Sorry You have not borrowed anything from our system")
        print("")


