# Herramientas
La implementación de la API la desarrollare en [Python](https://www.python.org) usando [Flask](https://palletsprojects.com/p/flask/)+[Flask-restful](https://flask-restful.readthedocs.io/en/latest/).. Esta elección se debe a que quiero usar el mismo lenguaje para ofrecer la API como para realizar el procesamiento de la imagen. 

Para encontrar la ubicación de Wally usare [Keras](https://keras.io/) mas específicamente [Faster R-CNN](https://towardsdatascience.com/faster-r-cnn-object-detection-implemented-by-keras-for-custom-data-from-googles-open-images-125f62b9141a). __El entrenamiento de la red neuronal no es parte del microservicio__. Podriamos usar una funcionalidad que ya existiera o usar una entrenada por mi como quiero intentar en este caso. 

Para la gestión de entornos usare [Anaconda](https://www.anaconda.com/) y para los test usare [pytest](https://docs.pytest.org/en/latest/). Esta elección la he hecho ya que creo que son buenas (y fáciles) herramientas para la iniciación en  gestión de entornos y test. 



Para tener un registro de todo lo ocurrido en el sistema utilizare  [logging](https://docs.python.org/3/howto/logging.html). Utilizare como base de referencia [esta presentacion](https://static.sched.com/hosted_files/pycones19/48/El%20show%20de%20Truman.pdf) de [@Jimena_y_yo](https://twitter.com/jimena_y_yo) (Gracias a [JJ](github.com/JJ) por darnos la pista).


# Almacenamiento
Todas las imágenes recibidas, serán almacenadas. (al menos por un tiempo). Esta decisión ha sido debida a que para poder reentrenar  la red natural puedes sernos de utilizad imágenes dadas por los usuario y que no están en nuestro dataset inicial. Asi podemos tener cada vez un sistema mas preciso con son predicciones. Aunque repito, el entrenamiento del sistema no forma parte del microservicio. 

Para esto usaría [MongoDB](https://www.mongodb.com/es) mas específicamente la librería [PyMongo](https://api.mongodb.com/python/current/).
