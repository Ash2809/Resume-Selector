# Resume Matching and Recommendation System

This project focuses on building an AI-driven system to analyze resumes and recommend candidates for job descriptions using NLP and Machine Learning techniques. The system processes resumes, extracts relevant information, and calculates similarity scores based on job requirements to recommend the best matches.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [File Structure](#file-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Detailed File Description](#detailed-file-description)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

This project automates the process of matching resumes with job descriptions (JD). It:
- Parses resumes (PDF or text-based).
- Extracts skills and experience details.
- Calculates a similarity score between resumes and job descriptions.
- Outputs recommendations based on weighted criteria such as skill match and experience.

---

## Features

- **Resume Parsing:** Extracts data from resumes in PDF or text format.
- **Skill Extraction:** Extracts skills from resumes and compares them with the job description.
- **Similarity Scoring:** Calculates a weighted similarity score for ranking candidates.
- **Customizable Job Descriptions:** Allows users to define job details with required skills and experience.
- **Reproducibility:** Modular design for easy customization and extension.

---

## File Structure

```plaintext
project/
│
├── data/                  # Contains datasets for resumes and job descriptions.
│   └── UpdatedResumeData.csv
│
├── exp/                   # Experiments and exploratory data analysis.
│   └── eda.ipynb
│
├── src/                   # Source code for the project.
│   ├── __init__.py        # Package initializer.
│   ├── parse_jd.py        # Job description parsing functions.
│   ├── PDF_parser.py      # Parses resumes in PDF format.
│   ├── preprocess_resume.py # Preprocessing functions for resumes.
│   ├── recc.py            # Recommendation system functions.
│   ├── score.py           # Calculates similarity scores.
│   ├── skill_extraction.py # Extracts skills from resumes.
│   └── agent_app.py       # Main application script for agent-based interactions.
│
├── .gitignore             # Specifies files and directories to ignore in version control.
├── LICENSE                # License for the project.
├── main.py                # Entry point for the program.
├── README.md              # Project documentation.
└── requirements.txt       # Python dependencies.
```

---

## Installation

### Prerequisites

- Python 3.8 or above
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Ash2809/Resume-Selector.git
   cd Resume-Selector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have your dataset (`UpdatedResumeData.csv`) in the `data` directory.

---

## Usage

1. Run the main application:
   ```bash
   python main.py
   ```

2. Customize job descriptions and input resumes by modifying files or via the provided interface.

3. View recommendations and similarity scores for the candidates.

---

## Detailed File Description

### **`data/`**
- **`UpdatedResumeData.csv`:** Dataset containing sample resumes with details such as skills, experience, etc.

### **`exp/`**
- **`eda.ipynb`:** Jupyter Notebook for exploratory data analysis (EDA) on the dataset.

### **`src/`**
- **`__init__.py`:** Initializes the `src` package.
- **`parse_jd.py`:** Contains functions for parsing and processing job descriptions into structured data.
- **`PDF_parser.py`:** Extracts text and relevant information from resumes in PDF format.
- **`preprocess_resume.py`:** Preprocesses resumes for analysis, such as cleaning, tokenizing, and standardizing data.
- **`recc.py`:** Implements the recommendation logic, matching candidates to job descriptions.
- **`score.py`:** Contains the `calculate_scores` function to compute similarity scores between resumes and job descriptions using weighted criteria.
- **`skill_extraction.py`:** Extracts skills from resumes and identifies matches with job description requirements.
- **`agent_app.py`:** Main script that integrates components into an interactive application (e.g., agent or chatbot).

### **Root Files**
- **`.gitignore`:** Lists files and directories to be ignored by Git.
- **`LICENSE`:** Specifies the license under which the project is distributed.
- **`main.py`:** Entry point for running the system. Orchestrates all components to perform resume matching and recommendations.
- **`README.md`:** Documentation for the project (you're reading it now!).
- **`requirements.txt`:** Lists all Python dependencies required for the project.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to replace **your-repo** in the repository URL with your actual GitHub repository link. Let me know if you'd like further refinements!