# def recommend_top_candidates(resumes, scores, top_n=1):
#     """
#     Recommend top candidates based on their scores.
#     """
#     # Pair the resumes with their corresponding scores and sort them in descending order
#     ranked_candidates = sorted(zip(resumes, scores), key=lambda x: x[1], reverse=True)
    
#     # Return the top N candidates
#     return ranked_candidates[:top_n]


def recommend_top_candidates(resumes, scores, top_n=1):
    # Ensure resumes are in the correct format (as dictionaries with 'text', 'skills', etc.)
    ranked_candidates = sorted(zip(resumes.to_dict(orient='records'), scores), key=lambda x: x[1], reverse=True)
    return ranked_candidates[:top_n]

