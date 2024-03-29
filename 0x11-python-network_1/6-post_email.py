#!/usr/bin/python3
"""Script that takes a URL and an email, sends a POST request, and
displays response body"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
