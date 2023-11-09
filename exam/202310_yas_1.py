from __future__ import annotations
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression


@dataclass
class Config:
    step: str
    csv_path: str
    pred_path: str | None = None


def compute_stats(column: pd.Series):
    mean_val = column.mean()
    var_val = column.var()  # 不偏分散
    min_val = column.min()
    max_val = column.max()
    return mean_val, var_val, min_val, max_val


def invoke(config: Config) -> None:
    sales_df = pd.read_csv(config.csv_path)
    if config.step == "step1":
        output_stats(sales_df)
    elif config.step == "step2":
        output_data_fillna(sales_df)
    elif config.step == "step3":
        submission_df = pd.read_csv(config.pred_path)
        output_prediction(sales_df, submission_df)
    else:
        raise Exception("stepが不正です")


def output_stats(sales_df: pd.DataFrame) -> None:
    print(*compute_stats(sales_df["sales"]), sep=",")
    print(*compute_stats(sales_df["temperature"]), sep=",")
    print(*compute_stats(sales_df["THI"]), sep=",")
    print(*compute_stats(sales_df["num_staff"]), sep=",")


def get_data_fillna(sales_df: pd.DataFrame) -> pd.DataFrame:
    sales_df["weather"] = sales_df["weather"].fillna(1)
    for col in ["sales", "temperature", "THI", "num_staff"]:
        sales_df[col] = sales_df[col].fillna(sales_df[col].mean())
        # min max scale
        if col != "sales":
            sales_df[col] = (sales_df[col] - sales_df[col].min()) / (sales_df[col].max() - sales_df[col].min())
    return sales_df


def output_data_fillna(sales_df: pd.DataFrame) -> None:
    print(get_data_fillna(sales_df).to_csv(header=False, index=False))


def output_prediction(train_df: pd.DataFrame, test_df: pd.DataFrame) -> None:
    train_df = get_data_fillna(train_df)
    # one-hot encoding weather
    train_df["weather"] = train_df["weather"].astype(int).astype(str)
    train_df = pd.get_dummies(train_df, columns=["weather"])
    train_df.drop(columns=["date"], inplace=True)

    test_df = get_data_fillna(test_df)
    # one-hot encoding weather
    test_df["weather"] = test_df["weather"].astype(int).astype(str)
    test_df = pd.get_dummies(test_df, columns=["weather"])
    test_df.drop(columns=["date"], inplace=True)

    # train
    train_X, train_y = train_df.drop(columns=["sales"]), train_df["sales"]
    reg = LinearRegression(fit_intercept=False).fit(train_X, train_y)

    # test
    test_X = test_df.drop(columns=["sales"])
    pred = reg.predict(test_X)
    print(*list(pred), sep="\n")


def get_config(args: list[str]):
    return Config(
        step=args[0],
        csv_path=args[1],
        pred_path=args[2] if len(args) > 2 else None,
    )


if __name__ == "__main__":
    config = get_config(sys.argv[1:])
    invoke(config)
