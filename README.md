[![Build Status](https://travis-ci.org/antoni-heredia/WallysFinder.svg?branch=master)](https://travis-ci.org/antoni-heredia/WallysFinder)
[![CircleCI](https://circleci.com/gh/antoni-heredia/WallysFinder.svg?style=svg)](https://circleci.com/gh/antoni-heredia/WallysFinder)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# Buscador de Wally

## Índice de contenidos

- [Buscador de Wally](#buscador-de-wally)
  - [Índice de contenidos](#%c3%8dndice-de-contenidos)
  - [Descripción](#descripci%c3%b3n)
  - [Dataset de datos a usar](#dataset-de-datos-a-usar)
  - [Herramienta de construcción](#herramienta-de-construcci%c3%b3n)
  - [Sistema CI](#sistema-ci)
  - [Tests](#tests)
  - [Herramienta de construcción](#herramienta-de-construcci%c3%b3n-1)
  - [Creditos](#creditos)


## Descripción
Este proyecto es para la asignatura de Infraestructura Virtual. Este proyecto consiste en enviar una imagen mediante un formulario web, procesarla buscando a Wally y devolver una imagen donde indique la ubicación del mismo.

Las herramientas que usamos en el proyecto se pueden ver [aqui](docs/herramientas.md).

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
5. Comprobar si se pueden eliminar todas las imagenes de la base de datos. 
## Herramienta de construcción

    buildtool: Makefile


Aunque solo muestra un ```Hello World``` para iniciar el microservicio lo único (en caso de que esten instaladas las dependencias) que hay que hacer es:
 ```console
foo@bar:~$ python microservicio/main.py

 ``` 
 Tambien podemos usar ```make init```,  de esta forma primero instalara las dependencias y luego iniciara el microservicio

 La forma de ver si funciona el microservicio es accediendo desde el navegador a [localhost:5000](localhost:5000). Tambien he puesto el ejemplo de como iria implementando la descarga de una imagen, esto se puede probar desde [localhost:5000/download](localhost:5000/download).

 Para probar que se el microservicio recibe una imagen podemos hacer uso de 
 ```console
  foo@bar:~$ curl -F "name=nombre_de_la_imagen" -F "image=@ruta_de_la_imagen" 0.0.0.0:8080 
  ```

  ## Creditos
  El modelo usado para encontrar a Wally ya existia. Yo he realizado una pequeña adaptación para poder usarlo en mi microservicio. El proyecto original es [HereIsWally](https://github.com/tadejmagajna/HereIsWally/). 