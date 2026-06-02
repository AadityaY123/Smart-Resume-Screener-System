# Smart Resume Screening System

An AI-powered ATS (Applicant Tracking System) built using Flask, NLP, and Machine Learning techniques to compare resumes with job descriptions and generate an ATS match score.

---

# Features

* Upload Resume PDF
* Upload Job Description PDF
* Extracts text from PDFs
* Detects technical skills
* Extracts years of experience
* Calculates:

  * ATS Match Score
  * Matched Skills
  * Missing Skills
  * Semantic Similarity
* Clean Flask Web UI

---

# Tech Stack

## Backend

* Python
* Flask

## NLP / ML

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

## PDF Processing

* PyMuPDF

## Frontend

* HTML
* CSS
* Jinja2 Templates

---

# Project Workflow

```text
User Uploads Resume + JD PDFs
            ↓
PDF Text Extraction using PyMuPDF
            ↓
Skill & Experience Extraction
            ↓
Skill Matching using Set Intersection
            ↓
Semantic Similarity using TF-IDF + Cosine Similarity
            ↓
Weighted ATS Score Calculation
            ↓
Results Displayed in Flask UI
```

---

# How It Works

## 1. PDF Text Extraction

The application extracts raw text from uploaded resume and job description PDFs using PyMuPDF.

## 2. Skill Extraction

The system identifies technical skills from both the resume and JD using NLP-based keyword matching.

## 3. Skill Matching

Matched skills and missing skills are identified using set intersection logic.

### Formula

```text
Skill Match Score =
(Matched Skills / Total JD Skills) × 100
```

## 4. Semantic Similarity

TF-IDF vectorization converts resume and JD text into numerical vectors.

Cosine similarity is then applied to measure overall textual similarity between the two documents.

## 5. Final ATS Score

A weighted scoring algorithm combines:

* Skill Match Score
* Semantic Similarity Score

to generate the final ATS compatibility score.

---

# Project Structure

```text
Smart Resume Screening System/
│
├── app.py
├── matcher.py
├── parser.py
├── requirements.txt
│
├── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── venv/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/smart-resume-screening-system.git
```

## Move Into Project Folder

```bash
cd smart-resume-screening-system
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
flask
pymupdf
scikit-learn
numpy
```

---

# Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Sample Output

* ATS Match Score
* Matched Skills
* Missing Skills
* Experience Extracted
* Resume Analysis Summary

---

# Future Improvements

* LLM-based semantic matching using Groq/OpenAI
* Resume ranking system
* Multi-resume comparison
* Skill ontology matching
* Database integration
* Authentication system
* Dashboard analytics

---

# Learning Outcomes

This project helped in understanding:

* NLP preprocessing
* TF-IDF vectorization
* Cosine similarity
* Flask backend development
* PDF parsing
* ATS system design
* Resume-job semantic matching

---

# Author

Aaditya Yadav

---
