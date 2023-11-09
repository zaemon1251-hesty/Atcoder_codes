from fractions import Fraction
from itertools import permutations, product
from collections import deque


class FourDigitsToTen:
    """[summary]
    4桁の数字を入力して、10にできるかどうかを判定するプログラム
    4!(4つの数字の並び替え) * 3(3通りの演算順) * 4^3(４つの演算子を使う計算が3回ある)

    input:
    a1 a2 a3 a4
    (aiは0~9)

    output:
    Yes or No
    """

    def __init__(self) -> None:
        self.operators = ["+", "-", "*", "/"]

    def operate(self, x, y) -> list:
        result = []
        for op in self.operators:
            try:
                result.append(Fraction(eval("%s%s%s" % (x, op, y))))
            except ZeroDivisionError:
                continue
        return result

    def operate_all(self, x, y) -> list:
        if type(x) != list:
            x = [x]
        if type(y) != list:
            y = [y]
        result = []
        for i in x:
            for j in y:
                result.extend(self.operate(i, j))
        return result

    def isTenizable(self, A) -> bool:
        for i, j, k in permutations(range(3), 3):
            x = self.operate_all(A[i], A[i + 1])
            y = self.operate_all(A[2], A[3])
            if any(i == Fraction(10) for i in self.operate_all(x, y)):
                return True
        x = self.operate_all(A[1], A[2])
        y = self.operate_all(A[0], x)
        if any(i == Fraction(10) for i in self.operate_all(A[3], y)):
            return True
        x = self.operate_all(A[1], A[2])
        y = self.operate_all(A[3], x)
        if any(i == Fraction(10) for i in self.operate_all(A[0], y)):
            return True
        return False

    def main(self) -> None:
        inputArr = list(map(int, input().split()))
        permutes = permutations(inputArr, 4)
        for arr in permutes:
            if self.isTenizable(arr):
                print("Yes")
                return
        else:
            print("No")
            return


if __name__ == "__main__":
    # four2ten = FourDigitsToTen()
    # four2ten.main()

    inputArr = list(map(str, input().split()))
    for nums in permutations(inputArr, 4):
        for ops in product(["+", "-", "*", "/"], repeat=3):
            for order in permutations(range(3), 3):
                arr = list(nums)
                stack = deque([])
                fst = order.index(0)
                snd = order.index(1)
                trd = order.index(2)
                stack.extend([arr[fst], arr[fst + 1], ops[fst]])
                arr.pop(fst + 1)
                arr.pop(fst)
                if abs(snd - fst) > 1:
                    stack.extend([*arr, ops[snd], ops[trd]])
                else:
                    sndNum = int(snd > trd)
                    trdNum = 1 - sndNum
                    stack.extend([arr[sndNum], ops[snd], arr[trdNum], ops[trd]])
                buff = deque([])
                while stack:
                    s = stack.popleft()
                    if s in ["+", "-", "*", "/"]:
                        a = buff.pop()
                        b = buff.pop()
                        buff.append(f"({a}{s}{b})")
                    else:
                        buff.append(s)
                query = buff[-1]
                try:
                    if Fraction(eval(query)) == Fraction(10):
                        print("Found!!: %s" % query)
                        exit()
                except ZeroDivisionError:
                    pass
    print("Not Found")
