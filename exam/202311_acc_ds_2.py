from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
from argparse import ArgumentParser
import numpy as np


def main(argv):
    args = parse_args(argv)
    if args.step == "step1":
        sum_of_sales = step1(str(args.csv_learn))
        print(sum_of_sales)
    elif args.step == "step2":
        out_df_string = step2(str(args.csv_learn))
        print(out_df_string)
    elif args.step == "step3":
        weights = list(map(float, args.weights.split(",")))
        step3(weights, str(args.csv_predict))
    else:
        raise ValueError(f"Invalid step: {args.step}")


def step1(csv: str) -> int:
    sales_df = pd.read_csv(csv)
    sum_of_sales = sales_df["sales"].sum()
    return sum_of_sales


def step2(csv: str) -> str:
    sales_df = pd.read_csv(csv, parse_dates=["time"])
    # 平均値で補完
    sales_df = sales_df.fillna(sales_df.mean())
    # timeの昇順にソート
    sales_df = sales_df.sort_values("time")
    # time   2010/07/10-00:44:27 文字列化
    sales_df["time"] = sales_df["time"].dt.strftime("%Y/%m/%d-%H:%M:%S")
    result = sales_df.to_csv(index=False)
    return result


def step3(weights: list[float], csv_predict: str) -> None:
    predict_df = pd.read_csv(csv_predict)
    assert list(predict_df.columns) == ["sales", "cloud", "rainfall", "temperature", "humidity"]

    predict_X = predict_df.to_numpy()
    predict_X = np.concatenate([predict_X, np.ones((predict_X.shape[0], 1))], axis=1)  # bias項を追加

    weights = np.array(weights)  # "sales", "cloud", "rainfall", "temperature", "humidity", "bias"

    predict_y = predict(weights, predict_X)

    # 改行しつつ、小数点以下6桁で丸める
    print("\n".join(map(lambda x: f"{x:.6f}", predict_y)))


def predict(weights: np.ndarray, X: np.ndarray) -> np.ndarray:
    assert len(weights.shape) == 1
    assert weights.shape[0] == X.shape[1]
    linear_comb = weights @ X.T  # (1, 6) @ (6, 5) = (1, 5)

    # logistic function
    return 1 / (1 + np.exp(-linear_comb))


def parse_args(argv) -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("step", type=str, choices=["step1", "step2", "step3"])
    parser.add_argument("--csv_learn", type=Path, required=False)
    parser.add_argument("--weights", type=str, required=False)
    parser.add_argument("--csv_predict", type=Path, required=False)

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
