from fractions import Fraction
from itertools import permutations


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
        x = self.operate_all(A[0], A[1])
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
    four2ten = FourDigitsToTen()
    four2ten.main()
