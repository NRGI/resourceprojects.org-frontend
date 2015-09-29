FROM php:5.6-apache

# Add PHP timezone configuration
ADD timezone.ini /usr/local/etc/php/conf.d/

# Install git and sqlite3
RUN apt-get update
RUN apt-get install -y git sqlite3

# Enable apache's rewrite module
RUN a2enmod rewrite

# Remove default apache page
RUN rm index.html

# Clone the lodspeakr repository
RUN git clone https://github.com/alangrafu/lodspeakr.git lodspeakr

WORKDIR lodspeakr

# Run the install script
RUN ./install.sh base-url=/ base-namespace=http://resourceprojects.org/ sparql-endpoint=http://virtuoso:8890/sparql
# Create some directories and make them writeable by apache
RUN chown -R www-data cache meta components

# Add some files/folders from this repository
RUN rm -r components settings.inc.php
ADD components components
ADD settings.inc.php settings.inc.php
ADD start.sh start.sh

# Change module priorities https://github.com/alangrafu/lodspeakr/wiki/Changing-priorities-of-modules
RUN utils/lodspk.sh enable module type 1

ADD htaccess-modified .htaccess
ADD htaccess-parent-modified ../.htaccess

CMD ["./start.sh"]
