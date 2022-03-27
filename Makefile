#NAME ?= jal7434
all: build run push images ps

images: 
	docker images | grep jal7434
ps: 
	docker ps -a | grep jal7434
build:
	docker build -t jal7434 -t jal7434/app.py:midterm .
run:
	docker run -d -p 5017:5000 jal7434/app.py:midterm

push:
	docker push jal7434/app.py:midterm
