def getBooksList():
    try:
        file = open('books.txt','r+')
        books = file.readlines()
        for i in range(len(books)):
            books[i] = books[i].strip('\n').split(',')
        return books
    except:
        return False

def printBooks():
    books = getBooksList()

    if books != False:
        for i in range(len(books)):
            if int(books[i][2]) > 0:
                print(books.index(books[i]), "--->", books[i][0])
        print("")
    else:
        print("Oops Looks like something is wrong . Please Try again Later")

def changeQuantity(books):
    try:
        file = open("books.txt","r+")
    except:
        file = open("books.txt","w")

    for i in range(len(books)):
        for j in range(len(books[i])): 
            string = str(str(books[i][j]))
            file.write(string)
            if(j != 3):
                file.write(",")
        if i != len(books) - 1:
            file.write("\n")
    file.close()