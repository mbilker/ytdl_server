#!/bin/bash

cd "$(dirname "$0")"

exec docker build -t ytdl_server:latest -f Dockerfile .
