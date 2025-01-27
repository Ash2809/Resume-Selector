from sentence_transformers import SentenceTransformer, util
import pandas as pd
from src.parse_jd import parse_job_description
from src.preprocess_resume import preprocess_resumes
from src.recc import recommend_top_candidates
from src.score import calculate_scores
from src.PDF_parser import preprocess_resumes_from_folder

model = SentenceTransformer('all-mpnet-base-v2') 

# def ai_agent_pipeline(resume_data, job_description, top_n=1):
#     jd_details = parse_job_description(job_description)
#     jd_skills = jd_details["skills"]
    
#     resumes = preprocess_resumes(resume_data, jd_skills)
    
#     resume_texts = resumes['text'].tolist()
#     resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)
#     jd_embedding = model.encode([jd_details["text"]], convert_to_tensor=True)
    
#     scores = calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details)
    
#     top_candidates = recommend_top_candidates(resumes, scores, top_n=top_n)
#     return top_candidates, jd_details

def ai_agent_pipeline(resume_data, job_description, top_n, is_PDF):
    jd_details = parse_job_description(job_description)
    jd_skills = jd_details["skills"]
    
    if(is_PDF):
        folder_path = r"C:\Users\aashutosh kumar\OneDrive\Pictures\INFORMATION-TECHNOLOGY"
        resumes = preprocess_resumes_from_folder(folder_path, jd_skills)
    else:
        resumes = preprocess_resumes(resume_data, jd_skills)
    
    resume_texts = resumes['text'].tolist()
    
    resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)
    jd_embedding = model.encode([jd_details["text"]], convert_to_tensor=True)
    
    scores = calculate_scores(resume_embeddings, jd_embedding, resumes, jd_details)
    
    top_candidates = recommend_top_candidates(resumes, scores, top_n=top_n)
    
    return top_candidates, jd_details


def generate_explanation(candidate, job_description, jd_details):

    matched_skills = set(candidate['skills']) & set(jd_details['skills'])
    unmatched_skills = set(jd_details['skills']) - set(candidate['skills'])
    
    explanation = f"### Why this candidate is the best match for the job:\n\n"
    
    explanation += f"1. **Skills Match**: This candidate has the following skills that match the job description:\n"
    explanation += f"    - Matched Skills: {', '.join(matched_skills)}\n"
    if unmatched_skills:
        explanation += f"    - Unmatched Skills: {', '.join(unmatched_skills)}\n\n"
    
    experience_diff = candidate['experience'] - jd_details['experience']
    explanation += f"2. **Experience**: The candidate has {candidate['experience']} years of experience.\n"
    if candidate['experience'] >= jd_details['experience']:
        explanation += f"    - This exceeds the minimum required experience of {jd_details['experience']} years.\n\n"
    else:
        explanation += f"    - The candidate has {abs(experience_diff)} years less experience than required.\n\n"
    
    explanation += f"3. **Overall Match Score**: This candidate's match score is {candidate['score']:.2f}, indicating a strong alignment with the job description.\n"
    
    return explanation

if __name__ == "__main__":
    # data = pd.DataFrame({
    #     "Category": ["Data Science", "Data Science", "Data Science", "Data Science"],
    #     "Resume": [
    #         "Skills Python, Machine Learning, SQL. 5 years experience.",
    #         "Skills Python, R, Deep Learning. 3 years experience.",
    #         "Skills Tableau, SQL, AI. 2 years experience.",
    #         "Skills SAP HANA, Python. 1 year experience."
    #     ]
    # })

    data = pd.read_csv(r"C:\Projects\Resume-Selector\data\UpdatedResumeDataSet.csv")

    job_description = "Looking for a Data Scientist with skills: Python, Machine Learning, SQL. Minimum 3 years of experience required."

    # Run the pipeline
    top_candidates, jd_details = ai_agent_pipeline(data, job_description, top_n=1, is_PDF=True)

    # Display top candidates and generate explanation
    for idx, (candidate, score) in enumerate(top_candidates, start=1):
        print(f"Rank {idx}:\nResume: {candidate['text']}\nSkills: {candidate['skills']}\nExperience: {candidate['experience']} years\nScore: {score:.2f}\n")

    # Extract the top candidate and score
    top_candidate, top_score = top_candidates[0]  # Extract both candidate and score
    print(jd_details)

    # Attach the score to the candidate dictionary for explanation
    top_candidate['score'] = top_score

    # Generate and print explanation
    explanation = generate_explanation(candidate=top_candidate, job_description=job_description, jd_details=jd_details)
    print(explanation)

