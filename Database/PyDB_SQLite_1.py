import sqlite3 # Database Module

# Connection
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/Academy.db")

cursor = connection.cursor()

cursor.execute("DROP Table Students")

sql_command = ''' CREATE TABLE Students(
                  RollNo INTEGER PRIMARY KEY,
                  Name VARCHAR(20),
                  Grade CHAR(1),
                  Gender CHAR(1),
                  Average DECIMAL(5,2),
                  Birth_Date DATE ); '''
cursor.execute(sql_command) #Querry Execution

sql_command1 = '''INSERT INTO

                 Students(RollNo,Name,Grade,Gender,Average,Birth_Date)
                 Values(null,"Vasudevan",'A',"Male","95.5","03-01-2002")
                 ;'''

cursor.execute(sql_command1)
connection.commit()     # Save The DB
