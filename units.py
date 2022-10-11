import json

def load_candidates():
    with open('candidates.json',encoding='UTF-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_by_pk(pk):
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(skill_name):
    skills = get_all()
    skill_true = []
    for skill in skills:
        if skill_name.lower() in skill['skills'].lower().split(', '):
            skill_true.append(skill)
    return skill_true
