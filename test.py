import pandas as pd
  
# diccionario con objeto de diccionario anidado
detalles = { 
    0 : {
        'Nombre' : 'Ankit',
        'Edad' : 22,
        'Universidad' : 'BHU'
        },
    1 : {
        'Nombre' : 'Aishwarya',
        'Edad' : 21,
        'Universidad' : 'JNU'
        },
    2 : {
        'Nombre' : 'Shaurya',
        'Edad' : 23,
        'Universidad' : 'DU'
        }
}
df = pd.DataFrame(detalles)
df = df.transpose()
print(df)