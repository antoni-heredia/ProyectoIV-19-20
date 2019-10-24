.PHONY: tests dependencias #Indica el target es ficticio, y que el make no debería crear el archivo.

dependenciasCircle: #Instala las dependencias
	pip install  --user -r requirements.txt

dependencias: #Instala las dependencias
	pip install   -r requirements.txt

init: dependencias #Inicia el microservicio
	python microservicio/main.py
initCircle: dependenciasCircle #Inicia el microservicio

tests: #Para relizar los test
	python -m pytest
