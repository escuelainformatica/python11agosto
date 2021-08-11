import numpy as np

# ndarray (shape 3,3)
matriz=np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
)
print(matriz[0,0]) # 1

print(matriz[1,2]) # 6

print(matriz[2,:]) # [7 8 9] la fila 2  (: indica un rangos)

print(matriz[2,1:]) # [8,9]  la fila 2 y la columna 1 hasta el final

print(matriz[:,1]) # [2,5,8] toda la columna 1

columna2:np.ndarray=matriz[:,2]
print(columna2.sum()) # [3,6,9] = 18
print(np.sum(columna2)) # 18

matriz2x2=np.array([
    #4,6
    [1,2], # 3
    [3,4]  # 7
])
print(np.sum(matriz2x2))   # 10
print(np.sum(matriz2x2,axis=0))   # sume las columnas [4,6]
print(np.sum(matriz2x2,axis=1))   # sume las filas [4,6]

matriznormal=[[1,2],[3,4]]
print(matriznormal[0][0]) # 1 (numpy matriz[0,0])




# shape (4)
paises=numpy.array(["chile","argentina","peru","bolivia"])

print(paises[1:])