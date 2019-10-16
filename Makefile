.PHONY: tests dependencias #Indica el target es ficticio, y que el make no debería crear el archivo.

dependencias: #Instala las dependencias
	pip install -r --user requirements.txt

init: dependencias #Inicia el microservicio

tests: #Para relizar los test
	pytest test/test_img.py
