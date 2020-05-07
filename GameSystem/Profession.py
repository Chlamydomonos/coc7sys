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


class Profession:
    def __init__(self, professional_skills, skill_points):
        self.professional_skills = professional_skills
        self.skill_points = skill_points
