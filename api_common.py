import numpy as np
from json import loads
from loguru import logger
from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer()


def tp_vector_create(details):
    vector = vectorizer.fit_transform([details]).toarray()[0].tolist()

    return vector


def tp_vector_similarity_search(location, travel_planner):
    try:
        desc_similarities = []
        travel_planner_conn = travel_planner.cursor()

        travel_planner_conn.execute("select * from travel_kb")
        tp_response = travel_planner_conn.fetchall()

        for data in tp_response:
            query_vector = vectorizer.fit_transform([location]).toarray()[0]
            tp_vector = loads(data[-1])
            tp_vector = np.array(tp_vector)
            cos_sim = similarity(query_vector, tp_vector)
            desc_similarities.append((data, round(cos_sim, 2)))

        desc_similarities.sort(key=lambda x: x[1], reverse=True)

        return desc_similarities[:3]

    except Exception as e:
        logger.info(f"Error: {e}")

    finally:
        travel_planner_conn.close()


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)


def similarity(query_vector, tp_vector):
    max_length = max(len(query_vector), len(tp_vector))
    qv_padded = np.pad(
        query_vector, (0, max_length - len(query_vector)), 'constant'
    )
    tp_padded = np.pad(tp_vector, (0, max_length - len(tp_vector)), 'constant')
    cos_sim = cosine_similarity(qv_padded, tp_padded)
    return cos_sim
