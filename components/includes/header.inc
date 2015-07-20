<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Natural Resource Governance Institute</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" type="text/css" href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link href="{{lodspk.home}}css/nrgi.css" rel="stylesheet" type="text/css" media="screen" />
    <link rel="alternate" type="application/rdf+xml" title="RDF/XML Version" href="{{lodspk.local.value}}.rdf" />
    <link rel="alternate" type="text/turtle" title="Turtle Version" href="{{lodspk.local.value}}.ttl" />
    <link rel="alternate" type="text/plain" title="N-Triples Version" href="{{lodspk.local.value}}.nt" />
    <link rel="alternate" type="application/json" title="RDFJSON Version" href="{{lodspk.local.value}}.json" />
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
      .wait{
        background-image:url('{{lodspk.home}}img/wait.gif');
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
          <div class="banner">Some message here to let people know this site is still in production</div>
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <!--<a class="brand" href="{{lodspk.home}}">{{lodspk.title}}</a>-->
          <a class="brand" href="{{lodspk.home}}"><img src="{{lodspk.home}}img/NRGI_Logo_RGB_no_strapline.jpg" width="185" height="65" alt="Natural Resource Governance Institute Logo"/></a>
          <div class="nav-collapse">
            <ul class="nav list-inline">
              <!--<li><a href="{{lodspk.home}}">Home</a></li>-->
              <li><a href="{{lodspk.home}}project">Projects</a></li>
              <li><a href="{{lodspk.home}}country">Countries</a></li>
              <li><a href="{{lodspk.home}}company">Companies</a></li>
              <li><a href="{{lodspk.home}}license">Licenses</a></li>
            </ul>
            <form class="navbar-search pull-left" action="">
              <input type="text" data-provide="typeahead" class="typeahead search-query span2" placeholder="Search"/>
            </form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

