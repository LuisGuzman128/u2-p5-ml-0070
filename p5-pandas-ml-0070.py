import numpy as np
import pandas as pd
# Axel Guzman NC 0070
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print(" ---- datos a partir de una martiz 4 x 3 ----")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])
print(df)
# datos a partir de un diccionario
print(" ---- datos a partir de un diccionario ----")
alumno_dicionario={
    "nombre":["Axel","Joel","pedro","Ana","Josafat","Morquecho"],
    "califa":[60,90,100,80,70,50],
    "edad":[64,15,16,16,18,14]
}

estudiante = pd.DataFrame(alumno_dicionario)
print(estudiante)

print("Axel Guzman NC 0070")