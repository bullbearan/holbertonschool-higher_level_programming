#!/usr/bin/python3
''' This is a moudle '''

if __name__ == "__main__":
    import urllib.request
    link = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(link) as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(html.__class__))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))
