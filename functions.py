import pymysql
import pandas as pd
import smtplib
import pysftp
import datetime
import os

def test2():
    x=os.environ.get("FIRST_VAR")
    print (x)


def ugly_load_to_sftp():
    ftplocation = 'test/in'
    # filelocation ="C:/Users/Administrator/Documents/Leads"
    curdate = datetime.datetime.today().strftime('%Y-%m-%d')
    filename = "ANT003_" + curdate + "_Responsers_" + "test.txt"
    # con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
    #                      "Server=niel.database.windows.net;"
    #                      "Database=analysis;"
    #                      "Uid=niel;"
    # "Pwd=8sPvdY5C$Ss2pfSjy*")

    con = pymysql.connect(host="154.0.171.86",
                          user="niel",
                          password="L3adsu$ER",
                          db="leads",
                          cursorclass=pymysql.cursors.DictCursor)
    df = pd.read_sql_query("CALL get_new_leads()", con)
    df['TypeName'] = "ANTHROPOLOGY OLICO NPH STi"
    df['TypeDesc'] = "00008625"
    df2 = df.astype(str).apply(''.join, axis=1)
    df2.to_csv(filename, index=False, encoding="utf-8")
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host="st.sanlam.co.za", username="sd_antSB", password="Dep14K77", cnopts=cnopts) as sftp:
        with sftp.cd(ftplocation):
            sftp.put(filename)
    message_text = "SFTP LOAD: " + curdate + " - " + str(df2.shape[0])
    message_subject = "SFTP LOAD: " + curdate + " - " + str(df2.shape[0])
    fromaddr = 'anthropologyleadsnotification@gmail.com'
    toaddr = 'nieldv@gmail.com'
    message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "Subject: %s\r\n" % message_subject + "\r\n" + message_text
    toaddrs = [toaddr]

    username = 'anthropologyleadsnotification@gmail.com'
    password = '$6#saSH@xcr5vkP1zh'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()


def ugly_load_to_db(FIRSTNAME, LASTNAME, INITIAL, IDNUMBER, POSTALCODE, FROM, EMAIL, REPLYMESSAGE, ORIGINALMESSAGE,
                    ALTCONTACTNUM, DATEOFBIRTH, CAMPAIGNID, CAMPAIGNNAME, SMSSENTTIME, SMSREPLYTIME):
    sql_insert = "INSERT INTO karel_test3 VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14})".format(
        FIRSTNAME,
        LASTNAME,
        INITIAL,
        IDNUMBER,
        POSTALCODE,
        FROM,
        EMAIL,
        REPLYMESSAGE,
        ORIGINALMESSAGE,
        ALTCONTACTNUM,
        DATEOFBIRTH,
        CAMPAIGNID,
        CAMPAIGNNAME,
        SMSSENTTIME,
        SMSREPLYTIME)

    con = pymysql.connect(host="154.0.171.86",
                          user="niel",
                          password="L3adsu$ER",
                          db="leads",
                          cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as curr:
        curr.execute(sql_insert)
        curr.close()

    con.commit()
    con.close()
