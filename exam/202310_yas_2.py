import math
from sklearn.cluster import DBSCAN
import numpy as np


def calculate_coordinates(theta, r):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y


def find_pillars(data):
    coordinates = []

    for theta, r in data:
        if r < 30:
            x, y = calculate_coordinates(theta, r)
            coordinates.append([x, y])

    coordinates = np.array(coordinates)

    # DBSCAN クラスタリングを利用して柱の位置を推定
    db = DBSCAN(eps=0.4, min_samples=3).fit(coordinates)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    pillars = []
    unique_labels = set(labels)
    for k in unique_labels:
        if k == -1:  # ノイズを除外
            continue
        class_member_mask = labels == k
        x = coordinates[class_member_mask & core_samples_mask][:, 0].mean()
        y = coordinates[class_member_mask & core_samples_mask][:, 1].mean()
        pillars.append((x, y))

    # 後処理
    # 柱の中心は、r(柱の表面から)から1m先にあると仮定
    for i, (x, y) in enumerate(pillars):
        r = math.sqrt(x**2 + y**2)
        x = x * (r + 1) / r
        y = y * (r + 1) / r
        pillars[i] = (x, y)

    return pillars


if __name__ == "__main__":
    m = int(input())
    data = [tuple(map(float, input().split())) for _ in range(m)]

    pillars = find_pillars(data)

    print(len(pillars))
    for x, y in pillars:
        print(x, y)
