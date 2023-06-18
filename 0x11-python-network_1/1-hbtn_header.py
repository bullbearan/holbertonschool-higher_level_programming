#!/usr/bin/python3
''' This is a moudle '''

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html['X-Request-Id'])
