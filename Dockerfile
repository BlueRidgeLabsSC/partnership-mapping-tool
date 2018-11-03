#Grab the latest alpine image
FROM python:latest

# Install python and pip
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
# RUN adduser -D myuser
# RUN useradd -ms /bin/bash myuser
# USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD uwsgi --http :$PORT --gevent 1000 --http-websockets --master --wsgi-file app.py --callable app

