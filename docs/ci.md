# Sistema CI

Para la gestión de flujo de trabajo al final he decidido usar [Travis-CI](https://travis-ci.org/) . La elección se debe que es un sistema gratuito y tener integración fácil con github.

El lenguaje que he especificado en  [travis.yml](./.travis.yml) es python que es el que uso para realizar los test y crear el microservicio. Los test solo los voy a realizar desde la version __3.4__ en adelante ya que la versión __2.7__ deja de tener mantenimiento a partir de [Enero de 2020](https://www.python.org/dev/peps/pep-0373/). 

Para que travis pueda realizar los test correctamente tenemos que especificar en el [travis.yml](./.travis.yml):

 ``` 
install:
  - make dependencias
script:
  - make test 
 ```
 La descripción de __install:__ es para que instale las dependencias necesarias para realizar los test y __script:__ es para ver que tiene que ejecutar para realizar los test. 

 Como sistema adicional también he añadido [Circle Ci](https://circleci.com/). La configuración de Circle Ci va en el fichero [.circleci/config.yml](.circleci/config.yml). En la cual especifico que vamos a usar la imagen Docker [circle/python:3.6.4](https://circleci.com/docs/2.0/circleci-images/#python). Y luego le especificamos los siguientes pasos:

1. ```checkout```: Para obtener el codigo
2. ```make initCircle ```: Para instalar las dependencias e iniciar el proyecto.
3. ```make test```: Para ejecutar los test
 
 Como [Circle Ci](https://circleci.com/) funciona un poco diferente a [Travis-Ci](travis-ci.org) he creado otras reglas en el [makefile](./Makefile) para que pueda funcionar. Las dependencias en Circle se deben instalar con el flag  ```--user ``` con los permisos. Ademas Circle no permite ejecutar  ```pytest ``` como comando se tiene que realizar de la siguiente forma:

 ```console
foo@bar:~$ python -m pytest

 ``` 
## Tests
Para realizar los test he usado [pytest](https://docs.pytest.org/en/latest/) como he mencionado mas arriba. 


Realizo los siguiente tests a dia de hoy:
1. Comprobar si lo recibido es una imagen
2. Comprobar que se inserta una imagen a la base de datos
3. Comprobar que se devuelve una imagen de la base de datos
4. Comprobar que se eliminan una imagen de la base de datos. 
5. Comprobar si se pueden eliminar todas las imagenes de la base de datos. 
