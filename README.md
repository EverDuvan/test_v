# Comprobador de Proxies

Este script de Python verifica la funcionalidad de una lista de proxies con una lista de URLs.

## Requisitos

- Python 3.11.0
- pandas
- requests

## Uso

1. Asegúrate de haber subido las proxies a la base de datos en la tabla "proxies"
(se puede subir un archivo csv con el mismo nombre por cualquier administrador) con una unica columna llamada "ip" para que el script las pueda identificar.
2. Asegúrate de haber subido las urls a la base de datos en la tabla "urls"
(se puede subir un archivo csv con el mismo nombre por cualquier administrador) con las columnas "country", "retail", "country_retail", "url_category" para que el script las pueda identificar.
3. Ejecuta el script con Python: `python main.py`
4. El script creará un nuevo directorio llamado 'proxies_test' si no existe, y guardará un archivo de Excel con los resultados de las pruebas. El archivo se nombrará con la fecha y hora actual.
5. El script creará una nueva tabla (si no existe) en la base de datos llamada "result" con los datos resultantes.

## Funcionamiento

El script lee la lista de proxies y URLs, y luego intenta enviar una solicitud GET a cada URL usando cada proxy. Si la respuesta tiene un código de estado HTTP de 200, se considera que el proxy funciona con esa URL. Si el código de estado no es 200, o si se produce una excepción durante la solicitud (por ejemplo, si la solicitud se agota), se considera que el proxy no funciona con esa URL.

El script utiliza un ThreadPoolExecutor para probar varios proxies en paralelo. El número de hilos se puede ajustar cambiando la variable `num_threads`.

Al final de la ejecución, el script imprime el tiempo total transcurrido.
