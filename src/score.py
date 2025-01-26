from sentence_transformers import util

def calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details):
    """
    Calculate similarity scores between resumes and the job description embedding.
    """
    cosine_scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze(1)
    
    scores = []
    for i, score in enumerate(cosine_scores):
        experience_match = resumes[i]['experience'] >= jd_details.get('min_experience', 0)
        skills_match = len(resumes[i]['skills'] & jd_details.get('skills', set()))
        # Weight skills match and experience match
        weighted_score = score.item() + 0.5 * experience_match + 0.2 * skills_match
        scores.append(weighted_score)
    
    return scores
