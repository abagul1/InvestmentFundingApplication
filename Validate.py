# Class to validate user input data
class Validate:

    # Constructor for validate
    # Takes a connection to a database
    def __init__(self, cnx):
        self.cnx = cnx

    # Validate if a field exists in the database
    # Takes a table name, column name, and field value, and error message
    def validateExists(self, table, column, field, message):
        c = self.cnx.cursor()
        sql = "SELECT " + column + " FROM " + table
        c.execute(sql)
        arr = []
        for row in c.fetchall():
            arr.append(row[column])
        if int(field) in arr:
            return True
        else:
            print(message)
            return False

    # Validate an input based on an array of valid inputs
    # Takes user input and array of valid inputs
    def validateInput(self, in1, arr):
        arrLower = [x.lower() for x in arr]
        i = in1.lower()
        if i in arrLower:
            return True
        else:
            return False

    def validateUnique(self, table, column, field, message):
        c = self.cnx.cursor()
        sql = "SELECT " + column + " FROM " + table
        c.execute(sql)
        arr = []
        for row in c.fetchall():
            arr.append(row[column])

        if int(field) in arr:
            print(message)
            return False
        else:
            return True



