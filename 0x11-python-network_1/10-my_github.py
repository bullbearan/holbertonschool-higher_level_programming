#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    import requests
    from sys import argv
    cred = (argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=cred)
    try:
        dct = r.json()
        print(dct.get("id"))
    except Exception:
        print("None")
