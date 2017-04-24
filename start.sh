#!/bin/bash

cd Implementation/src/WebApp
gunicorn app:app --log-file=-
