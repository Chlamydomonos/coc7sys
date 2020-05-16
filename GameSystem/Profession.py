import pickle


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

    def get_introduction(self):
        temp = ''
        temp2 = ''
        if self.STR != 0:
            temp += '+力量*' + str(self.STR)
        if self.CON != 0:
            temp += '+体质*' + str(self.CON)
        if self.SIZ != 0:
            temp += '+体型*' + str(self.SIZ)
        if self.DEX != 0:
            temp += '+敏捷*' + str(self.DEX)
        if self.APP != 0:
            temp += '+外貌*' + str(self.APP)
        if self.INT != 0:
            temp += '+智力*' + str(self.INT)
        if self.POW != 0:
            temp += '+意志*' + str(self.POW)
        if self.EDU != 0:
            temp += '+教育*' + str(self.EDU)
        for i in range(len(temp)):
            if i > 0:
                temp2 += temp[i]
        return temp2


class ComplexSkillPoints:
    def __init__(self, way1, way2):
        self.way1 = way1
        self.way2 = way2

    def calculate(self, basics):
        return max(self.way1.calculate(basics), self.way2.calculate(basics))

    def get_introduction(self):
        return self.way1.get_introduction() + ' 或' + self.way2.get_introduction()


class Profession:
    def __init__(self, name, skill_points, credit, professional_skills_r1,
                 professional_skills_r2, professional_skills_r3):
        self.name = name
        self.skill_points = skill_points
        self.credit = credit
        self.professional_skills_r1 = professional_skills_r1  # amount of skills that are free to choose
        self.professional_skills_r2 = professional_skills_r2  # alternative skills
        self.professional_skills_r3 = professional_skills_r3  # fixed skills

    def read_introduction(self):
        f = open('ProfessionIntroductions\\' + self.name + '.itd', 'r')
        return f.read()

    def get_skills_introduction(self):
        temp = ''
        for i in range(len(self.professional_skills_r3)):
            if isinstance(self.professional_skills_r3[i], list):
                temp += self.professional_skills_r3[i][0] + ':' + self.professional_skills_r3[i][1]
            else:
                temp += self.professional_skills_r3[i]
            if i < len(self.professional_skills_r3) - 1:
                temp += '，'
        if len(self.professional_skills_r2) > 0:
            temp += '，'
            for i in range(len(self.professional_skills_r2)):
                temp += self.professional_skills_r2[i].get_introduction()
                if i < len(self.professional_skills_r2) - 1:
                    temp += '，'
        if self.professional_skills_r1 > 0:
            temp += '，任意' + str(self.professional_skills_r1) + '项其他技能'
        return temp


class AlternativeSkills:
    def __init__(self, skills, amount):
        self.skills = skills
        self.amount = amount

    def check(self, skills):
        temp = 0
        for i in skills:
            for j in self.skills:
                if i == j:
                    temp += 1
        if temp >= self.amount:
            return True
        else:
            return False

    def get_introduction(self):
        temp = ''
        for i in range(len(self.skills)):
            temp += self.skills[i]
            if i < len(self.skills) - 1:
                temp += '、'
        temp += '中的' + str(self.amount) + '项'
        return temp


def read_profession(name):
    f = open('ProfessionList\\' + name + '.pfs', 'rb')
    return pickle.load(f)


professions = [
    '会计师',
    '杂技演员',
    '演员-戏剧演员'
]
