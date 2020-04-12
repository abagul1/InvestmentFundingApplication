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
        sql = "SELECT %s FROM %s"
        val = (column, table)
        c.execute(sql, val)
        arr = []
        for row in c.fetchall():
            arr.append(row[column])

        if field not in arr:
            print(message)
            return False
        else:
            return True


