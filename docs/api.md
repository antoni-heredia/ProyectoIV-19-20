# API

 Para probar la API, una vez que esta iniciado el servicio con make start, podemos ir a [http://0.0.0.0:8080/doc/](http://0.0.0.0:8080/doc/). Ahi se encuentra una herramienta construida con [swagger.io](swagger.io) donde podemos probar las rutas que tengo actualmente en la API. 

Aunque no tengo todavia completamente desplegado el sistema. Podemos ver el funcionamiento de swagger desde [aquí](https://wallyfinder.herokuapp.com/doc/). 

## Diferentes rutas de la api
### /status
Si el sistema esta en marcha nos devolverá ```{'status':'OK'}```` con el código 200.
### /imagen
#### get
Nos devolverá una lista de todas las imágenes que existen en el sistema con el código 200. 
#### delete
Nos sirve para eliminar TODAS las imagenes que tengamos en la base de datos.  Devolverá ```{'Imagenes eliminada': 'true'}``` con el código 200

### /imagen/\<nombre\>
#### get
Nos sirve para descargar una imagen a partir de su nombre. Si la imagen existe la devuelve y ademas nos da el código 200. En caso de que no exista devolverá ```{'Imagen encontrada':'False'}``` con el código 404.
#### post
Esta manejador sirve para enviar una imagen y hacer que se encuentre a wally en ella. Tiene que recibir un formulario con el nombre: ```image```. En caso de que no se reciba dicho formulario devolverá ```{'Imagen recibida': 'false'}```  y el código 404. Si la recibe bien devolvera ```{'Imagen recibida': 'true'}``` y el codigo 200.

### Manejador de errores
En caso de que se solicite una ruta que no esta gestionada por la aplicación devolverá el codigo 404 y ```"Pagina no encontrada. Error 404"```.

## Test sobre la api
Ademas he añadido una serie de test para comprobar que la api funciona de forma adecuada. 

### test_estado
Prueba que /status este en funcionamiento y que deuvlevá el código 200.
### test_imagen_mnombre
Comprueba que la api devuelva una imagen cuando se le pide y que devuelva el codigo 200.
### test_imagen
Comprueba que la api devuleve la lista con todas las imag enes disponibles en la base de datos. 