```
docker build -t lodspeakr .
docker run --publish=127.0.0.2:80:80 --name=lodspeakr-container --rm --link virtuoso:virtuoso lodspeakr
```

Then visit http://127.0.0.2/

Running a docker build each time you change a file can be a bit too slow for development pursposes, so instead you can mount the components directory in the container from the host filesystem:

```
docker run --publish=127.0.0.2:80:80 --name=lodspeakr-tcontainer --rm --link virtuoso:virtuoso -v `pwd`/components:/var/www/html/lodspeakr/components lodspeakr
```

