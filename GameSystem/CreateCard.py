from GameSystem import Card, SkillList

basics_number = 8
skills_number = 60


def create_skills(basic_values, skill_professional_values, skill_interest_values, sub_skill_names):
    basics = []
    skills = []
    for i in range(basics_number):
        basics.append(Card.Diceable(SkillList.basics_name[i], basic_values[i]))
    for i in range(skills_number):
        if isinstance(SkillList.skills_initial, dict):
            skills.append(Card.Skill(SkillList.skills_name[i] + sub_skill_names[i],
                                     SkillList.skills_initial[i][sub_skill_names[i]], 0,
                                     skill_professional_values[i], skill_interest_values[i]))
        else:
            skills.append(Card.Skill(SkillList.skills_name[i] + sub_skill_names[i],
                                     SkillList.skills_initial[i], 0,
                                     skill_professional_values[i], skill_interest_values[i]))
    return basics, skills
