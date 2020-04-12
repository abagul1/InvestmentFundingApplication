import Validate
# Class to represent Updates
class Update:

    # Constructor for Updates
    # Takes a database connection
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("Create")

    # Updates a sector fund size
    def updateSector(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Sector ID: ", "New Fund Size: ", 'sector', 'sectorID',
                                            "Sector doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "UPDATE sector SET fund_size = %d WHERE sectorID = %d"
            values = (arr[0], arr[1])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Sector fund size updated")
            c.close()

    # Updates an investment amount
    def updateInvestmentAmount(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Investment ID: ", "New Amount: ", 'investment', 'investmentID',
                                            "Investment doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "UPDATE investment SET amount = %d WHERE investmentID = %d"
            values = (arr[0], arr[1])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Investment amount updated")
            c.close()

    # Updates an Investment stage
    def updateInvestmentSeries(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Investment ID: ", "New Series: ", 'investment', 'investmentID',
                                            "Investment doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "UPDATE investment SET series = %s WHERE investmentID = %d"
            values = (arr[0], arr[1])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Investment series updated")
            c.close()

    # Update a partner's VC firm
    def updatePartnerFirm(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Partner ID: ", "New Firm: ", 'partners', 'partnerID',
                                            "Partner doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "UPDATE partners SET firmID = %d WHERE partnerID = %d"
            values = (arr[0], arr[1])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Partner firm is updated")
            c.close()

    # Update the contact info of a partner
    def updatePartnerContact(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Partner id: ", "New Contact: ", 'partners', 'partnerID',
                                      "Partner doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "UPDATE partners SET contact = %s WHERE partnerID = %d"
            values = (arr[0], arr[1])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Partner contact is updated")
            c.close()

    # Validate the inputs to see if they exist
    def validateUpdateInputValue(self, in1, in2, table, column, message):
        identifier = input(in1)
        value = input(in2)
        v = Validate.Validate(self.cnx)
        while not v.validateExists(table, column, value,
                                   message):
            identifier = input(in1)
            if identifier == 'Q':
                return []

        return [value, identifier]
