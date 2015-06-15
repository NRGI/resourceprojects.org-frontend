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

If you wish to enable debug mode, also add `-e DEBUG=true` before `lodspeakr`.

Running a docker build each time you change a file can be a bit too slow for development pursposes, so instead you can mount the components directory in the container from the host filesystem:

```
docker run --publish=127.0.0.2:80:80 --name=lodspeakr-container --rm --link virtuoso:virtuoso -e BASE_URL=http://127.0.0.2/  -v `pwd`/components:/var/www/html/lodspeakr/components lodspeakr
```
