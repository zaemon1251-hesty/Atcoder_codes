from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


def main():
    @lru_cache(maxsize=None)
    def s(k):
        if k == 1:
            return "1"
        return f"{s(k - 1)} {str(k)} {s(k - 1)}"
    print(s(int(input())))


if __name__ == '__main__':
    main()
