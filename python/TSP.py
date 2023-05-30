import numpy as np
import matplotlib.pyplot as plt

def tsp(points):
    num_points = len(points)
    best_route = None
    min_distance = float('inf')

    # 初期経路を生成
    initial_route = np.random.permutation(num_points)

    # 2-opt法で経路を改善
    improved_route = improve_route(points, initial_route)

    # 最短距離を計算
    distance = calculate_distance(points, improved_route)

    # 最良の経路と最短距離を更新
    if distance < min_distance:
        min_distance = distance
        best_route = improved_route

    return best_route, min_distance

def improve_route(points, route):
    num_points = len(points)
    improved = True

    while improved:
        improved = False
        for i in range(1, num_points - 2):
            for j in range(i + 1, num_points):
                if j - i == 1:
                    continue
                new_route = route.copy()
                new_route[i:j] = route[j - 1:i - 1:-1]
                new_distance = calculate_distance(points, new_route)
                if new_distance < calculate_distance(points, route):
                    route = new_route
                    improved = True

    return route

def calculate_distance(points, route):
    distance = 0
    for i in range(len(route) - 1):
        point1 = points[route[i]]
        point2 = points[route[i + 1]]
        distance += np.linalg.norm(point2 - point1)
    return distance

# ランダムに100点を生成
np.random.seed(0)
points = np.random.rand(100, 2)

# TSPを解く
best_route, min_distance = tsp(points)

# 最適な経路を表示
plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], color='blue')
for i in range(len(best_route) - 1):
    point1 = points[best_route[i]]
    point2 = points[best_route[i + 1]]
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='red')
plt.plot([points[best_route[-1]][0], points[best_route[0]][0]], [points[best_route[-1]][1], points[best_route[0]][1]], color='red')
plt.show()

print('Best Route:', best_route)
print('Min Distance:', min_distance)
