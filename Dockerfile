FROM python:3

COPY . /usr/local/bin
# add dependencies
# RUN pip install pystrich
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
