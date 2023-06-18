#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.post(argv[1], {'email': argv[2]})
    print(r.text)
