#Analizamos la calidad de los vinos, la parte que más nos importa del Dataset

import pandas as pd

datos = pd.read_csv("WineQT.csv", header=0)

print(datos["quality"])