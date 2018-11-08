import pymysql
import pandas as pd
import smtplib
import pysftp
import datetime
import os

FTPLOCATION="/responders/test/in/"

FILENAMESUFFIX = "_Responders_test.txt"
FTPHOST = "st.sanlam.co.za"
FTPUSER = "sd_antSB"
FTPPASSWORD = "Dep14K77"


curdate = datetime.datetime.today().strftime('%Y-%m-%d')

filename = "ANT003_" + curdate + str(FILENAMESUFFIX)
print(filename)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=str(FTPHOST),
	username=str(FTPUSER),
    password=str(FTPPASSWORD),
    cnopts=cnopts) as sftp:

		with sftp.cd(str(FTPLOCATION)):
			sftp.put(filename)
