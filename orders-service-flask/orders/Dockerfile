FROM python:3.7.2-alpine
MAINTAINER Grzegorz Galios "grzegorz.galios@wp.pl"

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# Set the working directory to /app
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Run app.py when the container launches
CMD python manage.py run -h 0.0.0.0
