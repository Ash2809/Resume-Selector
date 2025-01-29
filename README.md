# AI Resume Screening System Documentation

## **Introduction**
The AI Resume Screening System is an advanced tool designed to simplify and automate the process of screening resumes and recommending top candidates for job descriptions. This project leverages state-of-the-art machine learning (ML) and natural language processing (NLP) techniques to parse job descriptions, process resumes, and provide ranked recommendations of the most suitable candidates.

The system supports two types of input data:
1. **CSV Files**: A dataset containing resume data in structured form (e.g., text fields for skills and experience).
2. **PDF Files**: A folder of resumes in PDF format that need to be processed and analyzed.

---

## **Project Workflow**
### **1. Input Parsing**
The system accepts two types of inputs: However the user need not upload the data as it automatically parses the data hardcoded which is consists of 962 resumes however it can parse the PDFs too which are also predefined in components.
- **Job Description**: A text-based job description that specifies required skills, experience, and other criteria.
- **Resume Data**:
  - CSV format containing text fields like "Skills" and "Experience."
  - A folder containing resumes in PDF format.

### **2. Job Description Parsing**
- **Module**: `parse_jd`
- **Process**:
  - Extracts key components from the job description, such as:
    - **Skills**: Identified keywords and phrases (e.g., "Python," "SQL").
    - **Experience**: Minimum required years of experience.
    - **Job Details**: A cleaned and tokenized version of the job description text.
  
### **3. Resume Preprocessing**
- **Modules**:
  - `preprocess_resumes`: For CSV-based resumes.
  - `PDF_parser`: For PDF-based resumes.
- **Process**:
  - For CSV files:
    - Reads data using `pandas`.
    - Extracts relevant columns such as "Skills" and "Experience."
    - Cleans and standardizes text.
  - For PDFs:
    - Uses NLP tools to extract text from each PDF file.
    - Matches extracted text against job description skills using regex.
  - Outputs:
    - A structured DataFrame with "Text," "Skills," and "Experience" fields.

### **4. Embedding Generation**
- **Model**: `SentenceTransformer` (using `all-mpnet-base-v2`).
- **Process**:
  - Generates sentence embeddings for the job description and each resume.
  - These embeddings are numerical vectors that capture the semantic meaning of text.

### **5. Scoring Mechanism**
- **Module**: `score`
- **Process**:
  - Computes the **Cosine Similarity** between the job description and each resume.
  - Adjusts scores based on additional factors like:
    - Skills overlap.
    - Experience difference (e.g., penalizes resumes with less experience than required).
    - The weighted score is calculated by combining the cosine similarity, experience match, and skill match:
    - weighted_score = score.item() + 0.2 * experience_match + 0.5 * skills_match

  - Outputs a score for each resume.

### **6. Candidate Ranking and Recommendation**
- **Module**: `recc`
- **Process**:
  - Ranks candidates based on their scores.
  - Returns the top N candidates with the highest scores, along with their extracted skills and experience.

### **7. Explanation Generation**
- **Module**: `generate_explanation`
- **Process**:
  - Generates a detailed explanation for each recommended candidate:
    - Skills matched and unmatched.
    - Experience comparison.
    - Overall match score.

---

## **Streamlit App**
### **Key Features**
The Streamlit app provides an interactive user interface (UI) to:
1. Upload CSV files or point to a folder of PDF resumes.
2. Input job descriptions.
3. Select the number of top candidates to recommend.
4. View ranked candidates with detailed explanations.

### **How It Works**
1. The user uploads data (CSV or PDF).
2. The app calls `ai_agent_pipeline` to process the resumes and job description.
3. The app displays:
   - Ranked candidates.
   - Their skills, experience, and scores.
   - Detailed explanations for each candidate.

---

## **Machine Learning and NLP Techniques**
### **1. Sentence Embeddings**
- **Model**: `all-mpnet-base-v2` from `sentence-transformers`.
- **Purpose**: Converts textual data into dense numerical vectors that capture semantic meaning.

### **2. Cosine Similarity & weighted scoring**
- **Purpose**: Measures similarity between the job description embedding and each resume embedding.
- **Formula**:
  \[ \text{Cosine Similarity} = \frac{A \cdot B}{||A|| \times ||B||} \]

