import Validate
import app
# Class to represent Updates
class Update:

    # Constructor for Updates
    # Takes a database connection
    def __init__(self, cnx):
        self.cnx = cnx

    # Delegate user commands to appropriate method
    def delegate(self):
        print("What do you want to update? Please chose from the following options, or enter Q to go back:")
        print("Sector Fund, Investment Amount, Investment Series, Partner Firm, Partner Contact")
        user_in = input("Update: ")
        if user_in.lower() == 'q':
            return app.main(self.cnx)
        v = Validate.Validate(self.cnx)
        while not v.validateInput(user_in, ["Sector Fund", "Investment Amount",
                                  "Investment Series", "Partner Firm", "Partner Contact"]):
            print("Invalid Input Please try again with the options below, or enter Q to go back")
            print("Sector Fund, Investment Amount, Investment Series, Partner Firm, Partner Contact")
            user_in = input("Update: ")
            if user_in.lower() == "q":
                return app.main(self.cnx)

        user_in = user_in.lower()
        if user_in == "sector fund":
            return self.updateSector()
        elif user_in == "investment amount":
            return self.updateInvestmentAmount()
        elif user_in == "investment series":
            return self.updateInvestmentSeries()
        elif user_in == "partner firm":
            return self.updatePartnerFirm()
        elif user_in == "partner contact":
            return self.updatePartnerContact()

    # Updates a sector fund size
    def updateSector(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Sector ID: ", "New Fund Size: ", 'sector', 'sectorID',
                                            "Sector doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "UPDATE sector SET fund_size = " + arr[0] + " WHERE sectorID = " + arr[1]
                c.execute(sql_statement)
                self.cnx.commit()
                print("Sector fund size updated\n")
                c.close()
            except:
                print("Update Failed!, Check inputs to see if they are valid\n")

    # Updates an investment amount
    def updateInvestmentAmount(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Investment ID: ", "New Amount: ", 'investment', 'investmentID',
                                            "Investment doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "UPDATE investment SET amount = " + arr[0] + " WHERE investmentID = " + arr[1]
                c.execute(sql_statement)
                self.cnx.commit()
                print("Investment amount updated.\n")
                c.close()
            except:
                print("Update Failed!, Check inputs to see if they are valid\n")

    # Updates an Investment stage
    def updateInvestmentSeries(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Investment ID: ", "New Series: ", 'investment', 'investmentID',
                                            "Investment doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "UPDATE investment SET series = '" + arr[0] + "' WHERE investmentID = " + arr[1]
                c.execute(sql_statement)
                self.cnx.commit()
                print("Investment series updated\n")
                c.close()
            except:
                print("Update Failed!, Check inputs to see if they are valid\n")

    # Update a partner's VC firm
    def updatePartnerFirm(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Partner ID: ", "New Firm ID: ", 'partners', 'partnerID',
                                            "Partner doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "UPDATE partners SET firmID = " + arr[0] + " WHERE partnerID = " + arr[1]
                c.execute(sql_statement)
                self.cnx.commit()
                print("Partner firm is updated\n")
                c.close()
            except:
                print("Update Failed!, Check inputs to see if they are valid\n")

    # Update the contact info of a partner
    def updatePartnerContact(self):
        c = self.cnx.cursor()
        arr = self.validateUpdateInputValue("Partner id: ", "New Contact: ", 'partners', 'partnerID',
                                      "Partner doesn't exist try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "UPDATE partners SET contact = '" + arr[0] + "' WHERE partnerID = " + arr[1]
                c.execute(sql_statement)
                self.cnx.commit()
                print("Partner contact is updated\n")
                c.close()
            except:
                print("Update Failed!, Check inputs to see if they are valid\n")

    # Validate the inputs to see if they exist
    def validateUpdateInputValue(self, in1, in2, table, column, message):
        try:
            identifier = input(in1)
            v = Validate.Validate(self.cnx)
            while not v.validateExists(table, column, int(identifier),
                                       message):
                identifier = input(in1)
                if identifier.lower() == 'Q':
                    return []

            value = input(in2)
        except ValueError:
            print("Update Failed!, Check inputs to see if they are the correct type")
            return []

        return [value, identifier]
