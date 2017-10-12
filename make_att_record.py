import xlrd
import MySQLdb
from array import *
from datetime import datetime, time, tzinfo, timedelta
def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return substring + s[:-amount]

def right(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[-amount:]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return s[:-amount] + substring
    
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "hr")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()
insert_cursor = database.cursor()

tbl_filename="ac_data"
uid="02074"
# Create the Select sql query
query = """SELECT * FROM `"""+tbl_filename
print query

# Execute sql Query
cursor.execute(query)

count = cursor.rowcount
print count
c=0
insert_tbl = raw_input("Enter staging table name: ")
queryBOL = """INSERT INTO `"""+insert_tbl+"""`(`ID`, `Date`, `Leave_status`) VALUES ("""
insert_query=""

row = cursor.fetchone()
while row is not None:
  if c==10:
      pass
      #exit()
  else:
      pass
  #print(row)
  #print "ID = "+row[0]

  if left(row[0],2).upper()=="RI":
      raw_ri_id = str(right(row[0],(len(row[0])-2)))
      #ri_id = '{:05d}'.format(raw_ri_id)
      ri_id = raw_ri_id.rjust(5,'0')
      print "RI -id "+ str(ri_id)
  else:
      ri_id = row[0]

  #print "Name = "+row[1]
  #print "Date ="+row[2]
  if row[3]=="":
    intime = datetime.strptime('0:0:0', '%H:%M:%S')
  else:
    intime = datetime.strptime(row[3], '%H:%M:%S')
  if row[4]=="":
    outime = datetime.strptime('0:0:0', '%H:%M:%S')
  else:
    outime = datetime.strptime(row[4], '%H:%M:%S')

  #outime=  datetime.strptime(row[4], '%H:%M:%S')
  uptime = outime - intime
  if uptime.seconds==0:
        # print "Absent"
        leavestatus="A"
  else:
        leavestatus="P"
        #print "Present"
  #print str(uptime.seconds) 
  insert_query = queryBOL+"""'"""+str(ri_id)+"""','"""+row[2]+"""','"""+leavestatus+"""');"""
  print insert_query
  insert_cursor.execute(insert_query)

  c=c+1
  #print "Leave Status ="+str(time.timedelta(seconds=int(uptime)))
#  break
  row = cursor.fetchone()

#exit()
# Close the cursor
cursor.close()
insert_cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done!"
print "I just imported "  + str(c) + " rows to MySQL!"
