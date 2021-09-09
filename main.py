import borrowBook
import returnBook

def startProgram():
	try:
		programStatus = True
		while programStatus:
			getIntro()
			getOptions()
			userSelection = input("Please select one of the option: ").lower()
			print("")
			notValidated = True
			while notValidated:
				if userSelection == "1":
					notValidated = False
					borrowBooks()
				elif userSelection == "2":
					notValidated = False
					returnBooks()
				elif userSelection == "3":
					notValidated = False
					exitProgram()
					return
				else:
					userSelection = input("Invalid Value \nPlease select correct value: ").lower()
					notValidated = True


			# Asking user if he/she still wants to continue with the program
			userSelectionForProgam = input("Do you want to continue running the program ? (Y) / y for yes and any other key to exit: ").lower()
			if userSelectionForProgam == "y":
				programStatus = True
			else:
				programStatus = False

		exitProgram()
	except:
		print("Oops ! Something went wrong !")

						


def borrowBooks():
	borrowBook.store()

def returnBooks():
	returnBook.store()

def exitProgram():
	print("")
	print("----------------------- THANK YOU FOR USING OUR SYSTEM -----------------------")
	print()


def getIntro():
	print("")
	print("----------------------- WELCOME TO OUR LIBRARY MANAGEMENT SYSTEM -----------------------")
	print()

def getOptions():
	print("Here are the list of things you can do in our system")
	print("")
	print("-> 1: Borrow Books")
	print("-> 2: Return Books")
	print("-> 3: Exit Program")
	print("")


startProgram()
