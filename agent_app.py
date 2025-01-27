import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from src.parse_jd import parse_job_description
from src.preprocess_resume import preprocess_resumes
from src.recc import recommend_top_candidates
from src.score import calculate_scores
from main import ai_agent_pipeline

model = SentenceTransformer('all-mpnet-base-v2') 

def generate_explanation(candidate, job_description, jd_details):
    """
    Generates an explanation of why a candidate is the best match for the job.
    """
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

def main():
    st.title("AI Resume Selector")
    st.write("Enter a Job Description to match the top resumes.")

    job_description = st.text_area("Job Description", height=150, placeholder="Enter the job description here...")

    if st.button("Match Resumes"):
        if job_description:
            data = pd.read_csv(r"C:\Projects\Resume-Selector\data\UpdatedResumeDataSet.csv")
            
            top_candidates = ai_agent_pipeline(data, job_description, top_n=2)
            
            if top_candidates:
                st.write("### Top Matching Resumes")
                for idx, (candidate, score) in enumerate(top_candidates, start=1):
                    st.write(f"**Rank {idx}:**")
                    st.write(f"**Resume:** {candidate['text']}")
                    st.write(f"**Skills:** {candidate['skills']}")
                    st.write(f"**Experience:** {candidate['experience']} years")
                    st.write(f"**Score:** {score:.2f}")
                    st.write("---")

                explanation = generate_explanation(top_candidates, job_description, jd_details)
                st.write(explanation)
            else:
                st.write("No matching candidates found.")
        else:
            st.warning("Please enter a job description to match resumes.")

if __name__ == "__main__":
    main()
