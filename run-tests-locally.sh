#!/bin/bash
set -e
docker build -t opendataservices/resourceprojects.org-frontend .
docker rm -f virtuoso-test || true
docker rm -f frontend-test || true
docker run -d -p 127.0.0.1:8887:8890 --name virtuoso-test opendataservices/virtuoso:master
sleep 30s
for f in ./fts/fixtures/*.ttl; do
    curl -T $f "http://127.0.0.1:8887/sparql-graph-crud-auth?graph=http://test" --digest --user dba:dba
done
docker run -d --publish=127.0.0.87:80:80 --link virtuoso-test:virtuoso -e BASE_URL=http://127.0.0.87/ -e SPARQL_ENDPOINT=http://virtuoso:8890/sparql -e DEBUG --name frontend-test opendataservices/resourceprojects.org-frontend
SERVER_URL=http://127.0.0.87/ py.test fts
