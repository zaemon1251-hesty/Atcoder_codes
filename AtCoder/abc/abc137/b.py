def main():
    K, X = map(int, input().split())
    minf = -1000000
    inf = -minf
    print(*range(max(minf, X-K+1), min(inf, X+K-1) + 1))

if __name__ == '__main__':
    main()