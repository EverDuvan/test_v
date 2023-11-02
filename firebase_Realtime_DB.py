from firebase import firebase
import pandas as pd

# Aqui se agrega la url de la base de datos asignada por Firebase
firebase = firebase.FirebaseApplication('https://dbtest-1a464-default-rtdb.firebaseio.com/', None)

# Aqui se agregan los datos a insertar el la tabla de la base de datos
# en cada ejecucion se hace una nueva insercion, incluso de valores repetidos si es el caso

datos = {
    'id':'30',
    'nombre:':'ana',
    'apellido:':'gutierrez'
}

# Aqui se realiza la insercion de los datos en la carpeta <usuarios> en base de datos
# en este caso en la carpeta usuarios de firebase
resultado = firebase.post('/usuarios',datos)

# Aqui se imprime la llave o direccion en la que se hizo la insercion
print (resultado)

# Aqui se lee la informacion de la carpeta <usuarios> en base de datos
leer = firebase.get('/usuarios',None)
print (leer)

# Aqui se crea un dataframe para visualizar los datos
df = pd.DataFrame(leer)

# Aqui se cambia el indice del dataframe
df = df.transpose()

# Aqui se imprime el dataframe
print(df)

# Aqui se agrega un nuevo valor a un registro ya creado, en este caso se cambia un id
firebase.put('/usuarios/-NiFY7d0ByCr3uALDBRV','id',10)

# Aqui se elimina un registro
firebase.delete('/usuarios/', '-NiFY7d0ByCr3uALDBRV')

