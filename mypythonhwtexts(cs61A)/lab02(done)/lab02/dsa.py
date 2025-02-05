import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.metrics import mean_squared_error
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

# 示例评分矩阵（用户数×电影数）
np.random.seed(42)  # 设置随机种子以保证结果可重复性

n_users = 50       # 用户数量
n_movies = 20      # 电影数量

# 创建一个示例评分矩阵，行是用户，列是电影，每个单元格是评分（1-5）
rating_matrix = np.random.randint(1, 6, size=(n_users, n_movies))

# 创建 Dataframe
rating_df = pd.DataFrame(rating_matrix)

# 步骤3：应用 SVD 进行降维
k = 5  # 可以调整这个值来改变降维的维度

svd = TruncatedSVD(n_components=k)
user_components = svd.fit_transform(rating_df)  # 用户在低维空间中的表示
movie_components = svd.components_             # 每个电影在低维空间中的权重

# 步骤4：训练并预测评分（假设部分评分缺失）
known_masking = np.random.choice([0,1], size=(n_users, n_movies), p=[0.75, 0.25])

masked_matrix = rating_matrix * known_masking

matrixcsr = csr_matrix(masked_matrix)

svd_model = TruncatedSVD(n_components=k)
svd_model.fit(matrixcsr)

# 预测评分矩阵
predicted_matrix = svd_model.transform(rating_df) @ svd_model.components_.T

# 步骤5：评估预测效果
known_ratings = rating_matrix[known_masking == 1]
predicted_ratings = predicted_matrix[known_masking == 1]

mse = mean_squared_error(known_ratings.flatten(), predicted_ratings.flatten())
print(f"Mean Squared Error: {mse}")

# 步骤6：推荐电影（基于每个用户的评分均值）
user_mean_ratings = known_ratings.mean(axis=1)

for user in range(n_users):
    sorted_movies = np.argsort(user_mean_ratings[user])[::-1]
    print(f"用户 {user} 最喜欢的电影是：", end='')
    for movie in sorted_movies[:5]:
        print(f"{movie+1}", end=' ')
    print()

# 步骤7：可視化低维表示
tsne = TSNE(n_components=2, random_state=42)
user_2d = tsne.fit_transform(user_components)

plt.figure(figsize=(10, 6))
plt.scatter(user_2d[:, 0], user_2d[:, 1])
plt.title('用户在 t-SNE 空间中的分布')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()