# CS3200 Project Frontend
# By: Akhil Bagul, Arian Gokhale

import pymysql
import Validate
import Create
import Read
import Update
import Delete

# Connection to database
def connectToDB():
    username = input('MySQL Username: ')
    password = input('MySQL Password: ')
    cnx = pymysql.connect(host='localhost', user=username, password=password,
                        db='fundingdatabase', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return cnx

# Initial command line prompt
def homePage(cnx):
    print("Enter any of the following commands to interact with the database, or enter Q to quit the application")
    print("Create, Read, Update, Delete")
    user_in = input("What would you like to do: ")
    if user_in.lower() == "Q":
        return user_in
    v = Validate.Validate(cnx)
    while not v.validateInput(user_in, ["Create", "Read", "Update", "Delete", "Q"]):
        print("Invalid input please select from the following, or enter Q to quit the application")
        print("Create, Read, Update, Delete")
        user_in = input("What would you like to do: ")

    return user_in

# Delegate user input to appropriate class
def delegate(cnx, user_in):
    user_in.lower()
    if user_in == "create":
        return Create.Create(cnx)
    elif user_in == "read":
        return Read.Read(cnx)
    elif user_in == "update":
        return Update.Update(cnx)
    elif user_in == "delete":
        return Delete.Delete(cnx)
    else:
        raise Exception("Invalid User input: " + user_in)

# Main function to run application
def main():
    cnx = connectToDB()
    user_in = homePage(cnx)
    while not user_in.lower() == "q":
        delegate(cnx, user_in).delegate()
    cnx.close()


if __name__ == "__main__":
    main()



