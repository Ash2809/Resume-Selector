def recommend_top_candidates(resumes, scores, top_n=1):

    ranked_candidates = sorted(zip(resumes, scores), key=lambda x: x[1], reverse=True)
    return ranked_candidates[:top_n]
