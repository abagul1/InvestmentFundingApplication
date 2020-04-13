import Validate
import app
import pymysql
class Create:
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("What do you want to create? Please chose from the following options, or press Q to go back:")
        print("Location, Growth Equity Firm, Venture Capital Firm, Portfolio Company, Sector, Investment, Partner")
        user_in = input("Create: ")
        if user_in.lower() == "q":
            return app.main(self.cnx)
        v = Validate.Validate(self.cnx)
        while not v.validateInput(user_in, ["Location", "Growth Equity Firm", "Venture Capital Firm",
                                            "Portfolio Company", "Sector", "Investment", "Partner"]):
            print("Invalid Input Please try again with the options below, or enter Q to go back")
            print("Location, Growth Equity Firm, Venture Capital Firm, Portfolio Company, Sector, Investment, Partner")
            user_in = input("Create: ")
            if user_in.lower() == "q":
                return app.main(self.cnx)

        user_in = user_in.lower()
        if user_in == "location":
            return self.addLocation()
        elif user_in == "growth equity firm":
            return self.addGrowthEquity()
        elif user_in == "venture capital firm":
            return self.addVC()
        elif user_in == "portfolio company":
            return self.addPortfolio()
        elif user_in == "sector":
            return self.addSector()
        elif user_in == "investment":
            return self.addInvestment()
        elif user_in == "partner":
            return self.addPartner()

    def addLocation(self):
        c = self.cnx.cursor()
        arr = self.validateCreateInputValue(["Location ID: ", "State: ", "City: "], "location", "locationID",
                                      "Location ID already exists try again or press Q to return to home")
        if not arr:
            return
        else:
            sql_statement = "INSERT INTO location (locationID, state, city) VALUES (" + arr[0] + ", '" \
                            + arr[1] + "', '" + arr[2] + "')"
            c.execute(sql_statement)
            self.cnx.commit()
            print("Location inserted into table\n")
            c.close()

    def addVC(self):
        c = self.cnx.cursor()

        arr = self.validateCreateInputValue(["Firm ID: ", "Name: ", "Location ID: "], "vc_firms", "firmID",
                                            "Firm ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "INSERT INTO vc_firms (firmID, name, locationID) VALUES (" + arr[0] + ", '" \
                                + arr[1] + "', " + arr[2] + ")"
                c.execute(sql_statement)
                self.cnx.commit()
                print('VC Firm inserted into table!\n')
                c.close()
            except pymysql.err.IntegrityError:
                print("Create Failed!, Check foreign key provided (locationID) to see if it exists.\n")

    def addPartner(self):
        c = self.cnx.cursor()
        arr = self.validateCreateInputValue(["Partner ID: ", "Name: ", "Contact: ", "Firm ID: "], "partners",
                                            "partnerID",
                                            "Partner ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "INSERT INTO partners (partnerID, firmID, name, contact) VALUES (" + arr[0] + ", " \
                                + arr[3] + ", '" + arr[1] + "', '" + arr[2] + "')"
                c.execute(sql_statement)
                self.cnx.commit()
                print('Partner inserted into table!\n')
                c.close()
            except pymysql.err.IntegrityError:
                print("Create Failed!, Check foreign key provided (firmID) to see if it exists.\n")

    def addGrowthEquity(self):
        c = self.cnx.cursor()
        arr = self.validateCreateInputValue(["Firm ID: ", "Name: ", "Location ID: "], "growth_equity_firms", "firmID",
                                            "Firm ID already exists try again or press Q to return to home")

        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "INSERT INTO growth_equity_firms (firmID, name, locationID) VALUES (" + arr[0] + ", '" \
                                + arr[1] + "', " + arr[2] + ")"
                c.execute(sql_statement)
                self.cnx.commit()
                print('Growth Equity Firm inserted into table!\n')
                c.close()
            except pymysql.err.IntegrityError:
                print("Create Failed!, Check foreign key provided (locationID) to see if it exists.\n")

    def addSector(self):
        c = self.cnx.cursor()
        arr = self.validateCreateInputValue(["Sector ID: ", "Industry: ", "Type (VC/GE)",
                                             "Fund Size: ", "firmID: "], "sector",
                                            "sectorID",
                                            "Sector ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = ""
                b = True
                while b:
                    if arr[2].lower() == "vc":
                        sql_statement = "INSERT INTO sector (sectorID, industry, vc_firm_id, ge_firm_id, fund_size) " \
                                    "VALUES (" + arr[0] + ", '" + arr[1] + "', " + arr[4] + ", null, " + arr[3] + ")"
                        b = False
                    elif arr[2].lower() == "ge":
                        sql_statement = "INSERT INTO sector (sectorID, industry, vc_firm_id, ge_firm_id, fund_size) " \
                                        "VALUES (" + arr[0] + ", '" + arr[1] + "', null, " + arr[4] + ", " \
                                        + arr[3] + ")"
                        b = False
                    elif arr[2].lower() == 'q':
                        return
                    else:
                        arr[2] = input("Invalid Type please re-eneter (VC/GE): ")

                c.execute(sql_statement)
                self.cnx.commit()
                print('Sector inserted into table!\n')
                c.close()
            except pymysql.err.IntegrityError:
                print("Create Failed! Check foreign key provided (firmID) to see if it exists.\n")

    def addInvestment(self):
        c = self.cnx.cursor()

        arr = self.validateCreateInputValue(["Investment ID: ", "Amount: ", "Series: ", "Date: "], "investment",
                                            "investmentID",
                                            "Investment ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            sql_statement = "INSERT INTO investment (investmentID, amount, series, date) VALUES (" + arr[0] + ", " \
                            + arr[1] + ", '" + arr[2] + "', '" + arr[3] + "')"
            c.execute(sql_statement)
            self.cnx.commit()
            print('Investment inserted into table!\n')
            c.close()

    def addPortfolio(self):
        c = self.cnx.cursor()

        arr = self.validateCreateInputValue(["Portfolio ID: ", "Name: ", "Investment ID: ", "Sector ID: "],
                                            "portfolio_companies",
                                            "portID",
                                            "Portfolio ID already exists try again or press Q to return to home")
        if not arr:
            print("Back to homepage")
        else:
            try:
                sql_statement = "INSERT INTO portfolio_companies (portID, name, investmentID, sectorID) VALUES ("\
                                + arr[0] + ", '" + arr[1] + "', " + arr[2] + ", " + arr[3] + ")"
                c.execute(sql_statement)
                self.cnx.commit()
                print('Portfolio inserted into table!\n')
                c.close()
            except pymysql.err.IntegrityError:
                print("Create Failed! Check foreign keys provided (investmentID, sectorID) to see if they exist.\n")

    # Validate the inputs to see if they exist
    def validateCreateInputValue(self, arr, table, column, message):
        try:
            identifier = input(arr[0])
            v = Validate.Validate(self.cnx)
            while not v.validateUnique(table, column, identifier,
                                       message):
                identifier = input(arr[0])
                if identifier == 'Q':
                    return []
        except ValueError:
            print("Cannot input a string as an ID, must be an int, try again")
            return []

        tempArr = [""] * len(arr)
        tempArr[0] = identifier
        for val in range(1, len(arr)):
            tempArr[val] = input(arr[val])

        return tempArr
