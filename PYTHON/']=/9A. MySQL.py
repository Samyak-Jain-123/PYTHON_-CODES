# Connectivity b/w PYTHON & MYSQL

'Install MySQL Connector ---> pip3 install mysql-connector-python'


# 1. Import the connector
import mysql.connector as mc



# 2. Create 'Connection' that establishes the connection b/w python and mysql.
Con = mc.connect(
    host = "localhost",
    user = "root", 
    password = "20081983",) 
  # database = "Delivery")                              # Optional

if Con:                                        
    print("Connection established...")



# 3. Create a 'Pointer' that is used to interact with the database.
Pointer = Con.cursor()

if Pointer:
    print("Pointer created...")                 





#1 Create Database
Pointer.execute("CREATE DATABASE PYTHON;")
print("Database PYTHON Created...")



#2 Use Database
Pointer.execute("USE PYTHON;")
print("Using database PYTHON...")



#3 Create Table
Pointer.execute("CREATE TABLE LEARNERS (Roll_no INT PRIMARY KEY, Name VARCHAR(50), Age INT);")
print("Table LEARNERS Created...")



#4 Insert values
Pointer.execute("""INSERT INTO LEARNERS VALUES 
                (101,'Geeta',14),
                (102,'Priya',13),
                (103,'Shiva',16);""")

Con.commit()
print("Values_1 inserted successfully...")
print(Pointer.rowcount, "records inserted...")

'OR' 

Sql = 'INSERT INTO LEARNERS VALUES(%s,%s,%s);'
Values = (104,'Dhruv',12)

Pointer.execute(Sql, Values)
Con.commit()

print("Values_2 inserted successfully...")
print(Pointer.rowcount, "records inserted...")


'OR'

Sql = 'INSERT INTO LEARNERS VALUES(%s,%s,%s);'
Values = [(105,'Ram',13),(106,'Geeta',14),(107,'Sam',18)]

Pointer.executemany(Sql, Values)
Con.commit()

print("Values_3 inserted successfully...")
print(Pointer.rowcount, "records inserted...")



#5 Show databases
Pointer.execute("SHOW DATABASES;")
print("Showing Databases...")

result = Pointer.fetchall()

print(result)

'OR'

for i in result:
    print(i, i[0])



#6 Show tables
Pointer.execute("SHOW TABLES;")
print("Showing Tables...")

result = Pointer.fetchall()
print(result)
print(result[0])
print(result[0][0])



#7 Selecting Records
Pointer.execute("SELECT * FROM LEARNERS;")
print("Selecting all from LEARNERS...")

result = Pointer.fetchall()
print(result)

'AND'

Pointer.execute("SELECT * FROM LEARNERS;")
print("Selecting first record from LEARNERS...")

result = Pointer.fetchone()
print(result)

Pointer.fetchall()                                      # Clears remaining rows

'AND'

Pointer.execute("SELECT * FROM LEARNERS;")
print("Selecting first 3 record from LEARNERS...")

result = Pointer.fetchmany(3)
print(result)

Pointer.fetchall()                                      # Clears remaining rows



#8 Describe Table
Pointer.execute("Describe LEARNERS;")
print("Describing Table LEARNERS...")

result = Pointer.fetchall()
for i in result:
    print(i)



#9 Update Table
Pointer.execute("Update LEARNERS SET AGE = 15 WHERE Roll_no = 101;")
Con.commit()

print("Data_1 updated successfully...")
print(Pointer.rowcount, "records updated...")

'OR'

Sql = 'Update LEARNERS SET AGE = %s WHERE Roll_no = %s;'
Values = (13,104)

Pointer.execute(Sql, Values)
Con.commit()

print("Data_2 updated successfully...")
print(Pointer.rowcount, "records updated...")

'OR'

Sql = 'Update LEARNERS SET AGE = %s WHERE Roll_no = %s;'
Values = [(14,105),(15,106),(19,107)]

Pointer.executemany(Sql, Values)
Con.commit()

print("Data_3 updated successfully...")
print(Pointer.rowcount, "records updated...")



#10 Alter Table
Pointer.execute("ALTER TABLE LEARNERS ADD COLUMN Marks INT;")
print("COLUMN Marks created...")

Pointer.execute("ALTER TABLE LEARNERS DROP COLUMN Marks;")
print("COLUMN Marks deleted...")

Pointer.execute("ALTER TABLE LEARNERS CHANGE COLUMN name First_Name VARCHAR(50) NOT NULL;")
print("COLUMN name changed to First_Name...")

Pointer.execute("ALTER TABLE LEARNERS MODIFY COLUMN First_Name VARCHAR (150) NOT NULL;")
print("COLUMN First_Name modified...")



#11 Delete records
Pointer.execute("DELETE FROM LEARNERS WHERE Roll_no = 101")
Con.commit()

print("Data_1 deleted successfully...")
print(Pointer.rowcount, "records deleted...")

'OR'

Sql = "DELETE FROM LEARNERS WHERE Roll_no = %s;"
Values = (105,)

Pointer.execute(Sql, Values)
Con.commit()

print("Data_2 deleted successfully...")
print(Pointer.rowcount, "records deleted...")

'OR'
 
Sql = "DELETE FROM LEARNERS WHERE Roll_no = %s;"
Values = [(103,),(106,),(107,)] 

Pointer.executemany(Sql, Values)
Con.commit()

print("Data_3 deleted successfully...")
print(Pointer.rowcount, "records deleted...")



#12 Truncate Table
Pointer.execute("TRUNCATE TABLE LEARNERS;")
print("All records deleted from table PYTHON...")



#13 Drop Table
Pointer.execute("DROP TABLE LEARNERS;")
print("Table LEARNERS deleted...")



#14 Drop Database
Pointer.execute("DROP DATABASE PYTHON;")
print("Database PYTHON deleted...")



#15 Close connection
Pointer.close()
Con.close()

print("Connection closed...")





# Practise 1 (User Input Program)
#1
Con = mc.connect(
    host = "localhost",
    user = "root", 
    password = "20081983",)


#2
Pointer = Con.cursor()


#3
Pointer.execute("CREATE DATABASE IF NOT EXISTS PYTHON;")
print("Database PYTHON Created...")


#4
Pointer.execute("USE PYTHON;")
print("Using database PYTHON...")


#5
Pointer.execute("CREATE TABLE IF NOT EXISTS LEARNERS(LearnerID INT PRIMARY KEY, LearnerName VARCHAR(50), Countryname VARCHAR(50));")
print("Table LEARNERS Created...")


#6
while True:
    print("Press any Key to insert records and to exit the program enter -->  Q")
    x = input("Enter a input: ")

    if x.upper() == "Q":
      break

    a = int(input("Enter LearnerID: "))
    b = input("Enter LearnerName: ")    
    c = input("Enter the Countryname: ")
 
    Sql = 'INSERT INTO LEARNERS values(%s,%s,%s)'
    Values = (a,b,c)

    Pointer.execute(Sql, Values)

    Con.commit()
print("Records Successfully stored...")


#7
Pointer.execute("SELECT * FROM LEARNERS;")

print("Selecting all from LEARNERS...")

result = Pointer.fetchall()
for i in result:
    print(i)


#8
Pointer.execute("DROP TABLE LEARNERS;")
print("Table LEARNERS deleted...")


#9
Pointer.execute("DROP DATABASE PYTHON;")
print("Database PYTHON deleted...")


#10
Pointer.close()
Con.close()

print("Connection closed...")

