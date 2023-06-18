#!/bin/bash
# This is a line of text
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
