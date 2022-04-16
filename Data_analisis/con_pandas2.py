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


