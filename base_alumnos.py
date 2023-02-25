#VOY A TRABAJAR CON MariaDB

import mariadb

mydb = mariadb.connect(
        host="127.0.0.1",
        user="root",
        autocommit=True
        )


cursor = mydb.cursor()
cursor.execute("CREATE DATABASE GRADO")

mydb = mariadb.connect(
        host="127.0.0.1",
        user="root",
        database = "GRADO"  
        )
cursor.close()

cursor = mydb.cursor()
cursor.execute("CREATE TABLE Alumnos(ID int PRIMARY KEY, NOMBRE VARCHAR(255),APELLIDO VARCHAR(255))")
print("\n -------- Se ha generado la tabla ALUMNOS correctamente -----------")
cursor.close()

cursor=mydb.cursor()
x = "INSERT INTO Alumnos(ID,NOMBRE,APELLIDO) VALUES (%s,%s,%s)"
q = [(1,"german","ponzio"),(2,"luis","viale"),(3,"alfaro","ritchmond"),(4,"jose","olinden"),
     (5,"juan","perez"),(6,"roberto","carlos"),(7,"roxana","rico"),(8,"pedro","gerez")]
cursor.executemany(x,q)
mydb.commit()
print("\n---------------", cursor.rowcount,"Registros insertados correctamente")
for h in q:
    print(h)
cursor.close()

cursor=mydb.cursor()
x = "SELECT * FROM Alumnos where NOMBRE LIKE  '%german%'"
cursor.execute(x)
resultado = cursor.fetchall()
for i in resultado:
    print(f"El alumno encontrado con ese nombres es \n {i}")
    
cursor.close()    




"""
mycursor = mydb.cursor()
sql = "SELECT * FROM cliente where nombre LIKE '%Ana%' "
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""

