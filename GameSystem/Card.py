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


class InitialSkill:
    def __init__(self, main_name, branch_name, initial):
        self.main_name = main_name
        self.branch_name = branch_name
        self.name = main_name + branch_name
        self.initial = initial

    def amend_initial(self, value):
        self.initial = value


class Skill(InitialSkill, Diceable):
    def __init__(self, initial_skill, growth, professional, interest):
        self.main_name = initial_skill.main_name
        self.branch_name = initial_skill.branch_name
        self.name = self.main_name + self.branch_name
        self.initial = initial_skill.initial
        self.growth = growth
        self.professional = professional
        self.interest = interest
        self.simple = self.initial + self.growth + self.professional + self.interest
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
    def __init__(self, info, profession, basics, skills, background):
        self.info = info  # info = [姓名, 性别（0-男，1-女）, 年龄, 住地, 故乡]
        self.profession = profession
        self.basics = basics  # basics = [STR, CON, SIZ, DEX, APP, INT, POW, EDU]
        self.skills = skills
        self.luck = self.calculate_luck()
        self.maxHP = (basics[1].simple + basics[2].simple) // 10
        self.HP = self.maxHP
        self.DB, self.build = self.calculate_build()
        self.MOV = self.calculate_movement()
        self.maxSan = 99 - self.skills[11].simple
        self.san = self.basics[6].simple
        self.background = background
        self.equipments = []
        self.weapons = []
        self.items = []
        self.consumeLevel = self.calculate_consume_level()
        self.maxMP = self.basics[6].simple // 5
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

    def calculate_luck(self):
        if self.info[1] < 20:
            temp1 = (Dice.D6 * 3).throw() * 5
            temp2 = (Dice.D6 * 3).throw() * 5
            return max(temp1, temp2)
        else:
            return (Dice.D6 * 3).throw() * 5

    def add_equipment(self, equipment):
        self.equipments.append(equipment)

    def remove_equipment(self, equipment_id):
        del self.equipments[equipment_id]

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def remove_weapon(self, weapon_id):
        del self.weapons[weapon_id]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        del self.items[item_id]


class CardList:
    def __init__(self):
        self.list = []

    def add_card(self, card: Card):
        temp = len(self.list) + 1
        self.list.append(card.info[0] + '--' + str(temp))

    def delete_card(self, card_id):
        del self.list[card_id]