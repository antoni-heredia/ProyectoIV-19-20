.PHONY: tests dependencias #Indica el target es ficticio, y que el make no debería crear el archivo.

dependenciasCircle: #Instala las dependencias
	pip install  --user -r requirements.txt

dependencias: #Instala las dependencias
	pip install   -r requirements.txt

init: dependencias #Inicia el microservicio
	python microservicio/main.py

pm2:
	sudo apt update
	sudo apt install -y nodejs
	sudo apt install -y npm
	sudo npm install -g pm2

initCircle: dependenciasCircle #Inicia el microservicio

tests:  #Para relizar los test
	python -m pytest test/*
	
start: 
	pm2 start "gunicorn --bind 0.0.0.0:8080  app:app" --name microservicio
	pm2 start microservicio/recieve.py --name recieve

start-sin-pm2:
	gunicorn --bind 0.0.0.0:8080  app:app & python microservicio/recieve.py &

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

contruir-taper:
	sudo docker build -t anthercas/wallyfinder .

iniciar-taper: contruir-taper
	export HOST_PORT=5050
	export PORT=5050
	sudo docker run -e PORT=$PORT -p $HOST_PORT:$PORT anthercas/wallyfinder