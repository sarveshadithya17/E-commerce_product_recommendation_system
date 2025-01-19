# Import required libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the matrix
final_ratings_matrix = pd.read_csv(r'C:\Sarvesh\recommendation-system\data\final_ratings_matrix.csv', index_col=0)

# Define a function to find similar users
def similar_users(user_index, interactions_matrix):
    similarity = []
    for user in range(interactions_matrix.shape[0]):
        sim = cosine_similarity(
            [interactions_matrix.loc[user_index]],
            [interactions_matrix.loc[user]]
        )
        similarity.append((user, sim))
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_users = [tup[0] for tup in similarity]
    similarity_scores = [tup[1] for tup in similarity]
    most_similar_users.remove(user_index)
    similarity_scores.pop(0)
    return most_similar_users, similarity_scores

# Define a function to generate recommendations
def recommendations(user_index, num_of_products, interactions_matrix):
    most_similar_users = similar_users(user_index, interactions_matrix)[0]
    user_interactions = set(interactions_matrix.columns[np.where(interactions_matrix.loc[user_index] > 0)])
    recommended_products = []

    for similar_user in most_similar_users:
        if len(recommended_products) >= num_of_products:
            break
        similar_user_interactions = set(interactions_matrix.columns[np.where(interactions_matrix.loc[similar_user] > 0)])
        new_recommendations = similar_user_interactions - user_interactions
        recommended_products.extend(list(new_recommendations))
        user_interactions.update(similar_user_interactions)

    return recommended_products[:num_of_products]

# Test recommendations for specific users
print("Recommendations for User 3:", recommendations(3, 5, final_ratings_matrix))
print("Recommendations for User 1521:", recommendations(1521, 5, final_ratings_matrix))
