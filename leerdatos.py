import pymssql
import os
import numpy as np

# sqlserver <-- especifico.
# odbc <-- generico

conn: pymssql.Connection = pymssql.connect("104.36.110.17"
                                           , os.environ['usuariopython']
                                           , os.environ['claveypython']
                                           , "sales1")

cursor: pymssql.Cursor = conn.cursor(as_dict=False) # devolver datos como tuplas

sql="select top(100) SalesID,Quantity from sales where ProductId=%s"

idproducto=input("indique el numero del producto")

cursor.execute(sql,(idproducto))

ventas=cursor.fetchall()  # listado de tuplas

ventas2:np.ndarray =np.array(ventas)  # ndarray

total=ventas2.sum() # sume la segunda columna
print(f"\nel total es {total}")
# total2=ventas2[:,1]*2


# print(ventas2)

cursor.close()
conn.close()




