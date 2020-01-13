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
  - [API](#api)
  - [Despliegue en PaaS](#despliegue-en-paas)
  - [Taperización con docker](#taperizaci%c3%b3n-con-docker)
  - [DockerHub](#dockerhub)
  - [Creditos](#creditos)


## Descripción
Este proyecto es para la asignatura de Infraestructura Virtual. Este proyecto consiste en enviar una imagen mediante un formulario web, procesarla buscando a Wally y devolver una imagen donde indique la ubicación del mismo.

Las herramientas que usamos en el proyecto se pueden ver [aqui](docs/herramientas.md).

## Dataset de datos a usar

Buscando por github he encontrado un repositorio con imágenes ya clasificadas de Wally. El repositorio tiene licencia [ODbL](https://es.wikipedia.org/wiki/Licencia_Abierta_de_Bases_de_Datos) y se encuentra en el siguiente [link](https://github.com/vc1492a/Hey-Waldo).


## Herramienta de construcción
La herramienta de construcción que usaremos es ```makefile```. Para ello he creado el siguiente fichero [Makefile](./Makefile), donde se encuentra toda la información. 

    buildtool: Makefile
Podemos ver mas información sobre las herramientas de construción [aqui](docs/construcion.md)
## API

 Para mas información sobre las distintas rutas de la API y los test realizados sobre la misma consultar el fichero [api.md](docs/api.md).

## Despliegue en PaaS
Para el despliegue en un [PaaS](https://azure.microsoft.com/es-es/overview/what-is-paas/) he elegido en primera instancia [Heroku](https://dashboard.heroku.com/). La explicación de como como configurar Heroku se encuentra [aqui](docs/paas.md). La elección de Heroku es por la simplicidad y ademas es gratuito. Mas adelante tengo pensado desplegar en Oracle o Azure, para usar plataformas con mas potencia, ya que en Heroku, con la capa gratuita no puedo correr la aplicación original y tengo un mockup que simplemente pinta un circulo en el centro de la imagen a pesar de que es ya funcional. 

    Despliegue: https://wallyfinder.herokuapp.com

## Taperización con docker

El proceso de la creación del [Dockerfile](Dockerfile) viene explicada en este [documento](docs/taperización.md). 

El despliegue usando varios PaaS viene explicada [aqui](docs/despliegue_taper.md). 

El despliegue en PaaS con Docker esta realizado en la siguiente [dirección]():

	Contenedor: https://hub.docker.com/r/anthercas/wallyfinder

El despliegue en Heroku usando Docker lo encontramos [aqui](https://wallyfinder.herokuapp.com/status).

Ademas he añadido la automatización de la creación y inicio del contenedor.
Para hacer el build basta con ejecutar:
```console
foo@bar:~$ make contruir-taper
```

Y para lanzar el servidor desde el contenedor ejecutamos
```console
foo@bar:~$ make iniciar-taper
```
que a su vez también ejecutara contruir-taper como dependencia. 
## DockerHub
La dirección de DockerHub donde se encuentra el contenedor es la siguiente:

    URL: https://hub.docker.com/r/anthercas/wallyfinder

Los pasos para descargar y ejecutar el contenedor en local son: 

```console
foo@bar:~$ docker pull anthercas/wallyfinder:latest

foo@bar:~$ docker run -e PORT=$PORT -p $HOST_PORT:$PORT wallyfinder .
```
## Creditos
El modelo usado para encontrar a Wally ya existia. Yo he realizado una pequeña adaptación para poder usarlo en mi microservicio. El proyecto original es [HereIsWally](https://github.com/tadejmagajna/HereIsWally/). 