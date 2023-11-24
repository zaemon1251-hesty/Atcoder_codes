import sys
import pandas as pd
from pathlib import Path


def main(argv):
    csv_path = get_path_from_argv(argv)
    df = pd.read_csv(csv_path)
    df["thi"] = df.apply(lambda r: get_thi(r["Temperature"], r["Humidity"]), axis=1)
    cor = df["thi"].corr(df["Altitude"])
    print(cor)


def get_thi(t: float, h: float) -> float:
    return 0.81 * t + 0.01 * h * (0.99 * t - 14.3) + 46.3


def get_path_from_argv(argv) -> Path:
    # csvのファイルパスが引数として与えられる
    assert len(argv) == 1
    return Path(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
