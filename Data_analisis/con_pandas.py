import pandas as pd



"Agrupacion y clasificacion"

df = pd.read_csv("WineQT.csv")

#Un ejemplo sencillo de agrupacion de los datos es ordenarlos segun, por ejemplo, la columna pH
print (df.groupby(by="pH").mean())

#En lugar de agrupar solo por una columna, lo podemos hacer con varias a la vez. El parametro de agrupacion es la media de las tres columnas en este caso
print (df.groupby(by=["fixed acidity","volatile acidity","citric acid"]).mean())

#Vamos a clasificar el dataframe segun el pH, de manera ascendente
df["pH_rank"] = df["pH"].rank(ascending=1)
#Seleccionamos la nueva columna creada (pH_rank) como el indice del dataframe
df = df.set_index("pH_rank")
df = df.sort_index()
#Ordenamos el indice y lo mostramos por pantalla
print (df)
#De esta manera podemos observar que para los valores en los que el pH es el mismo, se hace la media de los puestos que ocupan
#Como el caso de 2.88, que ocupan el tercer y cuarto puesto, por lo tanto la media es 3.5 que es el valor que aparece en el indice



"Tipos de datos y valores perdidos"

#Vamos a reemplazar los valores perdidos (NaN), ya que no conviene eliminarlos al perderse muchos datos del dataset

df = pd.read_csv("WineQT.csv")

#Funcion que devuelve el promedio redondeado de una columna dek dataset
def promedio(string):
    return round(df["{}".format(string)].mean())

lista_df = list(df)

#Con este bucle sustituiriamos cada valor perdido por la media de la columna en la que se encuentra dicho valor
#Sin embargo al no haber ningun valor perdido da error
try:
    for i in lista_df:
        df["{}".format(i)].replace(df.nan, promedio(i))
except:
    raise AttributeError("No hay ningun valor perdido en el dataframe")