"""
オンラインジャッジを利用するために利用したスクリプトです。

"${workspaceFolder}/AtCoder/(abc|arc)%3d.py"
に存在する
```
def main(a-f)(...):
    # solutions...
```
のコードから、
"${workspaceFolder}/AtCoder/(abc|arc)/(abc|arc)%3d/(a-f).py"
ファイルを作成します。
"""


import glob
import os
from typing import Dict, List

abc = {}
arc = {}
probs = ["a", "b", "c", "d", "e", "f"]
pwd = os.getcwd()


# read data
print("read start")

python_files = os.path.join(pwd, "AtCoder/*.py")
for path in glob.glob(python_files):
    f = open(path, "r")
    print(path, ": read")
    basename = os.path.basename(path).split(".")[0]
    newDir: Dict[str, List] = {prob: [] for prob in probs}
    readlines = f.readlines()
    line_num = len(readlines)
    i = 0
    while i < line_num and not readlines[i].startswith("def main"):
        i += 1
    # currnent_line includes "def maina()"
    for prob in probs:
        i += 1
        while i < line_num and not readlines[i].startswith("def main"):
            # インデントを消す
            if len(readlines[i]) > 4:
                newDir[prob].append(readlines[i][4:])
            i += 1
    f.close()
    if basename.startswith("abc"):
        abc[basename] = newDir
    elif basename.startswith("arc"):
        arc[basename] = newDir


# write data
print("write start")

print(abc.keys())

for c, contest in {"abc": abc, "arc": arc}.items():
    print(f"Got {c} contests:")
    print(*contest.keys(), sep="\n")
    print("\n")
    for contest_name, Dir in contest.items():
        contest_dir = os.path.join(pwd, "AtCoder", c, contest_name)
        os.makedirs(contest_dir, exist_ok=True)
        for prob, problines in Dir.items():
            prob_path = os.path.join(contest_dir, f"{prob}.py")
            if problines == []:
                print(f"{prob_path} : No data")
                continue
            elif os.path.exists(prob_path):
                print(f"{prob_path} : Already exists")
                continue
            with open(prob_path, "w") as f:
                f.writelines(problines)
            print(f"{prob_path} : Done")


print("Finished")
