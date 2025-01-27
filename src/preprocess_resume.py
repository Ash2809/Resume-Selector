import re
import pandas as pd

# def preprocess_resumes(resume_data, jd_skills):

#     def extract_details(text):
#         experience_pattern = r"(\d+)\s*(?:years|yrs)\s*experience"
#         skills = {word.strip().lower() for word in text.split() if word.strip().lower() in jd_skills}
#         experience = int(re.findall(experience_pattern, text)[0]) if re.search(experience_pattern, text) else 0
#         return {
#             "text": text,
#             "skills": skills,
#             "experience": experience
#         }
    
#     return resume_data['Resume'].apply(extract_details)

import re
import pandas as pd

def preprocess_resumes(resume_data, jd_skills):

    def extract_details(text):
        experience_pattern = r"(\d+)\s*(?:years|yrs)\s*experience"
        skills = {word.strip().lower() for word in text.split() if word.strip().lower() in jd_skills}
        experience = int(re.findall(experience_pattern, text)[0]) if re.search(experience_pattern, text) else 0
        return {
            "text": text,
            "skills": skills,
            "experience": experience
        }
    
    processed_resumes = resume_data['Resume'].apply(extract_details)
    return pd.DataFrame(processed_resumes.tolist())

if __name__ == "__main__":
    jd_skills = ['python', 'javascript', 'stata', 'excel', 'c', 'pytorch', 'deep learning', 
                 'machine learning', 'r', 'data analysis', 'ethical hacking', 
                 'statistical modeling', 'go', 'nist', 'transformers']
    data = pd.read_csv(r"C:\Projects\Resume-Selector\data\UpdatedResumeDataSet.csv")
    
    if 'Resume' not in data.columns:
        raise KeyError("The column 'Resume' does not exist in the dataset. Please check your input file.")
    
    res = preprocess_resumes(data, jd_skills)
    print(res)
    print("Experience for each resume:")
    print(res['experience'])
