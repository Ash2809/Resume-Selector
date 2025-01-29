from sentence_transformers import util


def calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details):
    cosine_scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze(1)
    print("Inside calculate_score.py")
    print("Resume head is")
    print(resumes.head())
    
    scores = []
    max_skills = len(jd_details.get('skills', []))
    max_score = 1 + 0.2 + 0.5 * max_skills 
    
    for i, score in enumerate(cosine_scores):
        resume_skills = {skill.lower() for skill in resumes.iloc[i]['skills']}
        jd_skills = {skill.lower() for skill in jd_details.get('skills', set())}

        matched_skills = resume_skills & jd_skills
        experience_match = resumes.iloc[i]['experience'] >= jd_details.get('min_experience', 0)
        
        skills_match = len(matched_skills)
        weighted_score = score.item() + 0.2 * experience_match + 0.5 * skills_match
        
  
        percentage_score = (weighted_score / max_score) * 100
        scores.append(percentage_score)
    
    return scores

