# Container image that runs your code
FROM alpine:3.10

RUN sudo apt-get update
RUN sudo apt-get install python3.7
# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY src/main.py /main.py
COPY shop-extensions.json /shop-extensions.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
