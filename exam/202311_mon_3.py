#!/usr/bin/env python3
import sys
from functools import lru_cache
import requests

API_URL = "https://challenge-server.code-check.io/"
ASK_ENDPOINT = API_URL + "api/recursive/ask"


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    SEED, N = parse_args(argv)

    def call_api(n):
        params = {
            "seed": SEED,
            "n": n,
        }
        # json response required
        response = requests.get(ASK_ENDPOINT, params=params)
        if response.status_code == 503:
            raise Exception("error! api server is busy")
        elif response.status_code != 400:
            raise Exception("error! bad parameters")
        elif response.status_code != 200:
            raise Exception("error! api server returned status code {}".format(response.status_code))
        return response.json()["result"]

    @lru_cache(maxsize=None)
    def f(n):
        if n == 0:
            return 1
        elif n == 2:
            return 2
        elif n % 2 == 0:
            return f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
        else:
            return call_api(n)

    print(f(N))
    exit(0)


def parse_args(argv):
    if len(argv) != 2 or not argv[1].isnumeric():
        print("error! invalid arguments")
        exit(1)
    SEED = argv[0]
    N = int(argv[1])
    return SEED, N


if __name__ == "__main__":
    main(sys.argv[1:])
