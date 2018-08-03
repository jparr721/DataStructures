#!/bin/bash

docker stop $(cat process.txt) >/dev/null && docker rm $(cat process.txt) >/dev/null

docker run --name devpostgres -p 5432:5432 -e DOCKER_HOST=127.0.0.1 -e POSTGRES_PASSWORD=lotus -e POSTGRES_DB=devel_people -v /home/lotus/Work/devdb/db-data:/var/lib/postgresql/data -d postgres:9.6 > process.txt


