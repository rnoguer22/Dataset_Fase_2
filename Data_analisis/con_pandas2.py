#Importamos pandas
import pandas as pd

#Crear, leer y escribir
#Para crear un archivo csv con pandas usamos el método pd.DataFrame:

columnas = {"columna 1": ["datos de la columna"], "columna 2": ["datos de la columna"]}
archivo = pd.DataFrame(data=columnas)
#Esto nos devolverá una tabla con los datos proporcionados anteriormente
print(archivo)

#Para leer un archivo csv con pandas usamons el método pd.read_csv:
wineqt = pd.read_csv("WineQT.csv") #Para leerlo desde un archivo
wineqt_link = pd.read_csv(r"https://github.com/rnoguer22/Dataset_Fase_2/blob/main/WineQT.csv") #Para leerlo desde una URL

#Para escrbir en un archivo csv usamos el método pd.to_csv:
archivo.to_csv("WineQT.csv", mode="a") #Ponemos el mode a para que añada al csv y no reemplace los datos que hay ya escritos


#Indexación, selección y asignación
#Selección de una columna:
wine = pd.read_csv("WineQT.csv")
columna_elegida = wine["density"]
print(columna_elegida)

#Selección de varias columnas:
columnas_elegidas = wine[["chlorides", "density", "pH"]]
print(columnas_elegidas)

#Selección de una fila
fila_elegida = wine.iloc[6]
print(fila_elegida)

#Seleccion de varias filas
filas_elegidas = wine.iloc[[6, 13]]
print(filas_elegidas)

#Seleccionar filas y columnas
subtabla1 = wine.ix[[6, 13], ["chlorides", "density", "pH"]]
print(subtabla1)

#Seleccionar todas las filas y alguna columna
subtabla2 = wine.loc[:, ["chlorides", "density", "pH"]]
print(subtabla2)







