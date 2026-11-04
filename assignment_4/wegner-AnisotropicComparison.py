import pandas as pd
from sklearn import cluster
from sklearn import metrics
id = 200514620
df = pd.read_csv('anisotropic.csv')
true_labels = df.iloc[:, 0]

kmeans_1 = cluster.KMeans(n_clusters = 3, random_state = id)
kmeans_2 = cluster.KMeans(n_clusters = 4, random_state = id)
kmeans_3 = cluster.KMeans(n_clusters = 5, random_state = id)
km_labs1 = kmeans_1.fit_predict(df.iloc[:, 1:]).copy()
km_labs2 = kmeans_2.fit_predict(df.iloc[:, 1:]).copy()
km_labs3 = kmeans_3.fit_predict(df.iloc[:, 1:]).copy()
kmeans_1_ARI = metrics.adjusted_rand_score(true_labels, km_labs1)
kmeans_2_ARI = metrics.adjusted_rand_score(true_labels, km_labs2)
kmeans_3_ARI = metrics.adjusted_rand_score(true_labels, km_labs3)

agglo_1 = cluster.AgglomerativeClustering(n_clusters = 3)
agglo_2 = cluster.AgglomerativeClustering(n_clusters = 4)
agglo_3 = cluster.AgglomerativeClustering(n_clusters = 5)
agglo_labs1 = agglo_1.fit_predict(df.iloc[:, 1:]).copy()
agglo_labs2 = agglo_2.fit_predict(df.iloc[:, 1:]).copy()
agglo_labs3 = agglo_3.fit_predict(df.iloc[:, 1:]).copy()
agglo_1_ARI = metrics.adjusted_rand_score(true_labels, agglo_labs1)
agglo_2_ARI = metrics.adjusted_rand_score(true_labels, agglo_labs2)
agglo_3_ARI = metrics.adjusted_rand_score(true_labels, agglo_labs3)

db_1 = cluster.DBSCAN(eps = 0.1)
db_2 = cluster.DBSCAN(eps = 0.05)
db_3 = cluster.DBSCAN(eps = 0.01)
db_labs1 = db_1.fit_predict(df.iloc[:, 1:]).copy()
db_labs2 = db_2.fit_predict(df.iloc[:, 1:]).copy()
db_labs3 = db_3.fit_predict(df.iloc[:, 1:]).copy()
db_1_ARI = metrics.adjusted_rand_score(true_labels, db_labs1)
db_2_ARI = metrics.adjusted_rand_score(true_labels, db_labs2)
db_3_ARI = metrics.adjusted_rand_score(true_labels, db_labs3)

data = {
    'Model': [
        'KMeans (n_clusters = 3)',
        'KMeans (n_clusters = 4)',
        'KMeans (n_clusters = 5)',
        'Agglomerative (n_clusters = 3)',
        'Agglomerative (n_clusters = 4)',
        'Agglomerative (n_clusters = 5)',
        'DBSCAN (eps = 0.1)',
        'DBSCAN (eps = 0.05)',
        'DBSCAN (eps = 0.01)'
    ],
    'ARI': [
        kmeans_1_ARI, kmeans_2_ARI, kmeans_3_ARI,
        agglo_1_ARI, agglo_2_ARI, agglo_3_ARI,
        db_1_ARI, db_2_ARI, db_3_ARI
    ]
}
data = pd.DataFrame(data)
data = data.sort_values(by = 'ARI', ascending = False)

with open('Wegner-anisotropic-model-ranking.txt', 'w') as file:
    file.write(f'{'=' * 17} Model Rankings {'=' * 17}\n\n')
    
    for _, row in data.iterrows():
        file.write(f'{row['Model']} ARI Score: {row['ARI']}\n')