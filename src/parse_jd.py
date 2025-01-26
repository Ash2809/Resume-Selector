from src.skill_extraction import extract_skills_from_job_description2
import re

def parse_job_description(job_description):
    """
    Extracts required skills and experience from the job description.
    """
    jd_skills = extract_skills_from_job_description2(job_description)
    print(jd_skills)
    experience_pattern = r"(\d+)\s*(?:years|yrs)\s*experience"
    experience = int(re.findall(experience_pattern, job_description)[0]) if re.search(experience_pattern, job_description) else 0
    return {
        "text": job_description,
        "skills": jd_skills,
        "experience": experience
    }

if __name__ == "__main__":
    jd = """
    **Job Title:** Machine Learning Engineer  
    **Location:** [Location] (Remote options available)  
    **Job Type:** Full-Time

    **About Us:**  
    [Company Name] is a cutting-edge technology company focused on leveraging data and advanced algorithms to solve real-world problems. We are seeking a talented and motivated Machine Learning Engineer to join our team and help us build innovative solutions that scale. This is a great opportunity to work in a dynamic, collaborative environment where you can grow your skills and make a real impact.

    **Responsibilities:**  
    - Design, develop, and deploy machine learning models and algorithms to solve complex business problems.
    - Collaborate with data scientists, software engineers, and other stakeholders to integrate machine learning models into production systems.
    - Conduct research to improve the performance and scalability of existing models.
    - Continuously monitor and fine-tune deployed models to ensure optimal performance.
    - Work with large datasets, preprocess, clean, and explore data to extract valuable insights.
    - Stay up to date with the latest advancements in machine learning and artificial intelligence.

    **Requirements:**  
    - Bachelor’s or Master’s degree in Computer Science, Engineering, Mathematics, or a related field (or equivalent experience).
    - Proven experience building and deploying machine learning models in a production environment.
    - Strong programming skills in Python, Java, C++, or similar languages.
    - Solid understanding of machine learning algorithms (e.g., regression, classification, clustering, neural networks, reinforcement learning).
    - Experience with machine learning frameworks such as TensorFlow, Keras, PyTorch, or scikit-learn.
    - Familiarity with data processing libraries such as NumPy, pandas, and tools for big data processing (e.g., Hadoop, Spark).
    - Strong problem-solving skills and ability to work independently or in a team.
    - Excellent communication skills and ability to explain technical concepts to non-technical stakeholders.

    **Nice to Have:**  
    - Experience with cloud platforms (AWS, GCP, Azure).
    - Knowledge of deep learning and NLP techniques.
    - Experience with containerization and orchestration (e.g., Docker, Kubernetes).
    - Familiarity with version control (e.g., Git).

    **Benefits:**  
    - Competitive salary and bonus structure
    - Health, dental, and vision insurance
    - Paid time off and holidays
    - Professional development opportunities
    - Flexible work hours and remote work options
    - Collaborative and innovative work environment"""

    res = parse_job_description(jd)
    print(res)

