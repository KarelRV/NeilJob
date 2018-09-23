import pyodbc 
import pandas as pd
import smtplib
import pysftp
import datetime


ftplocation = 'test/in'
filelocation ="C:/Users/Administrator/Documents/Leads"
curdate = datetime.datetime.today().strftime('%Y-%m-%d')

filename = "ANT003_"+curdate+"_Responsers_"+"test.txt"
#con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                      "Server=niel.database.windows.net;"
#                      "Database=analysis;"
#                      "Uid=niel;"
					  #"Pwd=8sPvdY5C$Ss2pfSjy*")
					  
con = pyodbc.connect("Driver={MySQL ODBC 3.51 Driver};"
                      "Server=154.0.171.86;"
                      "Database=leads;"
                      "Uid=niel;"
					  "Pwd=L3adsu$ER")					  

df = pd.read_sql_query("CALL get_new_leads()", con)

df['TypeName']="ANTHROPOLOGY OLICO NPH STi"
df['TypeDesc']="00008625"

df2=df.astype(str).apply(''.join,axis=1)
df2.to_csv(filelocation+filename,index=False,encoding="utf-8")

cnopts = pysftp.CnOpts()
cnopts.hostkeys=None

with  pysftp.Connection(host="st.sanlam.co.za", username="sd_antSB",password="Dep14K77",cnopts=cnopts) as sftp:
	with sftp.cd(ftplocation):
		sftp.put(filelocation+filename)
		#sftp.close()

message_text = "SFTP LOAD: "+curdate+" - "+ str(df2.shape[0])

message_subject = "SFTP LOAD: "+curdate+" - "+ str(df2.shape[0])
fromaddr = 'anthropologyleadsnotification@gmail.com'
toaddr  = 'nieldv@gmail.com'

message = "From: %s\r\n" % fromaddr	+ "To: %s\r\n" % toaddr	+ "Subject: %s\r\n" % message_subject + "\r\n" + message_text

toaddrs = [toaddr]
		
username = 'anthropologyleadsnotification@gmail.com'
password = '$6#saSH@xcr5vkP1zh'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
print(message)
server.sendmail(fromaddr, toaddrs, message)
server.quit()

print("klaar")

