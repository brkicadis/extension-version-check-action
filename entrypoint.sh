#!/bin/sh -l

set -e

ls
python /usr/bin/main.py ${{ github.repository }}
