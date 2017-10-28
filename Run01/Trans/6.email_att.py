import smtplib
import MySQLdb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime , time, tzinfo, timedelta

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
    bcc="sathishkumar.k@qubecinema.com"
    #bcc=""
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = "HR Desk"
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://localhost/attend/attreport.php">online</a>!"""
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('postman.realimage.co.in:25')
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    password = "2011Ppc@1056"
 
    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO,bcc], MESSAGE.as_string())
    server.quit()


database = MySQLdb.connect (host="localhost", user = "attend", passwd = "attend01", db = "hr")

# Get the cursor, which is used to traverse the database, line by line
att_read_cursor = database.cursor()

tbl1_name="att_report"
tbl2_name="erp_report"
tbl3_name="email"

startdate = datetime(int(2017),int(8),21)
#print startdate.strftime('%Y-%m-%d')

testid = raw_input("Enter Employee ID to generate email : [Enter 0 for all] ")
if testid==0:
    # Create the Select sql query
    att_query = """SELECT A.ID,B.Employee_Name,A.Date,A.Leave_status,C.Email_Id FROM `att_report` A,`erp_report` B, `email` C WHERE A.ID=B.E_code AND A.ID=C.Emp_Code;"""
else:
    att_query = """SELECT A.ID,B.Employee_Name,A.Date,A.Leave_status,C.Email_Id FROM `att_report` A,`erp_report` B, `email` C WHERE A.ID=B.E_code AND A.ID=C.Emp_Code AND A.ID='"""+testid+"""';"""

# Execute sql Query
att_read_cursor.execute(att_query)
att_count = att_read_cursor.rowcount

att_row = att_read_cursor.fetchone()
ic=0

content="""
"""
att_date_list=[]
att_ls_list=[]



