from GameSystem import Dice


class Diceable:
    def __init__(self, name, value):
        self.name = name
        self.simple = value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def change(self, value):
        self.simple = value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def add(self, value):
        self.simple += value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def minus(self, value):
        self.simple -= value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5


class Skill(Diceable):
    def __init__(self, name, initial, growth, professional, interest):
        self.name = name
        self.initial = initial
        self.growth = growth
        self.professional = professional
        self.interest = interest
        self.simple = initial + growth + professional + interest
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def change(self, value):
        self.simple = value
        self.growth = value - self.initial - self.professional - self.initial
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def add(self, value):
        self.simple += value
        self.growth += value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5

    def minus(self, value):
        self.simple -= value
        self.growth -= value
        self.hard = self.simple // 2
        self.very_hard = self.simple // 5


class Card:
    def __init__(self, info, icon, basics, skills, luck, background, equipments, weapons, items):
        self.info = info  # info = [姓名, 年龄, 性别（0-男，1-女）, 住地, 故乡, 职业]
        self.icon = icon
        self.basics = basics
        self.skills = skills
        self.luck = luck
        self.maxHP = (basics[1].simple + basics[2].simple) // 10
        self.HP = self.maxHP
        self.DB, self.build = self.calculate_build()
        self.MOV = self.calculate_movement()
        self.maxSan = 99 - self.skills[11].simple
        self.san = self.maxSan
        self.background = background
        self.equipments = equipments
        self.weapons = weapons
        self.items = items
        self.consumeLevel = self.calculate_consume_level()
        self.maxMP = self.basics[6] // 5
        self.MP = self.maxMP
        self.experience = []
        self.companion = []
        self.cthulhu_items = []

    def calculate_build(self):
        temp = self.basics[0].simple + self.basics[2].simple
        if temp <= 64:
            return -2, -2
        elif temp <= 84:
            return -1, -1
        elif temp <= 124:
            return 0, 0
        elif temp <= 164:
            return Dice.D4, 1
        elif temp <= 204:
            return Dice.D6, 2
        else:
            return Dice.D6 * ((temp - 204) // 80) + Dice.D6, ((temp - 204) // 80) + 1

    def calculate_movement(self):
        if self.basics[3].simple < self.basics[2].simple & self.basics[0].simple < self.basics[2].simple:
            temp = 7
        elif self.basics[3].simple > self.basics[2].simple & self.basics[0].simple > self.basics[2].simple:
            temp = 9
        else:
            temp = 8
        return temp - ((self.info[1] - 30) // 10)

    def calculate_consume_level(self):
        if self.skills[10].simple <= 0:
            return '身无分文'
        elif self.skills[10].simple < 10:
            return '贫穷'
        elif self.skills[10].simple < 50:
            return '标准'
        elif self.skills[10].simple < 90:
            return '小康'
        elif self.skills[10].simple < 99:
            return '富裕'
        else:
            return '富豪'
