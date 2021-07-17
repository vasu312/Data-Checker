import sqlite3

conc = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

crsr = conc.cursor()
crsr.execute("DROP TABLE MyDBTable;")
crsr.execute('''CREATE TABLE MyDBTable (
                 ID INTEGER,
                 Name VARCHAR(15),
                 City VARCHAR(10)
                 );''')


student_data = [("1","Vasudevan","03-01-2002"),
                ("2","Udhayakumar","15-10-2001"),
                ("3","Naveen","25-07-2002")]

for p in student_data:
    format_str = """ INSERT INTO
                     MyDBTable(ID,Name,City)      
                     Values("{vid}","{vname}","{vcity}"); """ # {} --> Space Holder
    sql_command = format_str.format(vid = p[0],vname=p[1],vcity=p[2])

    crsr.execute(sql_command)

conc.commit()
conc.close()
print("Record Added")