### **3. Skills Matching**
- **Technique**: Extracts skills from resumes and job descriptions using tokenization and keyword matching.

### **4. Experience Gap Analysis**
- **Technique**: Compares years of experience from resumes against the minimum requirement from the job description.

---

## **Approach and Methodologies**
### **Why Sentence Transformers?**
Sentence Transformers are a specialized model architecture designed to produce high-quality sentence embeddings, which are compact, dense vector representations of text that capture semantic meaning. While BERT is an exceptional model for many NLP tasks, it was not originally optimized for generating sentence-level embeddings. Here's how Sentence Transformers improve upon BERT for similarity and matching tasks:

# **Limitations of BERT*
Token-Level Embeddings:

BERT generates embeddings for individual tokens or words and requires pooling (e.g., using the [CLS] token or averaging all token embeddings) to obtain a sentence embedding. This approach often results in suboptimal representations for sentence-level meaning.
Inefficiency in Pairwise Comparisons:

To compute the similarity between two texts, BERT requires both texts to be concatenated and processed together. For large datasets, this pairwise approach becomes computationally expensive.
Advantages of Sentence Transformers
Optimized for Sentence-Level Embeddings:

Sentence Transformers use a Siamese or triplet network structure where two sentences are processed independently through the model, and their embeddings are compared using a similarity metric like Cosine Similarity. This design ensures embeddings are directly meaningful at the sentence level.
Pretrained on Sentence Similarity Tasks:

Unlike BERT, which is trained primarily on masked language modeling (MLM) and next sentence prediction (NSP), Sentence Transformers are fine-tuned on tasks like Semantic Textual Similarity (STS). This makes their embeddings more suited for semantic tasks such as resume matching.
Efficiency:

Once embeddings are generated for each text (e.g., resumes and the job description), pairwise similarity computations are reduced to simple vector operations (e.g., dot products). This is far more efficient than BERT’s approach.
Higher Accuracy for Matching Tasks:

Sentence Transformers consistently outperform BERT in benchmarks for text similarity and clustering tasks due to their better alignment of embeddings in semantic space.
Practical Impact in Resume Screening
Using Sentence Transformers ensures that resumes and job descriptions are compared based on their semantic content rather than surface-level token matches.
The embeddings capture nuanced relationships between phrases like "3 years of experience in Python development" and "Skilled in Python with 3 years of work experience," ensuring accurate candidate ranking.
By leveraging Sentence Transformers, this project achieves both high accuracy and computational efficiency, making it a robust solution for large-scale resume screening tasks.ks.

### **Why Cosine Similarity?**
- Simple yet effective for comparing high-dimensional vectors.
- Computationally efficient for ranking resumes.

### **Pipeline Design**
The modular design ensures flexibility:
- Separate preprocessing functions for CSV and PDF.
- Easy integration of additional scoring metrics or new models.

---

## **Tech Stack**
### **Programming Language**
- **Python**: Used for both backend processing and web development.

### **Libraries and Frameworks**
1. **ML/NLP**:
   - `sentence-transformers`: For embedding generation.
   - `scikit-learn`: For cosine similarity calculations.
2. **Web Development**:
   - `streamlit`: For building an interactive UI.
3. **Data Handling**:
   - `pandas`: For manipulating resume datasets.
   - `PyPDF2`: For extracting text from PDF resumes.
4. **Other Tools**:
   - `numpy`: For numerical computations.

---

## **How to Use the System**
### **Local Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Resume-Screening-System.git
   ```
2. Navigate to the project folder:
   ```bash
   cd AI-Resume-Screening-System
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```


---

## **Future Enhancements**
1. **Advanced Parsing**:
   - Use Named Entity Recognition (NER) models to extract structured information from resumes and job descriptions.
2. **Multilingual Support**:
   - Incorporate language translation models for non-English resumes.
3. **Dynamic Weighting**:
   - Allow users to assign custom weights to factors like skills match or experience.

---

## **Conclusion**
The AI Resume Screening System streamlines the hiring process by leveraging modern ML and NLP techniques. Its flexibility to handle both structured CSV data and unstructured PDF resumes makes it a versatile tool for recruiters. By automating candidate ranking and providing detailed explanations, the system ensures transparency and efficiency in talent acquisition.

