#!/bin/sh
unset GIT_DIR && cd /var/www/wikigit/ && git pull
python /root/scripts/jekyllgen.py /var/www/wikigit/ /var/www/wiki/_posts/
cd /var/www/wiki/ && jekyll build
