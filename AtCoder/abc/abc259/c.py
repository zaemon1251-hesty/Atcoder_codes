def main():
    S = list(input())
    T = list(input())

    S_Counter = []
    S_Chars = []
    i = 0
    while i < len(S):
        if 0 < i < len(S) and S[i] == S[i - 1]:
            S_Counter[-1] += 1
        else:
            S_Counter.append(1)
            S_Chars.append(S[i])
        i += 1

    T_Counter = []
    T_Chars = []
    j = 0
    while j < len(T):
        if 0 < j < len(T) and T[j] == T[j - 1]:
            T_Counter[-1] += 1
        else:
            T_Counter.append(1)
            T_Chars.append(T[j])
        j += 1

    if len(S_Counter) != len(T_Counter):
        print("No")
        exit()

    for sc, schr, tc, tchr in zip(S_Counter, S_Chars, T_Counter, T_Chars):
        if schr != tchr or sc > tc or (sc == 1 and tc != 1):
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
