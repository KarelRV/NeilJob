import pymysql
import pandas as pd
import smtplib
import pysftp
import datetime
import os

curdate = datetime.datetime.today().strftime('%Y-%m-%d')
FILENAMESUFFIX = "_Responders_test.txt"
MYSQLDB = 'leads'
MYSQLHOST = '154.0.171.86'
MYSQLUSER = 'niel'
MYSQLPASSWORD = 'L3adsusER!@#'



filename = "ANT003_" + curdate + str(FILENAMESUFFIX)

con = pymysql.connect(host=str(MYSQLHOST),
                          user=str(MYSQLUSER),
                          password=str(MYSQLPASSWORD),
                          db=str(MYSQLDB),
                          cursorclass=pymysql.cursors.DictCursor)
#df = pd.read_sql_query("CALL get_new_leads()", con)
df = pd.read_sql_query("SELECT * FROM leads_history limit 1", con)

df['TypeName'] = "ANTHROPOLOGY OLICO NPH STi"
df['TypeDesc'] = "00008625"
print(df)




df2 = df.astype(str).apply(''.join, axis=1)
print(df2)
df2.to_csv(filename, index=False, encoding="utf-8")
list(df2)