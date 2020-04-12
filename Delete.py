class Delete:
    def __init__(self, cnx):
        self.cnx = cnx

    def delegate(self):
        print("Delete")

    def delVC(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from vc_firms WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'VC Firm deleted')
        c.close()

    def delPartner(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from partner WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Partner deleted')
        c.close()

    def delGrowthEquity(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from growth_equity_firms WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Growth equity firm deleted')
        c.close()

    def delSector(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from sector WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Sector deleted')
        c.close()

    def delInvestment(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from investment WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Investment deleted')
        c.close()

    def delPortfolio(self, field, target):
        c = self.cnx.cursor()
        sql_statement = "DELETE from portfolio WHERE %d = %s"
        values = (field, target)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Portfolio deleted')
        c.close()
