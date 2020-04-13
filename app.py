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
    conn = pymysql.connect(host='localhost', user=username, password=password,
                        db='fundingdatabase', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return conn

# Initial command line prompt
def homePage(conn):
    print("Enter any of the following commands to interact with the database")
    print("Create, Read, Update, Delete")
    user_in = input("What would you like to do: ")
    v = Validate.Validate(conn)
    while not v.validateInput(user_in, ["Create", "Read", "Update", "Delete"]):
        print("Invalid input please select from the following:")
        print("Create, Read, Update, Delete")
        user_in = input("What would you like to do: ")

    return user_in

# Delegate user input to appropriate class
def delegate(conn, user_in):
    user_in = user_in.lower()
    if user_in == "create":
        print("\n")
        return Create.Create(conn)
    elif user_in == "read":
        print("\n")
        return Read.Read(conn)
    elif user_in == "update":
        print("\n")
        return Update.Update(conn)
    elif user_in == "delete":
        print("\n")
        return Delete.Delete(conn)
    else:
        raise Exception("Invalid User input: " + user_in)


# Main function to run application
def main(conn):
    user_in = homePage(conn)
    while True:
        delegate(conn, user_in).delegate()


if __name__ == "__main__":
    cnx = connectToDB()
    main(cnx)
