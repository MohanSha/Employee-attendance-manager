1. Create a table structure in a excel with 1'st row as Column_name, Data_Type, Length. 
        
 Example: 
        filenames : ac_data_tbl.xls ,erp_report_tbl.xls, mob_data_tbl.xls, ac_report_tbl.xls, att_report_tbl.xls, att_stage01_tbl.xls, calendar_tbl.xls, email_tbl.xls, holiday_tbl.xls        
        
        Column_name Data_Type Length
            ID       varchar    100

Note: All filenames must have _tbl in the end
      Column_name should not have any spaces,special characters except underscore(_)
      Only contain 1 sheet named Sheet1
      save as filename_tbl.xls
2.  Run createtbl.py with following command in command prompt 
        C:\Users\Mohan sha>python createtbl.py

    when prompted for to Enter Table Excel Filename enter any one from the above filenames <filename>.xls
        Enter Table Excel Filename : ac_data_tbl.xls

Note: Repeat step 1 & step 2 for all the tables structure
      you should have all the above mentioned filenames and proceed further

3. Check the filetype of the data to import either a .xls file or .csv file

    3.1 If data is in .xls format run importdata.py and when prompted to enter the table name for the excel enter the filename with extension and skip step 3.2.
        Example: filename is ac_data.xls
                 C:\Users\Mohan sha>Enter table excel filename : ac_data.xls

    3.2 If data is in .csv format run import_csvdata.py and when prompted to enter the table name for the excel enter the filename with extension
        Example: filename is erp_report.csv
                 C:\Users\Mohan sha>Enter table excel filename : erp_report.csv
 

Note: Repeat Step 3 to import data to all the above created tables(filenames).
      Recommended .xls format data
      Column_name should be same as table structures
      Only contain 1 sheet named Sheet1

4. For Holiday data run holiday.py
        Example: C:\Users\Mohan sha>python holiday.py
     
5. For calendar data run calendar.py
        Example: C:\Users\Mohan sha>python calendar.py

6. Run make_att_record.py to combine access card data(ac_data) and mobile data(mob_data) into single data and updated in table att_stage01 
       C:\Users\Mohan sha>python make_att_record.py

7. Run merge2.py to combine data from above step (att_stage01) and ERP report data(erp_report) into single data and updated in table att_report
       C:\Users\Mohan sha>python merger2.py
    
    Now we will get all data from access card, mobile and ERP into a single merged data(att_report)

8. Run holiday_att.py to update paid holiday's list(PH) for all the employees in att_report

9. Run calendar_att.py to update weekoff list(WO) for all the employees in att_report

10. Run email_att.py to send attendance to all the employees and wait for it print "ALL Done"


      

       