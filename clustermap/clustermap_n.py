import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from scipy.cluster import hierarchy
import argparse
import scipy.spatial as sp
import numpy as np


def load_and_process_data(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df1 = df[0].str.split(';', expand=True)
    df = df.drop(0, axis=1)
    merged_df = pd.concat([df1, df], axis=1)
    processed_df = merged_df.set_index(merged_df[0]).T.reset_index(drop=True).rename_axis(None, axis=1)
    processed_df = processed_df.drop(index=0).reset_index(drop=True)
    processed_df.index = processed_df.columns
    print(processed_df.shape)
    return processed_df


def plot_clustermap(data, output_file, n_clusters):
    distance_matrix = 100 * data.astype(float)  # Converting to percentage

    # Performing hierarchical clustering
    linkage = hierarchy.linkage(sp.distance.squareform(distance_matrix.values), method='average')

    # Assigning clusters based on n_clusters
    cluster_assignments = hierarchy.fcluster(linkage, n_clusters, criterion='maxclust')

    # Creating a color palette for the clusters
    cluster_colors = sns.color_palette("Set2", n_clusters)  # Set2 is a perceptually uniform color palette
    row_colors = pd.DataFrame(cluster_assignments, index=data.index, columns=['Cluster'])
    row_colors['Color'] = row_colors['Cluster'].map(lambda x: cluster_colors[x - 1])

    # Creating a clustermap with row colors indicating clusters
    plt.figure(figsize=(10, 8))
    clustered_heatmap = sns.clustermap(
        distance_matrix,
        row_cluster=True,
        col_cluster=True,
        row_linkage=linkage,
        col_linkage=linkage,
        cbar_kws={"shrink": 0.5},
        row_colors=row_colors['Color'].values  # Coloring the rows according to the cluster assignment
    )

    clustered_heatmap.savefig(output_file)
    plt.close()

    # Getting the order of rows after clustering
    row_order = clustered_heatmap.dendrogram_row.reordered_ind
    row_names = data.index[row_order]
    
    return row_names, cluster_assignments[row_order]


def save_row_names_with_clusters(row_names, clusters, output_csv):
    # Grouping rows by their cluster assignments
    cluster_dict = {f'Cluster {i+1}': [] for i in range(max(clusters))}
    
    for name, cluster in zip(row_names, clusters):
        cluster_dict[f'Cluster {cluster}'].append(name)
    
    # Writing clusters and their rows to the CSV file
    with open(output_csv, 'w') as f:
        for cluster, names in cluster_dict.items():
            f.write(f'{cluster}:\n')
            for name in names:
                f.write(f'{name}\n')
            f.write('\n')


def main(csv_file, plot_file, output_csv, n_clusters):
    data = load_and_process_data(csv_file)
    row_names, clusters = plot_clustermap(data, plot_file, n_clusters)
    save_row_names_with_clusters(row_names, clusters, output_csv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("plot heatmap clusters")
    parser.add_argument('-p', '--input_path', type=str, required=True, help="Generalized CSV input path")
    parser.add_argument('-n', '--n_clusters', type=int, required=True, help="Number of clusters to form")
    args = parser.parse_args()
    
    main(args.input_path, 'clustermap.png', 'clustermap.csv', args.n_clusters)
