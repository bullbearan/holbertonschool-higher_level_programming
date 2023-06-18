#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    data = parse.urlencode({'email': argv[2]}).encode()
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))
