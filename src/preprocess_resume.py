import re
import pandas as pd


# def preprocess_resumes(resume_data, jd_skills):
#     def extract_details(text):
#         try:
#             # Updated experience pattern to capture common formats
#             experience_pattern = r"(\d+)\s*(?:year[s]?|yr[s]?)?\s*(\d+)?\s*(?:month[s]?)?"
            
#             # Skills extraction: handle comma-separated and free-text patterns
#             skills_pattern = r"(?:skills[:\s]+)?([\w\s,]+)"
#             skills_match = re.search(skills_pattern, text, re.IGNORECASE)
            
#             if skills_match:
#                 extracted_skills = skills_match.group(1)
#                 # Normalize skills and match with JD skills
#                 skills = {skill.strip().lower() for skill in re.split(r"[,\s]+", extracted_skills) if skill.strip().lower() in jd_skills}
#             else:
#                 skills = set()
            
#             # Extract experience
#             experience = 0
#             match = re.search(experience_pattern, text, re.IGNORECASE)
#             if match:
#                 years = int(match.group(1)) if match.group(1) else 0
#                 months = int(match.group(2)) if match.group(2) else 0
#                 experience = years + (months / 12)  # Convert months to years
            
#             return {
#                 "text": text,
#                 "skills": skills,
#                 "experience": experience
#             }
#         except Exception as e:
#             print(f"Error processing resume: {text}")
#             raise e

#     processed_resumes = resume_data['Resume'].apply(extract_details)
#     return pd.DataFrame(processed_resumes.tolist())


# if __name__ == "__main__":
#     jd_skills = ['python', 'javascript', 'stata', 'excel', 'c', 'pytorch', 'deep learning', 
#                  'machine learning', 'r', 'data analysis', 'ethical hacking', 
#                  'statistical modeling', 'go', 'nist', 'transformers']
    
#     # Simulated data for testing
#     # data = pd.DataFrame({
#     #     "Category": ["Data Science", "Data Science", "Data Science", "Data Science"],
#     #     "Resume": [
#     #         "Skills: Python, Machine Learning, SQL. 5 years experience.",
#     #         "Skills Python, R, Deep Learning. 3 years experience.",
#     #         "Skills Tableau, SQL, AI. 2 years experience.",
#     #         "Skills SAP HANA, Python. 1 year experience."
#     #     ]
#     # })
#     data = pd.read_csv(r"C:\Projects\Resume-Selector\data\UpdatedResumeDataSet.csv")
    
#     if 'Resume' not in data.columns:
#         raise KeyError("The column 'Resume' does not exist in the dataset. Please check your input file.")
    
#     # Process resumes
#     res = preprocess_resumes(data, jd_skills)
#     print(res)


import re
import pandas as pd


def preprocess_resumes(resume_data, jd_skills):
    def extract_details(text):
        try:
            # Experience pattern
            experience_pattern = r"(\d+)\s*(?:year[s]?|yr[s]?)?\s*(?:and\s*(\d+)\s*month[s]?)?"
            
            # Skills pattern
            skills_pattern = r"(?:skills|technologies|expertise|proficient in|Computer Skills)[:\s]+([\w\s,]+)"
            
            # Debugging aid
            print(f"Processing text: {text[:10]}...")

            # Extract skills
            skills_match = re.search(skills_pattern, text, re.IGNORECASE)
            if skills_match:
                extracted_skills = skills_match.group(1)
                # Normalize skills and match with JD skills
                skills = {skill.strip().lower() for skill in re.split(r"[,\s]+", extracted_skills) if skill.strip().lower() in jd_skills}
            else:
                skills = set()

            # Extract experience
            experience = 0
            experience_match = re.search(experience_pattern, text, re.IGNORECASE)
            if experience_match:
                years = int(experience_match.group(1)) if experience_match.group(1) else 0
                months = int(experience_match.group(2)) if experience_match.group(2) else 0
                experience = years + (months / 12)
            if(experience > 20):
                experience = 0

            # Return extracted data
            return {
                "text": text,
                "skills": skills,
                "experience": experience
            }
        except Exception as e:
            print(f"Error processing resume: {text}")
            raise e

    processed_resumes = resume_data['Resume'].apply(extract_details)
    return pd.DataFrame(processed_resumes.tolist())


if __name__ == "__main__":
    jd_skills = ['python', 'javascript', 'stata', 'excel', 'c', 'pytorch', 'deep learning', 
                 'machine learning', 'r', 'data analysis', 'ethical hacking', 
                 'statistical modeling', 'go', 'nist', 'transformers', 'MS-PowerPoint']
    
    # Load dataset
    # data = pd.read_csv(r"C:\Projects\Resume-Selector\data\UpdatedResumeDataSet.csv")
    data = pd.DataFrame({
        "Category": ["Data Science", "Data Science", "Data Science", "Data Science"],
        "Resume": [
            "Skills: Python, Machine Learning, SQL. 5 years experience.",
            "Skills Python, R, Deep Learning. 3 years experience.",
            "Skills Tableau, SQL, AI. 2 years experience.",
            "Skills SAP HANA, Python. 1 year experience."
        ]
    })
    
    if 'Resume' not in data.columns:
        raise KeyError("The column 'Resume' does not exist in the dataset. Please check your input file.")
    
    # Process resumes
    res = preprocess_resumes(data, jd_skills)
    print(res)
