FROM google/python

ADD . /app
WORKDIR /app

RUN virtualenv /env
RUN /env/bin/pip install -r /app/requirements.txt
