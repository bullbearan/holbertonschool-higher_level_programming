#!/bin/bash
# This is a line of text
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
