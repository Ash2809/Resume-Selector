from sentence_transformers import SentenceTransformer, util
import pandas as pd
import re
from rapidfuzz import fuzz

def extract_skills_from_job_description2(job_description, known_skills):
    job_description = job_description.lower()
    skill_delimiters = r"[,:;\.\-\n]"  
    potential_skills = re.split(skill_delimiters, job_description)
    extracted_skills = set()

    for skill in potential_skills:
        skill = skill.strip()
        for known_skill in known_skills:
            if fuzz.partial_ratio(skill, known_skill) > 80: 
                extracted_skills.add(known_skill)
                break

    return extracted_skills



if __name__ == "__main__":
    job_descriptions = ["""
        Objectives of this role
Design and develop machine learning algorithms and deep learning applications and systems for [Company X]

Solve complex problems with multilayered data sets, and optimize existing machine learning libraries and frameworks 

Collaborate with data scientists, administrators, data analysts, data engineers, and data architects on production systems and applications   

Identify differences in data distribution that could potentially affect model performance in real-world applications

Ensure algorithms generate accurate user recommendations

Stay up to date with developments in the machine learning industry

Responsibilities
Study and transform data science prototypes and apply appropriate machine learning algorithms and tools 

Run machine learning tests and experiments, and document findings and results 

Train, retrain, and monitor machine learning systems and models as needed 

Construct optimized data pipelines to feed machine learning models

Consult with managers to determine and refine machine learning objectives 

Extend existing machine learning libraries and frameworks 
Skills and qualifications
Impeccable analytical and problem-solving skills 

Extensive math and computer skills, with a deep understanding of probability, statistics, and algorithms 

In-depth knowledge of machine learning frameworks, like Keras or PyTorch

Familiarity with data structures, data modeling, and software architecture 

Excellent time management and organizational skills

Desire to learn

Preferred qualifications
Proven experience as a machine learning engineer or similar role 

Familiarity with Python, Java, and R 

Excellent communication and collaboration skills

Innovative mind with a passion for continuous learning 

General knowledge of building machine learning systems 

Bachelor’s degree (or equivalent) in computer science, mathematics, or related field"""
    ]
    known_skills = {
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "ruby", 
    "php", "swift", "go", "rust", "r", "matlab", "kotlin", "scala", 
    "perl", "visual basic", "sql", "bash", "shell scripting", "powershell",

    # Data Science & AI
    "machine learning", "deep learning", "data analysis", "data visualization", 
    "statistical modeling", "nlp", "computer vision", "tensorflow", "keras", 
    "pytorch", "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", 
    "opencv", "huggingface", "transformers", "xgboost", "lightgbm", 

    # Web Development
    "html", "css", "javascript", "react", "angular", "vue.js", "next.js", 
    "node.js", "express.js", "flask", "django", "php", "asp.net", "spring", 
    "graphql", "web3", "tailwind css", "bootstrap", "rest api", "graphql api", "node.js",
    "ppc campaigns",

    # Cloud Computing
    "aws", "azure", "google cloud", "gcp", "heroku", "cloudformation", 
    "terraform", "kubernetes", "docker", "jenkins", "ci/cd", "openstack", 
    "ansible", "cloudwatch", "datadog",

    # DevOps
    "devops", "git", "github actions", "bitbucket", "version control", 
    "jenkins", "circleci", "kubernetes", "docker-compose", "ansible", 
    "terraform", "cloudformation", "helm", "grafana", "prometheus", 
    "elk stack", "splunk", "monitoring tools",

    # Databases
    "mysql", "postgresql", "sqlite", "mongodb", "redis", "elasticsearch", 
    "dynamodb", "cassandra", "neo4j", "oracle db", "sql server", 
    "data warehouse", "etl", "hive", "snowflake", "bigquery",

    # Marketing & SEO
    "seo", "sem", "google analytics", "ppc", "content marketing", 
    "email marketing", "social media marketing", "crm", "hubspot", 
    "salesforce", "lead generation", "brand strategy", "market research",

    # Business & Management
    "project management", "agile", "scrum", "kanban", "jira", "trello", 
    "microsoft project", "business analysis", "risk management", 
    "stakeholder management", "cost estimation", "six sigma",

    # Cybersecurity
    "penetration testing", "vulnerability assessment", "firewalls", 
    "network security", "ethical hacking", "kali linux", "wireshark", 
    "cryptography", "endpoint security", "incident response", 
    "iso 27001", "nist", "compliance",

    "excel", "tableau", "power bi", "qlikview", "autocad", "sap", 
    "sap hana", "sas", "stata", "rpa", "uipath", "blue prism", 
    "jira", "trello", "slack", "microsoft teams", "figma", 
    "adobe photoshop", "adobe illustrator", "canva", "unity", 
    "unreal engine", "solidworks",

    "communication", "teamwork", "problem solving", "critical thinking", 
    "time management", "leadership", "adaptability", "creativity", 
    "negotiation", "conflict resolution"}

    for idx, jd in enumerate(job_descriptions, start=1):
        extracted_skills = extract_skills_from_job_description2(jd, known_skills)
        print(f"Job Description {idx}:\n{jd}\nExtracted Skills: {extracted_skills}\n{'-'*50}")