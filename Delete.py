import Validate
import app
class Delete:
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("What do you want to delete? Please chose from the following options, or press Q to go back:")
        print("Investment, Location, Partner, Growth Equity Firm, VC Firm, Portfolio Company, Sector")
        user_in = input("Delete: ")
        if user_in.lower() == "q":
            return app.main(self.cnx)
        v = Validate.Validate(self.cnx)
        while not v.validateInput(user_in, ["Investment", "Location", "Partner", "Growth Equity Firm", "VC Firm",
                                            "Portfolio Company", "Sector"]):
            print("Invalid Input Please try again with the options below, or enter Q to go back")
            print("Investment, Location, Partner, Growth Equity Firm, VC Firm, Portfolio Company, Sector")
            user_in = input("Delete: ")
            if user_in.lower() == "q":
                return app.main(self.cnx)

        user_in = user_in.lower()
        if user_in == "investment":
            return self.delInvestment()
        elif user_in == "location":
            return self.delLocation()
        elif user_in == "partner":
            return self.delPartner()
        elif user_in == "growth equity firm":
            return self.delGrowthEquity()
        elif user_in == "vc firm":
            return self.delVC()
        elif user_in == "portfolio company":
            return self.delPortfolio()
        elif user_in == "sector":
            return self.delSector()

    def delLocation(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from location WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Location deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delVC(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from vc_firms WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('VC Firm deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delPartner(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from partner WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Partner deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delGrowthEquity(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from growth_equity_firms WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Growth equity firm deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delSector(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from sector WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Sector deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delInvestment(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from investment WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Investment deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def delPortfolio(self):
        c = self.cnx.cursor()
        arr = self.validDeleteValue()
        try:
            sql_statement = "DELETE from portfolio WHERE " + arr[0] + " = " + arr[1]
            c.execute(sql_statement)
            self.cnx.commit()
            print('Portfolio company deleted!\n')
            c.close()
        except:
            print("Delete failed! Check inputs to see if they exist\n")

    def validDeleteValue(self):
        field = input("Target field to delete: ")
        target = input("Value to delete: ")
        return [field, target]
