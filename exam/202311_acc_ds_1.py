from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
from scipy import stats


def main(lines):
    csv_path = parse_args(lines)
    df = pd.read_csv(csv_path)
    df.columns = ["time", "option", "click", "result"]
    no_change_result = df[df["option"] == 0]["result"]
    no_change_result_strong = no_change_result * 1.1
    change_result = df[df["option"] == 1]["result"]

    # welch t test で有意差があるかどうかを判定する
    # 広告を変更することで、resultが5%水準で有意に1,1倍よりも大きくなるかどうかを判定する
    test_result = stats.ttest_ind(change_result, no_change_result_strong, equal_var=False, alternative="greater")
    print(int(test_result.pvalue < 0.05))


def parse_args(lines) -> Path:
    csv_path = Path(lines[0])
    return csv_path


if __name__ == "__main__":
    main(sys.argv[1:])
