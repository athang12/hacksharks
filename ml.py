import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
data = pd.read_csv('interest_data.csv')

# Load pre-trained GloVe embeddings
embeddings_index = {}
with open('glove.6B.100d.txt', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

# Function to compute the average vector representation of user interests
def get_user_vector(user_interests):
    user_vector = np.zeros((100,))
    count = 0
    for interest in user_interests:
        words = interest.lower().split('_')
        for word in words:
            if word in embeddings_index:
                user_vector += embeddings_index[word]
                count += 1
    if count > 0:
        user_vector /= count
    return user_vector

# Function to recommend interests based on user input
def recommend_interests(user_interests):
    # Get the average vector representation of user interests
    user_vector = get_user_vector(user_interests)

    # Compute cosine similarity between user vector and all interest vectors
    interest_vectors = [get_user_vector(interest.lower().split('_')) for interest in data['interest']]
    similarities = cosine_similarity([user_vector], interest_vectors)

    # Sort the interests based on similarity scores
    sorted_indices = np.argsort(similarities)[0][::-1]
    sorted_interests = [data['interest'][i] for i in sorted_indices]

    # Get the top 10 recommended interests
    recommended_interests = sorted_interests[:1]

    return recommended_interests

# Take user inputs
user_interests = []
for i in range(5):
    interest = input(f"Enter interest {i+1}: ")
    user_interests.append(interest)

# Get recommended interests
recommended_interests = recommend_interests(user_interests)

# Print the recommended interests
print("Predicted Interests:")
for interest in recommended_interests:
    li = interest.split(',')
    for i in li :
        print(i)