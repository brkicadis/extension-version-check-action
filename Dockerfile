# Container image that runs your code
FROM python:3

RUN pip install lastversion
RUN pip install gitpython

ENTRYPOINT ["/bin/bash", "-c", "find . -name shop-extensions.json"]
# Copies your code file from your action repository to the filesystem path `/` of the container
COPY src/main.py /usr/bin/main.py
#COPY shop-extensions.json /github/workspace/shop-extensions.json
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
