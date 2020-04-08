FROM python:3

ADD . /app
WORKDIR /app
# add dependencies
# RUN pip install pystrich
ENV PYTHONPATH /app
CMD ["/app/src/main.py"]
