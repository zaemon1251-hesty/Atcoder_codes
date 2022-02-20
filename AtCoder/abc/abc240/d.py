def main():
    N = int(input())
    A = list(map(int, input().split()))
    st = []
    nums = []
    ans = []
    for i in range(N):
        if st and st[-1] == A[i]:
            if nums[-1]+1 == A[i]:
                for _ in range(nums[-1]):
                    st.pop()
                nums.pop()
            else:
                st.append(A[i])
                nums[-1] += 1
        else:
            st.append(A[i])
            nums.append(1)
        ans.append(len(st))
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
