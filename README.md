[![Build Status](https://travis-ci.org/antoni-heredia/WallysFinder.svg?branch=master)](https://travis-ci.org/antoni-heredia/WallysFinder)
[![CircleCI](https://circleci.com/gh/antoni-heredia/WallysFinder.svg?style=svg)](https://circleci.com/gh/antoni-heredia/WallysFinder)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# Buscador de Wally

## Índice de contenidos

- [Buscador de Wally](#buscador-de-wally)
  - [Índice de contenidos](#%c3%8dndice-de-contenidos)
  - [Descripción](#descripci%c3%b3n)
  - [Implementación](#implementaci%c3%b3n)
  - [Almacenamiento](#almacenamiento)
  - [Dataset de datos a usar](#dataset-de-datos-a-usar)
  - [Herramienta de construcción](#herramienta-de-construcci%c3%b3n)
  - [Sistema CI](#sistema-ci)
  - [Tests](#tests)
  - [Inciar microservicio](#inciar-microservicio)


## Descripción
Este proyecto es para la asignatura de Infraestructura Virtual. Este proyecto consiste en enviar una imagen mediante un formulario web, procesarla buscando a Wally y devolver una imagen donde indique la ubicación del mismo.

## Implementación

La implementación de la API la desarrollare en [Python](https://www.python.org) usando [Flask](https://palletsprojects.com/p/flask/)+[Flask-restful](https://flask-restful.readthedocs.io/en/latest/).. Esta elección se debe a que quiero usar el mismo lenguaje para ofrecer la API como para realizar el procesamiento de la imagen. 

Para encontrar la ubicación de Wally usare [Keras](https://keras.io/) mas específicamente [Faster R-CNN](https://towardsdatascience.com/faster-r-cnn-object-detection-implemented-by-keras-for-custom-data-from-googles-open-images-125f62b9141a). __El entrenamiento de la red neuronal no es parte del microservicio__. Podriamos usar una funcionalidad que ya existiera o usar una entrenada por mi como quiero intentar en este caso. 

Para la gestión de entornos usare [Anaconda](https://www.anaconda.com/) y para los test usare [pytest](https://docs.pytest.org/en/latest/). Esta elección la he hecho ya que creo que son buenas (y fáciles) herramientas para la iniciación en  gestión de entornos y test. 



Para tener un registro de todo lo ocurrido en el sistema utilizare  [logging](https://docs.python.org/3/howto/logging.html). Utilizare como base de referencia [esta presentacion](https://static.sched.com/hosted_files/pycones19/48/El%20show%20de%20Truman.pdf) de [@Jimena_y_yo](https://twitter.com/jimena_y_yo) (Gracias a [JJ](github.com/JJ) por darnos la pista).


## Almacenamiento
Todas las imágenes recibidas, serán almacenadas. (al menos por un tiempo). Esta decisión ha sido debida a que para poder reentrenar  la red natural puedes sernos de utilizad imágenes dadas por los usuario y que no están en nuestro dataset inicial. Asi podemos tener cada vez un sistema mas preciso con son predicciones. Aunque repito, el entrenamiento del sistema no forma parte del microservicio. 

Para esto usaría [MongoDB](https://www.mongodb.com/es) mas específicamente la librería [PyMongo](https://api.mongodb.com/python/current/).


## Dataset de datos a usar

Buscando por github he encontrado un repositorio con imágenes ya clasificadas de Wally. El repositorio tiene licencia [ODbL](https://es.wikipedia.org/wiki/Licencia_Abierta_de_Bases_de_Datos) y se encuentra en el siguiente [link](https://github.com/vc1492a/Hey-Waldo).

## Herramienta de construcción
Python al no tener una herramienta de construcción predeterminada he decidido usar la herramienta ```make```. Para ello he creado el siguiente fichero [Makefile](./Makefile).

Para instalar las dependencias basta con ejecutar:
```console
foo@bar:~$ make dependencias
```
Y para ejecutar los test debemos ejecutar:
```console
foo@bar:~$ make tests
```
Ahora mismo el único test que se realiza es el de comprobar que lo enviado es una imagen, ya que no nos importa el formato especifico. 

Con ```make init``` podremos iniciar el microservicio
## Sistema CI

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
## Inciar microservicio

Aunque solo muestra un ```Hello World``` para iniciar el microservicio lo único (en caso de que esten instaladas las dependencias) que hay que hacer es:
 ```console
foo@bar:~$ python microservicio/main.py

 ``` 
 Tambien podemos usar ```make init```,  de esta forma primero instalara las dependencias y luego iniciara el microservicio