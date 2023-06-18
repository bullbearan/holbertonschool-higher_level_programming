#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    from urllib import request, parse, error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
