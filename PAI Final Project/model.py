# model.py

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV file
df = pd.read_csv("data.csv")
answers = df['answer'].fillna("").tolist()

# Load pretrained model and encode all answers
model = SentenceTransformer('all-MiniLM-L6-v2')
answer_embeddings = model.encode(answers)

def get_best_answer(user_input):
    question_embedding = model.encode([user_input])
    similarities = cosine_similarity(question_embedding, answer_embeddings)[0]
    best_match_index = int(np.argmax(similarities))
    best_answer = answers[best_match_index]
    top_indices = np.argsort(similarities)[::-1][1:4]
    similar_answers = [answers[i] for i in top_indices]
    return best_answer, similar_answers

