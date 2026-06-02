from flask import Flask, render_template, request
import fitz
import os

from parser import extract_skills, extract_experience
from matcher import semantic_similarity, skill_match, final_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/match', methods=['POST'])
def match():

    resume_file = request.files['resume']
    jd_file = request.files['jd']

    resume_path = os.path.join(
        UPLOAD_FOLDER,
        resume_file.filename
    )

    jd_path = os.path.join(
        UPLOAD_FOLDER,
        jd_file.filename
    )

    resume_file.save(resume_path)
    jd_file.save(jd_path)

    # Extract PDF text
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    # Experience extraction
    experience = extract_experience(resume_text)

    # Semantic similarity using Groq embeddings
    semantic_score = semantic_similarity(
        resume_text,
        jd_text
    )

    # Skill matching
    matched_skills, missing_skills, skill_score = skill_match(
        resume_skills,
        jd_skills
    )

    # Final combined score
    score = final_score(
        skill_score,
        semantic_score
    )

    explanation = (
        f"Resume matches {len(matched_skills)} required skills "
        f"and is missing {len(missing_skills)} skills. "
        f"Overall semantic similarity with the JD is good."
    )

    return render_template(
        'result.html',
        score=score,
        matched=matched_skills,
        missing=missing_skills,
        experience=experience,
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(debug=True)