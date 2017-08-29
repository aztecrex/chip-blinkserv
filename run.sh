#!/usr/bin/env bash


source /home/chip/.virtualenv/p3/bin/activate

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=blinkserv.py

flask run --host 0.0.0.0 --port 80

