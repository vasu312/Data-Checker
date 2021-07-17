# 1) DB_Program - Fetch All
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Students")
data = cursor.fetchall()
for value in data:
    print (value)
'''
# 2) DB_Program - Fetch One
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Students")
data = cursor.fetchone()
while data is not None: #Data Value
    print(data)
    data = cursor.fetchone() #Next Line
'''
# 3) DB_Program - Fetch Many
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Students")
data = cursor.fetchmany(2)
print(data)
'''
# 4) DB_Program - DISTINCT
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT(Name) FROM Students")
data = cursor.fetchall()
print(data)
'''
# 5) DB_Program - Count
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*)FROM Students")
data = cursor.fetchall()
print(data)
'''
# 6) DB_Program - WHERE
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("SELECT ID,Name FROM Students WHERE ID >2")
data = cursor.fetchall()
print(data,sep='\n')
'''
# 7) DB_Program - DELETE
'''
import sqlite3
connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")
cursor = connection.cursor()
cursor.execute("DELETE FROM Students WHERE ID = '4' ")
connection.commit()
print("Succecfully Deleted")
connection.close()
'''
