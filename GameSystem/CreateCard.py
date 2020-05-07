from GameSystem import Card, SkillList, Dice

basics_number = 8
skills_number = 60


def random_basics():
    temp1 = Dice.D6 * 3
    temp2 = Dice.D6 * 2 + 6
    return [temp1.throw() * 5, temp1.throw() * 5, temp2.throw() * 5, temp1.throw() * 5,
            temp1.throw() * 5, temp2.throw() * 5, temp1.throw() * 5, temp2.throw() * 5]


def create_skills(basic_values, skill_professional_values, skill_interest_values, sub_skill_names):
    basics = []
    skills = []
    for i in range(basics_number):
        basics.append(Card.Diceable(SkillList.basics_name[i], basic_values[i]))
    for i in range(skills_number):
        if isinstance(SkillList.initial_skills, dict):
            skills.append(Card.Skill(SkillList.initial_skills[i][sub_skill_names[i]], 0,
                                     skill_professional_values[i], skill_interest_values[i]))
        else:
            skills.append(Card.Skill(SkillList.initial_skills[i], 0,
                                     skill_professional_values[i], skill_interest_values[i]))
    return basics, skills
