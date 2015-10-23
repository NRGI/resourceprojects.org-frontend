<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Natural Resource Governance Institute</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" type="text/css" href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.css" />
    <link href='//api.tiles.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v0.0.2/leaflet.fullscreen.css' rel='stylesheet' />
    <link href="/css/nrgi.css" rel="stylesheet" type="text/css" media="screen" />
    <script src="http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.js"></script>
    <script src='//api.tiles.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v0.0.2/Leaflet.fullscreen.min.js'></script>
    <link rel="alternate" type="application/rdf+xml" title="RDF/XML Version" href="{{lodspk.local.value}}.rdf" />
    <link rel="alternate" type="text/turtle" title="Turtle Version" href="{{lodspk.local.value}}.ttl" />
    <link rel="alternate" type="text/plain" title="N-Triples Version" href="{{lodspk.local.value}}.nt" />
    <link rel="alternate" type="application/json" title="RDFJSON Version" href="{{lodspk.local.value}}.json" />
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
      .wait{
        background-image:url('/img/wait.gif');
        background-repeat:no-repeat;
        padding-right:20px;
        background-position: right;
      }
    </style>
  </head>
  <body>

  <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <div class="banner">This is a <a href="/about.html">prototype site</a>: site links and contents are subject to change.</div>
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <!--<a class="brand" href="/">{{lodspk.title}}</a>-->
          <a class="brand" href="/"><img src="/img/print-logo.jpg" width="185" height="65" alt="Natural Resource Governance Institute Logo"/></a>
          <div class="nav-collapse">
            <ul class="nav list-inline">
              <!--<li><a href="/">Home</a></li>-->
              <li><a href="/about.html">About</a></li>
              <li><a href="/project">Projects</a></li>
              <li><a href="/country">Countries</a></li>
              <li><a href="/company">Companies</a></li>
              <li><a href="/commodity">Commodities</a></li>
              <li><a href="/source">Sources</a></li>
              <li><a href="/glossary.html">Glossary</a></li>
            </ul>
            <form class="navbar-search pull-left" action="">
              <input type="text" data-provide="typeahead" class="typeahead search-query span2" placeholder="Search"/>
            </form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

