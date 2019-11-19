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
  - [Creditos](#creditos)


## Descripción
Este proyecto es para la asignatura de Infraestructura Virtual. Este proyecto consiste en enviar una imagen mediante un formulario web, procesarla buscando a Wally y devolver una imagen donde indique la ubicación del mismo.

Las herramientas que usamos en el proyecto se pueden ver [aqui](docs/herramientas.md).

## Dataset de datos a usar

Buscando por github he encontrado un repositorio con imágenes ya clasificadas de Wally. El repositorio tiene licencia [ODbL](https://es.wikipedia.org/wiki/Licencia_Abierta_de_Bases_de_Datos) y se encuentra en el siguiente [link](https://github.com/vc1492a/Hey-Waldo).


## Herramienta de construcción
La herramienta de construcción que usaremos es ```makefile```. Para ello he creado el siguiente fichero [Makefile](./Makefile), donde se encuentra toda la información. 

    buildtool: Makefile

Para instalar las dependencias basta con ejecutar:
```console
foo@bar:~$ make dependencias
```
Y para ejecutar los test debemos ejecutar:
```console
foo@bar:~$ make tests
```

Para iniciar/detener/reiniciar/eliminar el servicio tenemos varias opciones dentro del makefile. 
```console
foo@bar:~$ make <start|stop|restart|delete>
```

 ## API

 Para probar la API, una vez que esta iniciado el servicio con make start, podemos ir a [http://0.0.0.0:8080/doc/](http://0.0.0.0:8080/doc/). Ahi se encuentra una herramienta construida con [swagger.io](swagger.io) donde podemos probar las rutas que tengo actualmente en la API. 

 Para mas información sobre las distintas rutas de la API y los test realizados sobre la misma consultar el fichero [api.md](docs/api.md).

  ## Creditos
  El modelo usado para encontrar a Wally ya existia. Yo he realizado una pequeña adaptación para poder usarlo en mi microservicio. El proyecto original es [HereIsWally](https://github.com/tadejmagajna/HereIsWally/). 