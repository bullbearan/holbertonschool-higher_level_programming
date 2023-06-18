#!/bin/bash
# This is a line of text
curl -s -o /dev/null -w "%{http_code}" "$1"
