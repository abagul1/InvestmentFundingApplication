import Validate
import app
class Read:
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("What do you want to read? Please chose from the following options, or press Q to go back:")
        print("Table, Portfolios by Sector, Investments by VC Firm, Investments by GE Firm,"
              " Partners at Firm, Firms in Location")
        user_in = input("Read: ")
        if user_in.lower() == "q":
            return app.main()
        v = Validate.Validate(self.cnx)
        while not v.validateInput(user_in, ["Table", "Portfolios by Sector", "Investments by VC Firm",
                                            "Investments by GE Firm", "Partners at Firm",
                                            "Firms in Location"]):
            print("Invalid Input Please try again with the options below, or enter Q to go back")
            print("Table, Portfolios by Sector, Investments by VC Firm, Investments by GE Firm,"
                  " Partners at Firm, Firms in Location")
            user_in = input("Create: ")
            if user_in.lower() == "q":
                return app.main()

        user_in = user_in.lower()
        if user_in == "table":
            return self.readTable()
        elif user_in == "portfolios by sector":
            return self.getSectorPortfolioCo()
        elif user_in == "investments by vc firm":
            return self.getInvestmentsByVCFirm()
        elif user_in == "investments by ge firm":
            return self.getInvestmentsByGEFirm()
        elif user_in == "partners at firm":
            return self.getPartnersForVCFirm()
        elif user_in == "firms in location":
            return self.getFirmsInLocation()

    def readTable(self):
        print("Which table would you like to read, chose from the list below or press Q to go back to home page")
        print("location, growth_equity_firms, vc_firms, portfolio_companies, sector, investment, partners")
        user_in = input("Table: ")
        v = Validate.Validate(self.cnx)
        if user_in.lower() == "q":
            return
        while not v.validateInput(user_in, ["location", "growth_equity_firms", "vc_firms", "portfolio_companies",
                                            "sector", "investment", "partners"]):
            print("Invalid Input try again, chose from the list below or press Q to go back to home page")
            print("location, growth_equity_firms, vc_firms, portfolio_companies, sector, investment, partners")
            user_in = input("Table: ")
            if user_in.lower() == "q":
                return

        c = self.cnx.cursor()
        sql = "select * from " + user_in
        c.execute(sql)
        for row in c.fetchall():
            print(row)
        c.close()

    def getSectorPortfolioCo(self):
        c = self.cnx.cursor()
        print("Select one of the following Sector Industries: ")
        sql = "select distinct industry from sector"
        c.execute(sql)
        s = ""
        for row in c.fetchall():
            s = s + row['industry'] + ", "
        print(s[:-2])
        arr = self.validateUpdateInputValue("Sector Industry: ", "sector", "industry",
                                      "Industry doesn't exist try again or press Q to return to home")
        if not arr:
            return
        else:
            c.callproc('getSectorPortfolioCo', {arr[0]})
            for row in c.fetchall():
                print(row)
        c.close()

    def getInvestmentsByVCFirm(self):
        c = self.cnx.cursor()
        print("Select one of the following VC Firms: ")
        sql = "select name from vc_firms"
        c.execute(sql)
        s = ""
        for row in c.fetchall():
            s = s + row['name'] + ", "
        print(s[:-2])
        arr = self.validateUpdateInputValue("VC Firm Name: ", "vc_firms", "name",
                                            "Firm doesn't exist try again or press Q to return to home")
        if not arr:
            return
        else:
            c.callproc('getInvestmentByVCFirm', {arr[0]})
            for row in c.fetchall():
                print(row)
        c.close()

    def getInvestmentsByGEFirm(self):
        c = self.cnx.cursor()
        print("Select one of the following GE Firms: ")
        sql = "select name from growth_equity_firms"
        c.execute(sql)
        s = ""
        for row in c.fetchall():
            s = s + row['name'] + ", "
        print(s[:-2])
        arr = self.validateUpdateInputValue("GE Firm Name: ", "growth_equity_firms", "name",
                                            "Firm doesn't exist try again or press Q to return to home")
        if not arr:
            return
        else:
            c.callproc('getInvestmentByGEFirm', {arr[0]})
            for row in c.fetchall():
                print(row)
        c.close()

    def getPartnersForVCFirm(self):
        c = self.cnx.cursor()
        print("Select one of the following VC Firms: ")
        sql = "select name from vc_firms"
        c.execute(sql)
        s = ""
        for row in c.fetchall():
            s = s + row['name'] + ", "
        print(s[:-2])
        arr = self.validateUpdateInputValue("VC Firm Name: ", "vc_firms", "name",
                                            "Firm doesn't exist try again or press Q to return to home")
        if not arr:
            return
        else:
            c.callproc('getPartnersForVCFirm', {arr[0]})
            for row in c.fetchall():
                print(row)
        c.close()

    def getFirmsInLocation(self):
        c = self.cnx.cursor()
        print("Select one of the following Locations: ")
        sql = "select city from location"
        c.execute(sql)
        s = ""
        for row in c.fetchall():
            s = s + row['city'] + ", "
        print(s[:-2])
        arr = self.validateUpdateInputValue("City: ", "location", "city",
                                            "Firm doesn't exist try again or press Q to return to home")
        if not arr:
            return
        else:
            c.callproc('getFirmsInLocation', {arr[0]})
            for row in c.fetchall():
                print(row)
        c.close()

    def validateUpdateInputValue(self, in1, table, column, message):
        identifier = input(in1)
        v = Validate.Validate(self.cnx)
        while not v.validateExists(table, column, identifier,
                                   message):
            identifier = input(in1)
            if identifier.lower() == 'q':
                return []

        return [identifier]
