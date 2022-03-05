import pyodbc
# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=17.16.15.100;  DATABASE=companyDB;UID=abc; PWD=xyz;')
cursor=connection.cursor()
cursor.execute("CREATE TABLE table1 (status varchar(10));")
cursor.commit()

for i in cursor:
      if (flag==1):
 
   
           cursor.execute("INSERT INTO table1 VALUES = ? ;", flag)
           cursor.commit()

           
      
      elif(flag==0):
           cursor.execute("INSERT INTO table1 VALUES = ? ;", flag)
           cursor.commit()
           break 
           print("Please stop the belt")
      

    