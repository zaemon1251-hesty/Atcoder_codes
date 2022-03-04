def main():
    N = int(input())
    ans = 0
    for num in range(1, N+1):
        if "7" in str(num):
            continue
        s = num
        t = True
        while s:
            if s%8==7:
                t = False
                break
            if s < 8:
                break
            s //= 8
        
        ans += 1 if t else 0
    print(ans)

if __name__ == '__main__':
    main()