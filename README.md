Pre-requisites
--------------

To run lodspeakr you will need an instance of virtuoso running.

```
docker run -p 127.0.0.1:8890:8890 --name=virtuoso caprenter/automated-build-virtuoso
```

Development
-----------

```
docker build -t lodspeakr .
docker run --publish=127.0.0.2:80:80 --name=lodspeakr-container --rm --link virtuoso:virtuoso -e BASE_URL=http://127.0.0.2/ lodspeakr
```

Then visit http://127.0.0.2/

If you wish to enable debug mode, also add `-e DEBUG=true` before `lodspeakr`. This turns on PHP debugging, and also allows you to see extra logs at http://127.0.0.2/logs

Running a docker build each time you change a file can be a bit too slow for development pursposes, so instead you can mount the components directory in the container from the host filesystem:

```
docker run --publish=127.0.0.2:80:80 --name=lodspeakr-container --rm --link virtuoso:virtuoso -e BASE_URL=http://127.0.0.2/  -v `pwd`/components:/var/www/html/lodspeakr/components lodspeakr
```

Uploading data into virtuoso
----------------------------

* Go to http://localhost:8890/conductor/
* Log in. Default uusername/password is dba/dba
* Click the linked data tab.

If you've previously uploaded resourceprojects data, delete the old data - go to Linked Data -> Graphs -> Graphs and hit the delete button on the resourceprojects.org row

To upload data go to Linked Data -> Quad Store Upload ( http://localhost:8890/conductor/rdf_import.vspx )

* Click the resource URL radio button.
* Put this in the resource URL text box: https://raw.githubusercontent.com/NRGI/resource-projects-etl/master/resource-projects.ttl
* Check the "Create graph explicitly" checkbox
* Put http://resourceprojects.org/ in the Named Graph IRI
* Hit the upload button

(If you've generated the data locally, you can use the "File" option instead).
