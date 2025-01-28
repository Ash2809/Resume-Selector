from sentence_transformers import util

# def calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details):
#     """
#     Calculate similarity scores between resumes and the job description embedding.
#     """
#     cosine_scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze(1)
    
#     scores = []
#     for i, score in enumerate(cosine_scores):
#         # Use .iloc to access the row in the DataFrame
#         resume = resumes.iloc[i]
        
#         # Experience match check
#         experience_match = resume['experience'] >= jd_details.get('min_experience', 0)
        
#         # Skills match calculation
#         skills_match = len(set(resume['skills']) & set(jd_details.get('skills', set())))
        
#         # Weight skills match and experience match
#         weighted_score = score.item() + 0.5 * experience_match + 0.2 * skills_match
#         scores.append(weighted_score)
    
    # return scores


# def calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details):
#     """
#     Calculate similarity scores between resumes and the job description embedding.
#     """
#     cosine_scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze(1)
#     print("Inside calculate_score.py ")
#     print("Resume head is ")
#     print(resumes.head())
    
#     scores = []
#     for i, score in enumerate(cosine_scores):
#         resume_skills = {skill.lower() for skill in resumes.iloc[i]['skills']}
#         jd_skills = {skill.lower() for skill in jd_details.get('skills', set())}

#         matched_skills = resume_skills & jd_skills
#         experience_match = resumes.iloc[i]['experience'] >= jd_details.get('min_experience', 0)
        
#         skills_match = len(matched_skills)
#         weighted_score = score.item() + 0.2 * experience_match + 0.5 * skills_match
#         scores.append(weighted_score)
    
#     return scores


def calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details):
    """
    Calculate similarity scores between resumes and the job description embedding,
    returning them as percentages for better readability.
    """
    cosine_scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze(1)
    print("Inside calculate_score.py")
    print("Resume head is")
    print(resumes.head())
    
    scores = []
    max_skills = len(jd_details.get('skills', []))
    max_score = 1 + 0.2 + 0.5 * max_skills  # Max possible weighted score
    
    for i, score in enumerate(cosine_scores):
        resume_skills = {skill.lower() for skill in resumes.iloc[i]['skills']}
        jd_skills = {skill.lower() for skill in jd_details.get('skills', set())}

        matched_skills = resume_skills & jd_skills
        experience_match = resumes.iloc[i]['experience'] >= jd_details.get('min_experience', 0)
        
        skills_match = len(matched_skills)
        weighted_score = score.item() + 0.2 * experience_match + 0.5 * skills_match
        
        # Convert weighted score to percentage
        percentage_score = (weighted_score / max_score) * 100
        scores.append(percentage_score)
    
    return scores

