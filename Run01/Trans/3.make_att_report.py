import MySQLdb
from datetime import datetime , time, tzinfo, timedelta

database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "hr")

# Get the cursor, which is used to traverse the database, line by line
mob_read_cursor = database.cursor()
att_read_cursor = database.cursor()
insert_cursor = database.cursor()
erp_read_cursor = database.cursor()

tbl1_name="mob_data"
tbl2_name="att_stage01"
tbl3_name="erp_report"
tbl4_name="att_report"

startdate = datetime(int(2017),int(9),21)
#print startdate.strftime('%Y-%m-%d')

# Create the Select sql query
mob_query = """SELECT * FROM `"""+tbl1_name+"""` WHERE `Employee_ID`LIKE %s;"""
att_query = """SELECT * FROM `"""+tbl2_name+"""` WHERE `ID`LIKE %s;"""
erp_query = """SELECT * FROM `"""+tbl3_name+"""`;"""

# Execute sql Query
erp_read_cursor.execute(erp_query)
erp_count = erp_read_cursor.rowcount

erp_row = erp_read_cursor.fetchone()
ic=0

while erp_row is not None:
    #if erp_row[0] == "02031":
    print erp_row
    #else:
    #    erp_row = erp_read_cursor.fetchone()
    #    continue

    att_read_cursor.execute(att_query,'%'+str(erp_row[0]))
    #att_read_cursor.execute(att_query,'%02015')
    att_row = att_read_cursor.fetchall()
    att_count = att_read_cursor.rowcount
    att_date_cr = 0 

    mob_read_cursor.execute(mob_query,'%'+str(erp_row[0]))
    #mob_read_cursor.execute(mob_query,'%02015')
    mob_row = mob_read_cursor.fetchone()
    mob_count = mob_read_cursor.rowcount

    val_id = str(erp_row[0])
    print "\nERP ID = "+ val_id
    #print "c = "+str(erp_read_cursor.rownumber)+" erp_count: "+str(erp_count) + " att_count: "+str(att_count) + " mob_count: "+str(mob_count)
   
    #print str(erp_row)
    insert_query="" 
 
    val_LS_list=[];

    for day in range(1,32):
        val_LS = ""
        if mob_count > 0:
            mob_date = startdate+timedelta(days=day-1)
            mob_LS = str(mob_row[day+1])
            val_LS = mob_LS.upper()

            #print "\n\nMOB ID = "+mob_date.strftime('%Y-%m-%d') + " Day"+str(day)+" is "+val_LS    
        if att_count > 0:
            att_date = datetime.strptime(str(att_row[att_date_cr][1]), '%d/%m/%Y')
            delt = att_date-(startdate+timedelta(days=day-1))
            #print delt.days
            if delt.days == 0:
                att_LS = str(att_row[att_date_cr][2])
                att_date_cr=att_date_cr+1
                if mob_count > 0:
                    if mob_LS.upper() != "A":
                        val_LS = mob_LS.upper()
                    else:
                        val_LS = att_LS.upper()
                else:
                    val_LS = att_LS.upper()
            else:
                #print "Date Difference: "
                att_date = startdate+timedelta(days=day-1)
                att_LS = ""
            
        erp_date = startdate+timedelta(days=day-1)
        erp_LS = str(erp_row[day+7])

        if att_LS.upper() == "P":
            val_LS = att_LS.upper()            
        else:
            if val_LS =="A":
                pass
            #else:
            #    val_LS ="P"
                
        if erp_LS != "":
            val_LS = erp_LS

        #print "ATT ID = "+att_date.strftime('%Y-%m-%d') + " Day"+str(day)+" is "+att_LS
        #print "ERP ID = "+erp_date.strftime('%Y-%m-%d') + " Day"+str(day)+" is "+erp_LS

        val_LS_list.insert(day,val_LS);

        insert_query = """INSERT INTO `att_report` (`ID`, `Date`, `Leave_status`) VALUES ('"""+val_id+"""','"""+erp_date.strftime('%d-%m-%Y')+"""','"""+val_LS+"""');"""  
        #print insert_query
        ic=ic+1
        insert_cursor.execute(insert_query)

    erp_row = erp_read_cursor.fetchone()

# Close the cursor
mob_read_cursor.close()
att_read_cursor.close()
erp_read_cursor.close()
insert_cursor.close()
#xexit()
# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done!"
print "I just imported "  + str(ic) + " rows to MySQL!"