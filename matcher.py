from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_similarity(text1, text2):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [text1, text2]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return round(similarity * 100, 2)


def skill_match(resume_skills, jd_skills):

    matched = list(
        set(resume_skills) & set(jd_skills)
    )

    missing = list(
        set(jd_skills) - set(resume_skills)
    )

    if len(jd_skills) == 0:
        score = 0
    else:
        score = (
            len(matched) / len(jd_skills)
        ) * 100

    return matched, missing, round(score, 2)


def final_score(skill_score, semantic_score):

    return round(
        (0.7 * skill_score) +
        (0.3 * semantic_score),
        2
    )