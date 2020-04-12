class Create:
    def __init__(self, cnx):
        self.cnx = cnx

    def addLocation(self, locationid, state, city):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO location (locationID, state, city) VALUES (%d, %s, %s)"
        values = (locationid, state, city)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, "Location inserted into table")
        c.close()

    def addVC(self, firmID, name, locationID):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO vc_firms (firmID, name, locationID) VALUES (%d, %s, %d)"
        values = (firmID, name, locationID)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'VC Firm inserted into table')
        c.close()

    def addPartner(self, partnerID, firmID, name, contact):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO partners (partnerID, firmID, name, contact) VALUES (%d, %d, %s, %s)"
        values = (partnerID, firmID, name, contact)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Partner inserted into table')
        c.close()

    def addGrowthEquity(self, firm_id, name, locationID):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO growth_equity_firms (firm_id, name, locationID) VALUES (%d, %s, %d)"
        values = (firm_id, name, locationID)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Growth Equity Firm inserted into table')
        c.close()

    def addSector(self, SectorID, industry, VC_firm_id, GE_firm_id, fund_size):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO sector (SectorID, industry, VC_firmID, GE_firmID, fund_size) " \
                        "VALUES (%d, %s, %d, %d, %d)"
        values = (SectorID, industry, VC_firm_id, GE_firm_id, fund_size)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Sector inserted into table')
        c.close()

    def addInvestment(self, investmentID, amount, series, date):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO investment (investmentID, amount, series, date) VALUES (%d, %d, %s, %s)"
        values = (investmentID, amount, series, date)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Investment inserted into table')
        c.close()

    def addPortfolio(self, PortID, name, InvestmentID, sectorID):
        c = self.cnx.cursor()
        sql_statement = "INSERT INTO portfolio_companies (PortID, name, InvestmentID, sectorID) VALUES (%d, %s, %d, %d)"
        values = (PortID, name, InvestmentID, sectorID)
        c.execute(sql_statement, values)
        self.cnx.commit()
        print(c.rowcount, 'Portfolio inserted into table')
        c.close()
