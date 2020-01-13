# Configuración del contenedor con Docker
Para usar Docker para la creación de contenedores es esencial usar un fichero de configuración llamado [Dockerfile](../Dockerfile). 

A continuación mostraremos el contenido de nuestro fichero y la explicación de cada una de las lineas que lo compone para poder entenderlo mejor. 
La estructura del fichero es la siguiente:
```
LABEL maintainer="Antonio Jesús Heredia (a.heredia.castillo@gmail.com)"

EXPOSE $PORT

COPY requirements.txt /tmp
RUN cd /tmp && pip install -r requirements.txt
RUN apt-get update && apt-get install rabbitmq-server -y
COPY . /app

WORKDIR /app


CMD rabbitmq-server &  ( sleep 5 &&  python microservicio/recieve.py  ) & gunicorn -b 0.0.0.0:${PORT} app:app
```
La explicación de las todas las lineas es la siguiente:
1. La primera linea __LABEL__ se refiere a quien es el mantenedor del contenedor. 
2. __EXPOSE__ se usa para indicar que ese puerto sera accesible desde el exterior de la maquina. 
3. En la tercera linea, con __COPY__ copiamos a una carpeta temporal los requirements de Python.
4. En la cuarta linea, hacemos uso de __RUN__ para instalar esas dependencias. 
5. En la quinta linea instalamos rabbitmq
6. En la sexta linea copiamos todos los ficheros excepto los que se encuentran en el fichero [.dockerignore](../.dockerignore).
7. En la séptima linea indicamos cual sera el directorio de trabajo desde que se ejecutara la ultima orden. 
8. Por ulitmo ejecutamos todos los procesos necesarios del contenedor. ESta forma tan enrevesa se debe a que si no me era imposible ejecutar el servidor de rabbitmq. Ejecutamos en paralelo tres comandos. El primero es el servidor de rabbitmq, el tercero el servidor de gunicorn y el segundo ejecuta dos comandos a su vez una espera de 5 segundos, para dar tiempo mientras se inicia el servidor de rabbitmq y por ultimo ejecuta el consumidor de mensajes de nuestra aplicación. 