# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution1(N):
    # Implement your solution here
    if N % 2 == 0:
        return "a" * (N - 1) + "b"
    else:
        return "a" * N


def solution2(S: str):
    # Implement your solution here
    S = S.lstrip("0")
    return S.count("1") * 2 + S.count("0") - 1


def solution3_(blocks):
    # Implement your solution here
    N = len(blocks)
    up_to = [0] * N
    cont = 0
    for i in range(N - 1):
        cont += 1
        if blocks[i] < blocks[i + 1]:
            up_to[i] = cont
            j = i
            i = i - cont
            while i < j:
                up_to[i] = cont
                i += 1
                cont -= 1
            cont = 0
    else:
        if cont > 0:
            up_to[i] = cont
            j = i
            i = i - cont
            while i < j:
                up_to[i] = cont
                i += 1
                cont -= 1

    blocks = blocks[::-1]
    down_to = [0] * N
    cont = 0
    for i in range(N - 1):
        cont += 1
        if blocks[i] < blocks[i + 1]:
            down_to[i] = cont
            j = i
            i = i - cont
            while i < j:
                down_to[i] = cont
                i += 1
                cont -= 1
            cont = 0
    else:
        if cont > 0:
            down_to[i] = cont
            j = i
            i = i - cont
            while i < j:
                down_to[i] = cont
                i += 1
                cont -= 1

    down_to = down_to[::-1]

    print(up_to)
    print(down_to)
    return max([up_to[i] + down_to[i] + 2 for i in range(N)])


def solution3(blocks):
    from bisect import bisect_left

    # Implement your solution here
    N = len(blocks)
    result = 0
    rights = [0] * N
    for i in range(N - 1):
        if blocks[i] < blocks[i + 1]:
            rights[i] = rights[i - 1] + 1
        else:
            rights[i] = rights[i - 1]
    lefts = [0] * N
    for i in range(N - 1, 0, -1):
        if blocks[i] < blocks[i - 1]:
            lefts[i] = lefts[i - 1] + 1
        else:
            lefts[i] = lefts[i - 1]
    for start_pos in range(N):
        right = bisect_left(rights, rights[start_pos])
        left = bisect_left(lefts, lefts[start_pos])
        result = max(result, left + right + 1)
    return result


if __name__ == "__main__":
    print(solution3([2, 6, 8, 5]))
    print(solution3([1, 5, 5, 2, 6]))
    print(solution3([1, 1]))
