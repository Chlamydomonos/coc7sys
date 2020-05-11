class SkillPoints:
    def __init__(self, STR, CON, SIZ, DEX, APP, INT, POW, EDU):
        self.STR = STR
        self.CON = CON
        self.SIZ = SIZ
        self.DEX = DEX
        self.APP = APP
        self.INT = INT
        self.POW = POW
        self.EDU = EDU

    def calculate(self, basics):
        return basics[0] * self.STR + basics[1] * self.CON + basics[2] * self.SIZ + basics[3] * self.DEX + \
               basics[4] * self.APP + basics[5] * self.INT + basics[6] * self.POW + basics[7] * self.EDU

    def __add__(self, other):
        return SkillPoints(self.STR + other.STR, self.CON + other.CON, self.SIZ + other.SIZ, self.DEX + other.DEX,
                           self.APP + other.APP, self.INT + other.INT, self.POW + other.POW, self.EDU + other.EDU)


typical_skill_points = SkillPoints(0, 0, 0, 0, 0, 0, 0, 4)


class Profession:
    def __init__(self, name, skill_points, credit, professional_skills_r1,
                 professional_skills_r2, professional_skills_r3, introduction):
        self.name = name
        self.skill_points = skill_points
        self.credit = credit
        self.professional_skills_r1 = professional_skills_r1  # amount of skills that are free to choose
        self.professional_skills_r2 = professional_skills_r2  # alternative skills
        self.professional_skills_r3 = professional_skills_r3  # fixed skills
        self.introduction = introduction


class AlternativeSkills:
    def __init__(self, name, skills, amount):
        self.name = name
        self.skills = skills
        self.amount = amount


professions = {}
