# NeilJob

The application runs on NGINX using uWSGI and Flask Application Factory. 

### Steps to redeploy:

1. ssh into the machine using `ssh root@197.242.150.230` and the password (which won't be stored here for security reasons).
1. Whilst in root folder, run the following commands sequentially:
    * `service nginx stop`
    * `fuser -k 80/tcp`
    * `fuser -k 8080/tcp`
    * `cd /var/www/`
    * `./iptables_flush.sh`
1. Check the contents of the `.bashrc` and make sure all environment vars used in the application are listed.
1. Run `source .bashrc` to reload all environment variables.
1. Next:
    * `cd NeilJob`
    * `git pull origin master`
1. At this point check that there are no conflicts with the current version after the `git pull`
1. Last couple of lines now to redeploy (you can do this all within the git repo folder i.e. NeilJob)
    * `service nginx start`
    * `nohup .venv/bin/uwsgi --socket 127.0.0.1:8080 --protocol=http -w WSGI:app &`
1. Now navigate to `http://anthropologylinux.dedicated.co.za/test` in a browser and see if the API is live.
1. In the terminal where the ssh session is running, type `exit` and hit return to quit the session without killing the application process that's running.