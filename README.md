# Buscador de Wally
## Descripción
Este proyecto es para la asignatura de Infraestructura Virtual. Este proyecto consiste en enviar una imagen mediante un formulario web, procesarla buscando a Wally y devolver una imagen donde indique la ubicación del mismo. 
## Implementación
La implementación de la API la desarrollare en [Python](https://www.python.org) usando [Django](www.djangoproject.com) + [REST Framework](https://www.django-rest-framework.org/). Esta elección se debe a que quiero usar el mismo lenguaje para ofrecer la API como para realizar el procesamiento de la imagen. Para encontrar la ubicación de Wally usare [Keras](https://keras.io/) mas específicamente [Faster R-CNN](https://towardsdatascience.com/faster-r-cnn-object-detection-implemented-by-keras-for-custom-data-from-googles-open-images-125f62b9141a).

## Ampliación opcional

Como posible ampliación para el sistema he pensado en almacenar la imagen que nos han enviado y la ubicación posible detectada. Para que los encargados ( en este caso yo)  puedan revisar si esta encontrado de manera adecuada a Wally. En caso de añadir esta funcionalidad usaría [MongoDB](https://www.mongodb.com/es) mas específicamente la librería [PyMongo](https://api.mongodb.com/python/current/).