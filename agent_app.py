import streamlit as st
from main import ai_agent_pipeline, generate_explanation  
import pandas as pd

st.title("AI Resume Screening System")
st.write("Upload resumes and input a job description to find the best-matched candidates.")

st.subheader("Job Description")
job_description = st.text_area("Enter the job description", "")

data = pd.DataFrame({
        "Category": ["Data Science", "Data Science", "Data Science", "Data Science"],
        "Resume": [
            "Skills Python, Machine Learning, SQL. 5 years experience.",
            "Skills Python, R, Deep Learning. 3 years experience.",
            "Skills Tableau, SQL, AI. 2 years experience.",
            "Skills SAP HANA, Python. 1 year experience."
        ]
    })

if st.button("Find Candidates"):
    if not job_description:
        st.error("Please enter a job description.")
    else:
        try:
            top_candidates, jd_details = ai_agent_pipeline(data, job_description, top_n=1, is_PDF=False)
            
            # Display the results
            st.subheader("Top Candidates")
            for idx, (candidate, score) in enumerate(top_candidates, start=1):
                print(f"Rank {idx}:\nResume: {candidate['text']}\nSkills: {candidate['skills']}\nExperience: {candidate['experience']} years\nScore: {score:.2f}\n")

            top_candidate, top_score = top_candidates[0]  
            print(jd_details)

            top_candidate['score'] = top_score
            explanation = generate_explanation(candidate=top_candidate, job_description=job_description, jd_details=jd_details)
            st.write(explanation)
            
        except Exception as e:
            st.error(f"Error processing resumes: {e}")
