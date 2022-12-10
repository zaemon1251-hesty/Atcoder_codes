def main():
    L = int(input())
    fact = [1, 1]

    for i in range(2, L+1):
        fact.append(fact[-1]*i)
    print(fact[L-1]//fact[11]//fact[L-12])


if __name__ == '__main__':
    main()
