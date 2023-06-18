#!/bin/bash
# This is a line of text
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
