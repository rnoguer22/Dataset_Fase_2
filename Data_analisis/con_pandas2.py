#Importamos pandas
import pandas as pd

#Crear, leer y escribir
#Para crear un archivo csv con pandas usamos el método pd.DataFrame:

columnas = {"columna 1": ["datos de la columna"], "columna 2": ["datos de la columna"]}
archivo = pd.DataFrame(data=columnas)
#Esto nos devolverá una tabla con los datos proporcionados anteriormente
print(archivo)
