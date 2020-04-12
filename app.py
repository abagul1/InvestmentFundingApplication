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
    print("Enter any of the following commands to interact with the database")
    print("Create, Read, Update, Delete")
    user_in = input("What would you like to do: ")
    v = Validate.Validate(cnx)
    while not v.validateInput(user_in, ["Create", "Read", "Update", "Delete"]):
        print("Invalid input please select from the following")
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
    delegate(cnx, user_in).delegate()


if __name__ == "__main__":
    main()



