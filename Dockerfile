# Container image that runs your code
FROM python:3

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY src/main.py /main.py
COPY shop-extensions.json /shop-extensions.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
