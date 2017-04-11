# Tweet Sentiment Labeller

Search for Tweets and download the data labeled with it's Polarity 


## Development Guide

1. apache install: sudo apt-get install apache2
   python install: sudo apt-get install python
or
   python3 install: sudo apt-get install python3

2.sudo a2enmod cgi

3. /etc/apache2/sites-available/000-default.conf
This is described well in the apache2 doc above, but essentially you to make all files in a cgi folder be executed, you would use this conf:

<Directory /srv/www/yoursite/public_html/cgi-bin>
        Options ExecCGI
        SetHandler cgi-script
    </Directory>

and to allow .py files to be executed as scripts in a particular folder you would use this conf:

    <Directory /srv/www/yoursite/public_html>
        Options +ExecCGI
        AddHandler cgi-script .py
    </Directory>

4.
You can change the first line in python program from

#!/usr/bin/env python

to

#!/path/to/your/python/binary

such as

#!/usr/bin/python3

5. Install requirements "pip install -r requirements.txt"

## [License @Milic Vukojicic]
