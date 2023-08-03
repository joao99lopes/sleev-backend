## **RUN ENVIRONMENT**
### **DEV MODE**

 - `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build`
### **PROD MODE**

 - `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build`

## **CONNECT TO RUNNING FLASK DOCKER CONTAINER**
 - `docker exec -it flask-on-docker_web_1 /bin/bash`

## **CONNECT TO RUNNING DB DOCKER CONTAINER**
 - `docker-compose exec db psql --username=postgres --dbname=sleev_db_dev`



## **VIRTUAL ENVIRONMENT**
### **!!! NOT NEEDED FOR THIS PROJECT !!!**

To create a virtual environment :

1. Navigate to "web" directory
2. `python3.11 -m venv env`

To activate the virtual environment :

1. Navigate to "web" directory
2. `source env/bin/activate`
