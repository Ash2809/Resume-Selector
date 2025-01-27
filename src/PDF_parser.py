import os
import re
import pandas as pd
import PyPDF2

def extract_experience_and_skills(resume_text, jd_skills):
    experience_years_pattern = r"(\d+)\s*(?:years|yrs)\s*experience"

    date_range_pattern = r"(\b\w+\s+\d{4})\s+to\s+(\b\w+\s+\d{4}|\bPresent\b|\bcurrent\b)"
    
    skills = {word.strip().lower() for word in resume_text.split() if word.strip().lower() in jd_skills}
    
    experience_years = sum(map(int, re.findall(experience_years_pattern, resume_text)))

    total_experience_years = 0
    date_ranges = re.findall(date_range_pattern, resume_text, re.IGNORECASE)
    for start_date, end_date in date_ranges:
        try:
            start_year = int(re.search(r"\d{4}", start_date).group())
            if end_date.lower() in ["present", "current"]:
                end_year = 2025  # Assume the current year
            else:
                end_year = int(re.search(r"\d{4}", end_date).group())
            total_experience_years += end_year - start_year
        except (ValueError, AttributeError):
            continue

    # Combine experiences from years and date ranges
    total_experience_years += experience_years
    
    return {
        "text": resume_text,
        "skills": skills,
        "experience": total_experience_years
    }

def parse_pdf_resumes(pdf_file, jd_skills):
    """
    Parses a PDF resume and extracts skills and experience using regex.
    """
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        resume_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            resume_text += page.extract_text()

    resume_details = extract_experience_and_skills(resume_text, jd_skills)
    return resume_details

def preprocess_resumes_from_folder(folder_path, jd_skills):
    """
    Processes all PDF resumes in the specified folder and extracts experience and skills.
    """
    resumes_data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):  # Check if the file is a PDF
            file_path = os.path.join(folder_path, file_name)
            resume_details = parse_pdf_resumes(file_path, jd_skills)
            resume_details['file_name'] = file_name  # Add file name for reference
            resumes_data.append(resume_details)
    
    return pd.DataFrame(resumes_data)

if __name__ == "__main__":
    # Define job description skills
    jd_skills = ['python', 'javascript', 'stata', 'excel', 'c', 'pytorch', 'deep learning', 
                 'machine learning', 'r', 'data analysis', 'ethical hacking', 
                 'statistical modeling', 'go', 'nist', 'transformers', 'Deep Learning']
    
    # Specify folder path containing resumes
    folder_path = r"C:\Users\aashutosh kumar\OneDrive\Pictures\INFORMATION-TECHNOLOGY"
    
    # Process all PDF files in the folder
    res = preprocess_resumes_from_folder(folder_path, jd_skills)
    
    # Print the results
    print("Extracted Resume Details:")
    print(res[['file_name', 'skills', 'experience']])
