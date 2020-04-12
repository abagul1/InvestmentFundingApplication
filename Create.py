import Validate
class Create:
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("What do you want to add? Please chose from the following options:")
        print("Location, Growth Equity Firm, Venture Capital Firm, Portfolio Company, Sector, Investment, Partner")
        user_in = input("Create: ")
        v = Validate.Validate(self.cnx)
        while not v.validateInput(user_in, ["Location", "Growth Equity Firm", "Venture Capital Firm",
                                            "Portfolio Company", "Sector", "Investment", "Partner"]):
            print("Invalid Input Please try again with the options below, or enter Q to go back")
            print("Location, Growth Equity Firm, Venture Capital Firm, Portfolio Company, Sector, Investment, Partner")
            user_in = input("Create: ")
            if user_in == "Q":
                return

        switch = {
            "Location", self.addLocation(),
            "Growth Equity Firm", self.addGrowthEquity(),
            "Venture Capital Firm", self.addVC(),
            "Portfolio Company", self.addPortfolio(),
            "Sector", self.addSector(),
            "Investment", self.addInvestment(),
            "Partner", self.addPartner()
        }
        func = switch.get(user_in)
        func()

    def addLocation(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO location (locationID, state, city) VALUES (%d, %s, %s)"
        arr = self.validateCreateInputValue(["Location ID: ", "State: ", "City: "], "location", "locationID",
                                      "Location ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, "Location inserted into table")
            c.close()

    def addVC(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO vc_firms (firmID, name, locationID) VALUES (%d, %s, %d)"
        arr = self.validateCreateInputValue(["Firm ID: ", "Name: ", "Location ID: "], "vc_firms", "firmID",
                                            "Firm ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'VC Firm inserted into table')
            c.close()

    def addPartner(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO partners (partnerID, firmID, name, contact) VALUES (%d, %d, %s, %s)"
        arr = self.validateCreateInputValue(["Partner ID: ", "Firm ID: ", "Name: ", "Contact: "], "partners",
                                            "partnerID",
                                            "Partner ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2], arr[3])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'Partner inserted into table')
            c.close()

    def addGrowthEquity(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO growth_equity_firms (firmID, name, locationID) VALUES (%d, %s, %d)"
        arr = self.validateCreateInputValue(["Firm ID: ", "Name: ", "Location ID: "], "growth_equity_firms", "firmID",
                                            "Firm ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'Growth Equity Firm inserted into table')
            c.close()

    def addSector(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO sector (sectorID, industry, vc_firm_id, ge_firm_id, fund_size) " \
                        "VALUES (%d, %s, %d, %d, %d)"
        arr = self.validateCreateInputValue(["Sector ID: ", "Industry: ", "VC firm ID: ", "GE Firm ID: ",
                                             "Fund Size: "], "sector",
                                            "sectorID",
                                            "Sector ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2], arr[3], arr[4])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'Sector inserted into table')
            c.close()

    def addInvestment(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO investment (investmentID, amount, series, date) VALUES (%d, %d, %s, %s)"
        arr = self.validateCreateInputValue(["Investment ID: ", "Amount: ", "Series: ", "Date: "], "investment",
                                            "investmentID",
                                            "Investment ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2], arr[3])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'Investment inserted into table')
            c.close()

    def addPortfolio(self):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO portfolio_companies (portID, name, investmentID, sectorID) VALUES (%d, %s, %d, %d)"
        arr = self.validateCreateInputValue(["Portfolio ID: ", "Name: " "Investment ID: ", "Sector ID: "],
                                            "portfolio_companies",
                                            "portID",
                                            "Portfolio ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            values = (arr[0], arr[1], arr[2], arr[3])
            c.execute(sql_statement, values)
            self.cnx.commit()
            print(c.rowcount, 'Portfolio inserted into table')
            c.close()

    # Validate the inputs to see if they exist
    def validateCreateInputValue(self, arr, table, column, message):
        identifier = input(arr[0])
        v = Validate.Validate(self.cnx)
        while not v.validateUnique(table, column, identifier,
                                   message):
            identifier = input(arr[0])
            if identifier == 'Q':
                return []

        tempArr = []
        for val, i in enumerate(arr):
            tempArr[i] = input(val)

        return tempArr
