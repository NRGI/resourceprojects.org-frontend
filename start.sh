#!/bin/bash
# If we need to we can do substitutions from environment variables
# in the config file
/bin/sed -i "s|BASE_URL|${BASE_URL}|" settings.inc.php
apache2-foreground
