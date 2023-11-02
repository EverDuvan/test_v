FIREBASE

- ******** Firebase *********

Para crear una base de datos en Firebase,sigue los siguientes pasos:

Primero, necesitas crear un proyecto en Firebase. Ve a Firebase console y agrega un nuevo proyecto

pagina: https://console.firebase.google.com/

Una vez que creas tu proyecto, espera un par de minutos para que se complete el setup en Firebase

Después de la configuración, serás enviado al panel principal de tu proyecto. Aquí, puedes crear tu primera base de datos. Haz clic en "Crear base de datos" y elige la opción "modo de pruebas" y "Realtime Database"

Nota: Es importante cambiar las reglas de seguridad cuando tu proyecto se encuentre en producción

ejemplo de insersion,cambio, borrado y transformacion a df de datos en bd firebase con python. se instalan dependencias 

pip install firebase

pip install pandas

```python
from firebase import firebase
import pandas as pd

# Aqui se agrega la url de la base de datos asignada por Firebase
firebase = firebase.FirebaseApplication('<URL aqui>', None)

# Aqui se agregan los datos a insertar el la tabla de la base de datos
# en cada ejecucion se hace una nueva insercion, incluso de valores repetidos si no hay cambios

datos = {
    'id':'30',
    'nombre:':'ana',
    'apellido:':'gutierrez'
}

# Aqui se realiza la insercion de los datos en la carpeta <usuarios> en base de datos
resultado = firebase.post('/usuarios',datos)

# Aqui se imprime la llave o direccion en la que se hizo la insercion
# ejemplo que será usado adelante, se vería asi en consola: -NiFY7d0ByCr3uALDBRV
print (resultado)

# Aqui se lee la informacion de la base de datos
leer = firebase.get('/usuarios',None)
print (leer)

# Aqui se crea un dataframe para visualizar los datos
df = pd.DataFrame(leer)

# Aqui se cambia el indice del dataframe
df = df.transpose()

# Aqui se imprime el dataframe
print(df)

# Aqui se agrega un nuevo valor a un registro ya creado
# pasando la carpeta /usuarios/ y el identificador de el registro ´-NiFY7d0ByCr3uALDBRV´
# en este caso se cambia un id
firebase.put('/usuarios/-NiFY7d0ByCr3uALDBRV','id',10)

# Aqui se elimina un registro
firebase.delete('/usuarios/', '-NiFY7d0ByCr3uALDBRV')

WHATSAPP MSJS

