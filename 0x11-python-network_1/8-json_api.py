#!/usr/bin/python3
''' This is a moudle '''


if __name__ == "__main__":
    import requests
    from sys import argv
    q = None
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = ''
    r = requests.post("http://0.0.0.0:5000/search_user", q)
    try:
        dct = r.json()
        if dct:
            print("[{}] {}".format(dct.get("id"), dct.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
