def recommend_career(resume_text):

    careers = {
        "Data Scientist": ["python","machine learning","data"],
        "Web Developer": ["html","css","javascript"],
        "Cyber Security": ["network","security","linux"],
        "AI Engineer": ["deep learning","ai","neural"]
    }

    resume_text = resume_text.lower()
    scores = {}

    for career, skills in careers.items():
        score = 0
        for skill in skills:
            if skill in resume_text:
                score += 1
        scores[career] = score

    best_career = max(scores, key=scores.get)

    return best_career, scores