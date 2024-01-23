# Virus Total API Application
This repository is non-commercial and not distributed in any use-cases. The purpose of this application is to build a web application and use the free API provided by https://docs.virustotal.com/reference/overview to detect malware in files. 

## Software Development Architecture
- The backend is design and built with FastAPI to create quick HTTP REST endpoints that connects between the database and the web application.
- The web application is build with Next.JS framework
- And using MongoDB as a way to store the meta-data acquired from the file report

## Running the application
Create your own .env file at the root directory where the `docker-compose.yml` file is with the necessary key and values:
1) API_KEY can be obtained by signing up an account here: https://www.virustotal.com/#/join-us
2) URI refers to the connection string that ATLAS povides
3) MONGO_DB - the name of the database
4) DOMAIN - the host running this application
```
API_KEY = ${API_KEY}
URI = ${URI}
MONGO_DB = ${DB}
DOMAIN = #{DOMAIN}
```

At the root directory run:
```
docker compose up -d --build
```
