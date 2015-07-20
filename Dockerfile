FROM php:5.6-apache

# Add PHP timezone configuration
ADD timezone.ini /usr/local/etc/php/conf.d/

# Install git and sqlite3
RUN apt-get update
RUN apt-get install -y git sqlite3

# Enable apache's rewrite module
RUN a2enmod rewrite

# Remove default apache page
RUN rm /var/www/html/index.html

# Clone the lodspeakr repository
RUN git clone https://github.com/alangrafu/lodspeakr.git /var/www/html/lodspeakr

WORKDIR /var/www/html/lodspeakr/

# Run the install script
RUN ./install.sh base-url=/ base-namespace=http://resourceprojects.org/ sparql-endpoint=http://virtuoso:8890/sparql
# Create some directories and make them writeable by apache
RUN chown -R www-data /var/www/html/lodspeakr/cache /var/www/html/lodspeakr/meta /var/www/html/lodspeakr/components

# Add some files/folders from this repository
RUN rm -r components settings.inc.php
ADD components /var/www/html/lodspeakr/components
ADD settings.inc.php /var/www/html/lodspeakr/settings.inc.php
ADD start.sh /var/www/html/lodspeakr/start.sh

# Change module priorities https://github.com/alangrafu/lodspeakr/wiki/Changing-priorities-of-modules
RUN utils/lodspk.sh enable module type 1

ADD htaccess-modified /var/www/html/lodspeakr/.htaccess
ADD htaccess-parent-modified /var/www/html/.htaccess

CMD ["./start.sh"]
