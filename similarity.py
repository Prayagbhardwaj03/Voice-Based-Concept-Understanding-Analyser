from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(user_text, reference_text):
    """
    Returns similarity score between user explanation
    and reference explanation.
    """

    embeddings = model.encode([user_text, reference_text])

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(score * 100, 2)