while att_row is not None:
    print att_row
    prev_id = att_row[0]
    prev_name = att_row[1]
    prev_email = att_row[4]
    for day in range(1,32):
        att_date_list.insert(day,att_row[2]);
        att_ls_list.insert(day,att_row[3]); 
        att_row = att_read_cursor.fetchone() 
        if att_row is None:
            curr_id = ""
            curr_name = ""
            curr_email = ""
        else:
            curr_id = att_row[0]
            curr_name = att_row[1]
            curr_email = att_row[4] 
        if curr_id != prev_id:
            if __name__ == "__main__":
                """Executes if the script is run as main script (for testing purposes)"""
                dt1 = datetime.strptime(att_date_list[0], '%d-%m-%Y')
                dt2 = datetime.strptime(att_date_list[1], '%d-%m-%Y')
                dt3 = datetime.strptime(att_date_list[2], '%d-%m-%Y')
                dt4 = datetime.strptime(att_date_list[3], '%d-%m-%Y')
                dt5 = datetime.strptime(att_date_list[4], '%d-%m-%Y')
                dt6 = datetime.strptime(att_date_list[5], '%d-%m-%Y')
                dt7 = datetime.strptime(att_date_list[6], '%d-%m-%Y')
                dt8 = datetime.strptime(att_date_list[7], '%d-%m-%Y')
                dt9 = datetime.strptime(att_date_list[8], '%d-%m-%Y')
                dt10 = datetime.strptime(att_date_list[9], '%d-%m-%Y')
                dt11 = datetime.strptime(att_date_list[10], '%d-%m-%Y')
                dt12 = datetime.strptime(att_date_list[11], '%d-%m-%Y')
                dt13 = datetime.strptime(att_date_list[12], '%d-%m-%Y')
                dt14 = datetime.strptime(att_date_list[13], '%d-%m-%Y')
                dt15 = datetime.strptime(att_date_list[14], '%d-%m-%Y')
                dt16 = datetime.strptime(att_date_list[15], '%d-%m-%Y')
                dt17 = datetime.strptime(att_date_list[16], '%d-%m-%Y')
                dt18 = datetime.strptime(att_date_list[17], '%d-%m-%Y')
                dt19 = datetime.strptime(att_date_list[18], '%d-%m-%Y')
                dt20 = datetime.strptime(att_date_list[19], '%d-%m-%Y')
                dt21 = datetime.strptime(att_date_list[20], '%d-%m-%Y')
                dt22 = datetime.strptime(att_date_list[21], '%d-%m-%Y')
                dt23 = datetime.strptime(att_date_list[22], '%d-%m-%Y')
                dt24 = datetime.strptime(att_date_list[23], '%d-%m-%Y')
                dt25 = datetime.strptime(att_date_list[24], '%d-%m-%Y')
                dt26 = datetime.strptime(att_date_list[25], '%d-%m-%Y')
                dt27 = datetime.strptime(att_date_list[26], '%d-%m-%Y')
                dt28 = datetime.strptime(att_date_list[27], '%d-%m-%Y')
                dt29 = datetime.strptime(att_date_list[28], '%d-%m-%Y')
                dt30 = datetime.strptime(att_date_list[29], '%d-%m-%Y')
                dt31 = datetime.strptime(att_date_list[30], '%d-%m-%Y')
                email_content = """
                <html>
                <head>
                    <title>Employee Attendance</title>
                    <style>
                        table,tr,th,td
                        {
                            white-space: nowrap;
                            border-collapse: collapse;
                            border: 1px solid black; 
                            padding:5px;       
                        }
                    </style>
                </head>
                <body>
                    Dear """+prev_name+""", <br><br>
                    Your attendance information from 21st """+str(datetime.strftime(dt1,'%b %Y'))+""" to 20th """+str(datetime.strftime(dt30,'%b %Y'))+"""<br><br>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>"""+str(datetime.strftime(dt1,'%d'))+"""<br>"""+str(datetime.strftime(dt1,'%b'))+"""<br>"""+str(datetime.strftime(dt1,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt2,'%d'))+"""<br>"""+str(datetime.strftime(dt2,'%b'))+"""<br>"""+str(datetime.strftime(dt2,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt3,'%d'))+"""<br>"""+str(datetime.strftime(dt3,'%b'))+"""<br>"""+str(datetime.strftime(dt3,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt4,'%d'))+"""<br>"""+str(datetime.strftime(dt4,'%b'))+"""<br>"""+str(datetime.strftime(dt4,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt5,'%d'))+"""<br>"""+str(datetime.strftime(dt5,'%b'))+"""<br>"""+str(datetime.strftime(dt5,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt6,'%d'))+"""<br>"""+str(datetime.strftime(dt6,'%b'))+"""<br>"""+str(datetime.strftime(dt6,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt7,'%d'))+"""<br>"""+str(datetime.strftime(dt7,'%b'))+"""<br>"""+str(datetime.strftime(dt7,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt8,'%d'))+"""<br>"""+str(datetime.strftime(dt8,'%b'))+"""<br>"""+str(datetime.strftime(dt8,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt9,'%d'))+"""<br>"""+str(datetime.strftime(dt9,'%b'))+"""<br>"""+str(datetime.strftime(dt9,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt10,'%d'))+"""<br>"""+str(datetime.strftime(dt10,'%b'))+"""<br>"""+str(datetime.strftime(dt10,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt11,'%d'))+"""<br>"""+str(datetime.strftime(dt11,'%b'))+"""<br>"""+str(datetime.strftime(dt11,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt12,'%d'))+"""<br>"""+str(datetime.strftime(dt12,'%b'))+"""<br>"""+str(datetime.strftime(dt12,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt13,'%d'))+"""<br>"""+str(datetime.strftime(dt13,'%b'))+"""<br>"""+str(datetime.strftime(dt13,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt14,'%d'))+"""<br>"""+str(datetime.strftime(dt14,'%b'))+"""<br>"""+str(datetime.strftime(dt14,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt15,'%d'))+"""<br>"""+str(datetime.strftime(dt15,'%b'))+"""<br>"""+str(datetime.strftime(dt15,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt16,'%d'))+"""<br>"""+str(datetime.strftime(dt16,'%b'))+"""<br>"""+str(datetime.strftime(dt16,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt17,'%d'))+"""<br>"""+str(datetime.strftime(dt17,'%b'))+"""<br>"""+str(datetime.strftime(dt17,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt18,'%d'))+"""<br>"""+str(datetime.strftime(dt18,'%b'))+"""<br>"""+str(datetime.strftime(dt18,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt19,'%d'))+"""<br>"""+str(datetime.strftime(dt19,'%b'))+"""<br>"""+str(datetime.strftime(dt19,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt20,'%d'))+"""<br>"""+str(datetime.strftime(dt20,'%b'))+"""<br>"""+str(datetime.strftime(dt20,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt21,'%d'))+"""<br>"""+str(datetime.strftime(dt21,'%b'))+"""<br>"""+str(datetime.strftime(dt21,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt22,'%d'))+"""<br>"""+str(datetime.strftime(dt22,'%b'))+"""<br>"""+str(datetime.strftime(dt22,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt23,'%d'))+"""<br>"""+str(datetime.strftime(dt23,'%b'))+"""<br>"""+str(datetime.strftime(dt23,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt24,'%d'))+"""<br>"""+str(datetime.strftime(dt24,'%b'))+"""<br>"""+str(datetime.strftime(dt24,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt25,'%d'))+"""<br>"""+str(datetime.strftime(dt25,'%b'))+"""<br>"""+str(datetime.strftime(dt25,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt26,'%d'))+"""<br>"""+str(datetime.strftime(dt26,'%b'))+"""<br>"""+str(datetime.strftime(dt26,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt27,'%d'))+"""<br>"""+str(datetime.strftime(dt27,'%b'))+"""<br>"""+str(datetime.strftime(dt27,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt28,'%d'))+"""<br>"""+str(datetime.strftime(dt28,'%b'))+"""<br>"""+str(datetime.strftime(dt28,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt29,'%d'))+"""<br>"""+str(datetime.strftime(dt29,'%b'))+"""<br>"""+str(datetime.strftime(dt29,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt30,'%d'))+"""<br>"""+str(datetime.strftime(dt30,'%b'))+"""<br>"""+str(datetime.strftime(dt30,'%a'))+"""</th>
                            <th>"""+str(datetime.strftime(dt31,'%d'))+"""<br>"""+str(datetime.strftime(dt31,'%b'))+"""<br>"""+str(datetime.strftime(dt31,'%a'))+"""</th>
                        </tr>
                        <tr>
                            <td align="center">"""+prev_id+"""</td>
                            <td align="center">"""+prev_name+"""</td>
                            <td align="center">"""+att_ls_list[0]+"""</td>
                            <td align="center">"""+att_ls_list[1]+"""</td>
                            <td align="center">"""+att_ls_list[2]+"""</td>
                            <td align="center">"""+att_ls_list[3]+"""</td>
                            <td align="center">"""+att_ls_list[4]+"""</td>
                            <td align="center">"""+att_ls_list[5]+"""</td>
                            <td align="center">"""+att_ls_list[6]+"""</td>
                            <td align="center">"""+att_ls_list[7]+"""</td>
                            <td align="center">"""+att_ls_list[8]+"""</td>
                            <td align="center">"""+att_ls_list[9]+"""</td>
                            <td align="center">"""+att_ls_list[10]+"""</td>
                            <td align="center">"""+att_ls_list[11]+"""</td>
                            <td align="center">"""+att_ls_list[12]+"""</td>
                            <td align="center">"""+att_ls_list[13]+"""</td>
                            <td align="center">"""+att_ls_list[14]+"""</td>
                            <td align="center">"""+att_ls_list[15]+"""</td>
                            <td align="center">"""+att_ls_list[16]+"""</td>
                            <td align="center">"""+att_ls_list[17]+"""</td>
                            <td align="center">"""+att_ls_list[18]+"""</td>
                            <td align="center">"""+att_ls_list[19]+"""</td>
                            <td align="center">"""+att_ls_list[20]+"""</td>
                            <td align="center">"""+att_ls_list[21]+"""</td>
                            <td align="center">"""+att_ls_list[22]+"""</td>
                            <td align="center">"""+att_ls_list[23]+"""</td>
                            <td align="center">"""+att_ls_list[24]+"""</td>
                            <td align="center">"""+att_ls_list[25]+"""</td>
                            <td align="center">"""+att_ls_list[26]+"""</td>
                            <td align="center">"""+att_ls_list[27]+"""</td>
                            <td align="center">"""+att_ls_list[28]+"""</td>
                            <td align="center">"""+att_ls_list[29]+"""</td>
                            <td align="center">"""+att_ls_list[30]+"""</td>
                            
                        </tr>
                    </table>
                    <p><p>Leave Type:</p>
                    <table border="1">
                    <tr>
                        <td> A </td>
                        <td> Not swipe/Not apply in ERP/Reporting officer not authorize </td>
                        <td> PH </td>
                        <td> Paid holiday </td>   
                    <tr>
                        <td> WO </td>
                        <td> Weekly off </td>
                        <td> MATRL </td>
                        <td> Maternity Leave </td>
                    </tr>  
                    <tr>  
                        <td>CL</td>
                        <td>Casual Leave</td>
                        <td>PTL</td>
                        <td>Paternity Leave</td>
                    </tr>
                    <tr>
                        <td>HSL</td>
                        <td>Half-day sick Leave</td>
                        <td>TL1</td>
                        <td>Tenure Leave 1</td>
                    </tr>  
                    <tr>  
                        <td>HCL</td>
                        <td>Half-day Casual Leave</td>
                        <td>TL2</td>
                        <td>Tenure Leave 2</td>
                    </tr>
                    <tr>
                        <td>SL</td>
                        <td>Sick Leave</td>
                        <td>BL</td>
                        <td>Bereavement Leave</td>
                    </tr>
                    <tr>    
                        <td>PL</td>
                        <td>Privilege Leave</td>
                        <td>EL</td>
                        <td>Education Leave</td>
                    </tr>
                    <tr>
                        <td>CO</td>
                        <td>Compensatory off</td>
                        <td>LOP</td>
                        <td>Loss of Pay</td>
                    </tr>
                    <tr>    
                        <td>ML</td>
                        <td>Marriage Leave</td>
                        <td>HOD/OD</td>
                        <td>Half Day OD<strong>/</strong>On Duty</td>
                    </tr>
            </table>
            <p>Note: If any date mentioned as &#34;A&#34; need to be apply in ERP ASAP Else it will be considered as &#34;Loss of pay&#34; in next month. If you have any clarification please revert to me at sathishkumar.k@qubecinema.com. </p> 
            <p>
            Regards<br>
            Team-Payroll</p>
    </body>
    </html>"""
                TO = 'mohansha@qubecinema.com'
                FROM ='mohansha@qubecinema.com'
                SUBJECT = "Your Attendance from "+str(datetime.strftime(dt1,'%b %Y'))+" to "+str(datetime.strftime(dt30,'%b %Y'))
                #print "mail sent for "+prev_id
                #print att_date_list
                #print att_ls_list
                py_mail(SUBJECT, email_content, TO, FROM)
                att_date_list=[]
                att_ls_list=[]
                ic = ic+1
            break

    
    #att_row = att_read_cursor.fetchone()

# Close the cursor
att_read_cursor.close()
#insert_cursor.close()
#xexit()


# Commit the transaction
#database.commit()

# Close the database connection
database.close()


# Print results
print ""
print "All Done!"
print "I just sent "  + str(ic) + " Emails!"