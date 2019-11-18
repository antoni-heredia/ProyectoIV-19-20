.PHONY: tests dependencias #Indica el target es ficticio, y que el make no debería crear el archivo.

dependenciasCircle: #Instala las dependencias
	pip install  --user -r requirements.txt

dependencias: #Instala las dependencias
	pip install   -r requirements.txt

init: dependencias #Inicia el microservicio
	python microservicio/main.py
initCircle: dependenciasCircle #Inicia el microservicio

tests: #Para relizar los test
	python -m pytest test/test_img.py   
	
start:
	pm2 start "gunicorn --bind 0.0.0.0:8080  app:app" --name microservicio
	pm2 start microservicio/recieve.py --name recieve

start-heroku:
	gunicorn --bind 0.0.0.0:$(PORT)  app:app
stop:
	pm2 stop microservicio
	pm2 stop recieve

delete:
	pm2 delete microservicio
	pm2 delete recieve

restart:
	pm2 restart microservicio
	pm2 restart recieve
