import MySQLdb
import datetime as dt
from datetime import datetime , time, tzinfo, timedelta


start_date = dt.datetime(2017, 1, 1)
end_date = dt.datetime(2017, 12, 31)

database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "hr")

insert_cursor = database.cursor()

tbl1_name="calendar"

# Create the Select sql query
query = """SELECT * FROM `"""+tbl1_name+"""`"""
print query

insert_count = insert_cursor.rowcount
#print insert_count

total_days = (end_date - start_date).days + 1 
ctr=0

for day_number in range(total_days):
    current_date = (start_date + dt.timedelta(days = day_number)).date()
    f=datetime.strftime(current_date,'%d-%m-%Y')
    #print current_date
    date = str(datetime.strftime(current_date,'%a'))
    if date=="Sat" or date=="Sun":
        #print date
        insert_query="""INSERT INTO `"""+tbl1_name+"""` (`cal_date`, `cal_day`, `calendar`) VALUES ('"""+str(f)+"""','"""+str(date)+"""','GENERAL')"""
        print insert_query
        # Execute sql Query
        insert_cursor.execute(insert_query)
        ctr=ctr+1

# Close the cursor
insert_cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done!"
print "I just imported "  + str(ctr) + " rows to Calendar!"