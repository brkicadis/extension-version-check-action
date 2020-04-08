#!/bin/sh -l

#echo "Hello $1"
#time=$(date)
#echo "::set-output name=time::$time"

pwd
ls
find . -name main.py
python main.py
