# CS3200 Project Frontend
# By: Akhil Bagul, Arian Gokhale

import pymysql

# Connection to database
username = input('MySQL Username: ')
password = input('MySQL Password: ')
cnx = pymysql.connect(host='localhost', user=username, password=password,
                    db='fundingdatabase', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

c = cnx.cursor()

