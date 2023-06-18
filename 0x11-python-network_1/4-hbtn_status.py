#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    import requests
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(r.text.__class__))
    print("\t- content: {}".format(r.text))
