from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# Load interaction matrix
interaction_matrix = pd.read_csv(r'C:\Sarvesh\recommendation-system\data\final_ratings_matrix.csv', index_col=0)

def similar_users(user_index, matrix):
    similarity = []
    for user in range(matrix.shape[0]):
        sim = cosine_similarity(
            [matrix.loc[user_index]],
            [matrix.loc[user]]
        )
        similarity.append((user, sim))
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_users = [tup[0] for tup in similarity]
    similarity_scores = [tup[1] for tup in similarity]
    most_similar_users.remove(user_index)
    similarity_scores.pop(0)
    return most_similar_users, similarity_scores

def recommend_products(user_index, num_of_products, matrix):
    most_similar_users = similar_users(user_index, matrix)[0]
    user_interactions = set(matrix.columns[np.where(matrix.loc[user_index] > 0)])
    recommendations = []
    for similar_user in most_similar_users:
        if len(recommendations) >= num_of_products:
            break
        similar_user_interactions = set(matrix.columns[np.where(matrix.loc[similar_user] > 0)])
        new_recommendations = similar_user_interactions - user_interactions
        recommendations.extend(list(new_recommendations))
        user_interactions.update(similar_user_interactions)
    return recommendations[:num_of_products]

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id')
    num_products = data.get('num_products', 5)
    try:
        recommendations = recommend_products(user_id, num_products, interaction_matrix)
        return jsonify({'user_id': user_id, 'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
