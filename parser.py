import re

SKILLS_DB = [

    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "nlp",
    "tensorflow",
    "pytorch",
    "flask",
    "fastapi",
    "django",
    "power bi",
    "excel",
    "tableau",
    "pandas",
    "numpy",
    "scikit-learn",
    "aws",
    "docker",
    "git",
    "linux"

]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_experience(text):

    pattern = r'(\d+)\s+years?'

    matches = re.findall(
        pattern,
        text.lower()
    )

    if matches:

        return max(
            [int(x) for x in matches]
        )

    return 0