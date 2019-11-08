# Love-my-movies
## Correrlo con docker
El proyecto está dockerizado en un repositorio de dockerhub que se puede encontrar en el siguiente link. 

    https://hub.docker.com/repository/docker/davidcorzo/love_my_movies


## Tomar en cuenta que para que la parte de redis funcione hay que corer:
Tenido redis instalado en una computadora de preferencia distribución linux como OS correr en la terminal:
    
    $ redis-server 


## Tomar en cuenta que se corre con el docker compose.
En la carpeta en cuestión escribir:
    
    $ docker-compose up

## La parte de HTML contiene:
El contenido del HTML contiene lo central del HTML así mismo como unas funciones de JS y contenido CSS, pero hay funciones que se encuentran en script.js así mismo como styles.css.

## Para correr mi app con python:
    $ python3 main.py

## CI
Actions/Beta CI: Esta activado en GitHub como acciones beta, se encuentra en un .yml.

## La imagen de docker compiló y se puede correr, pero con el docker compose.
Si se corre la imagen sin el docker compose no se activirán partes vitales y necesarias que no se activan con el simple comando de docker run.

## Todo está modulizado en modulize.py e importado en main.py
Ver archivos modulize.py & main.py

## requirements.txt
Está en este archivo todas las dependencias, pero de esto no hay que preocuparse por que lo incluye la imagen de docker.

## Maintainer: 
David Corzo at 
davidcorzo@ufm.edu