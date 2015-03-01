FROM google/python

RUN apt-get install -y libpq-dev python-dev

ADD . /app
WORKDIR /app

RUN virtualenv --no-site-packages /env
RUN /env/bin/pip install -r /app/reqs/prod.txt
