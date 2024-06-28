def account(): #creates a function called account, which i will later call to run this code
    account = [] #initializes an empty list that will contain a list of usernames 
    register = input("Create an account\n-------\nEnter username: ") #asks the user to enter an username to register
    print(f"Hello {register}") #welcomes the user using formatted string literals
    account.append(register) #stores the value of "register" inside the account list
    transaction = input("Make your first Transaction (Enter the name of the person you want to send money to): ") #makes the user perform their first transaction
    print(f"Succesfully sent money to {transaction}") #notifies them that the transaction went through
    update = input("Would you like to update your account info?: ") #asks the user if they would like to update their account info
    if update == "yes": #if the answer is yes
        update2 = input("Enter your updated username here: ") #it will ask them for an updated username
        account.clear() #it deletes the old one here
        account.append(update2) #and adds the new value
    search = input("Would you like to search for your account in our database?: ") #asks the user if they want to search the database to see if they're in there
    if search == "yes": # if the answer is yes
        search2 = input("Enter the name you would like to search: ") #it asks the user to enter the username they want to search
        if search2 in account: #if the entered username is in the list of values that contains all of the usernames entered
            print("Your account is in our database") #it notifies them that it is in there
        else: #if it isnt
            print("Your account is not in our database") # it notifies them that it isnt
    viewlist = input("Would you like to view the list of all of our customers?: ") #asks the user if they want to see a list of all of our customers
    if viewlist == "yes": #if the answer is yes
        print(f"Heres a list of all of our customers: {account}") # returns the account list, that contains all of the usernames of people
    elif viewlist == "no": #if the answer is no
        print("Okay, you are our only user anyways") # we notify them and tell them its fine, because they are our only user anyways
    delete = input("Would you like to delete your account?: ") # asks the user if they want to delete their account
    if delete == "yes": # if the answer is yes
        account.clear() # it deletes all of the elements in the list
        print(f"Okay, here's an updated version of the list of our cistomers: {account}") #and prints the updated list
    exitsys = input("Would you like to exit the system?(You can't say no): ") # asks the user if they want to exit the program, but they cant refuse because the program needs to be stopped eventually
    print("Shutting down...") #shuts down the program
account() #calls the function, running the program
