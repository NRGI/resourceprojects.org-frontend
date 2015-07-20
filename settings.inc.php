<?php

$offset = 0;
if(!empty($_GET['offset'])) {
    $offset = (int) $_GET['offset'];
    if ($offset < 0) {
      $offset = 0;
    }
}
$lodspk['offset'] = $offset;

$limit = 50;
if(!empty($_GET['limit'])) {
    $limit = (int) $_GET['limit'];
}
$lodspk['limit'] = $limit;

$lodspk['next'] = $offset + $limit;
$lodspk['prev'] = $offset - $limit;

if ($lodspk['prev'] <= 0) {
      $lodspk['prev'] = 0;
    }

$conf['endpoint']['local'] = 'http://virtuoso:8890/sparql';
$conf['home'] = '/var/www/html/lodspeakr/';
$conf['basedir'] = 'BASE_URL';
$conf['debug'] = false;

$conf['ns']['local']   = 'http://resourceprojects.org/';
$conf['ns']['base']   = 'BASE_URL';

$conf['mirror_external_uris'] = $conf['ns']['local'];

// Cherry-picked components (see https://github.com/alangrafu/lodspeakr/wiki/Reuse-cherry-picked-components-from-other-repositories)

// Variables in  can be used to store user info.
// For examples, 'title' will be used in the header.
// (You can forget about all conventions and use your own as well)
$lodspk['title'] = 'LODSPeaKr';

$conf['modules']['available'] = array('static','type','service');

$conf['root'] = 'data/';
