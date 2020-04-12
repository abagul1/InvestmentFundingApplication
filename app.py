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
    if user_in == "Q":
        return user_in
    v = Validate.Validate(cnx)
    while not v.validateInput(user_in, ["Create", "Read", "Update", "Delete", "Q"]):
        print("Invalid input please select from the following, or enter Q to quit the application")
        print("Create, Read, Update, Delete")
        user_in = input("What would you like to do: ")

    return user_in

# Delegate user input to appropriate class
def delegate(cnx, user_in):
    if user_in == "Create":
        return Create.Create(cnx)
    elif user_in == "Read":
        return Read.Read(cnx)
    elif user_in == "Update":
        return Update.Update(cnx)
    else:
        return Delete.Delete(cnx)

# Main function to run application
def main():
    cnx = connectToDB()
    user_in = homePage(cnx)
    while not user_in == "Q":
        delegate(cnx, user_in).delegate()
    cnx.close()


if __name__ == "__main__":
    main()



