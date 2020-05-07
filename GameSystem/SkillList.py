from GameSystem.Card import InitialSkill

basics_name = ['力量(STR)', '体质(CON)', '体型(SIZ)', '敏捷(DEX)', '外貌(APP)', '智力(INT)', '意志(POW)', '教育(EDU)']
skills_name = ['会计', '人类学', '估价', '考古学', '技艺:', '技艺:', '技艺:', '魅惑', '攀爬', '计算机使用 Ω',
               '信用评级', '克苏鲁神话', '乔装', '闪避', '汽车驾驶', '电气维修', '电子学 Ω', '话术', '格斗:斗殴', '格斗:',
               '格斗:', '射击:手枪', '射击:', '射击:', '急救', '历史', '恐吓', '跳跃', '语言:', '语言:',
               '语言:', '母语:', '法律', '图书馆使用', '聆听', '锁匠', '机械维修', '医学', '自然学', '导航',
               '神秘学', '操作重型机械', '说服', '驾驶:', '精神分析', '心理学', '骑术', '科学:', '科学:', '科学:',
               '妙手', '侦察', '潜行', '生存:', '生存:', '游泳', '投掷', '追踪', '罕见:', '学问:']
fighting_sub_skill_initial = {'鞭子': 5, '电锯': 5, '斧': 5, '剑': 5, '绞索': 5, '链枷': 5, '矛': 5}
firearms_sub_skill_initial = {'步枪/霰弹枪': 25, '冲锋枪': 25, '弓术': 25, '火焰喷射器': 25, '机枪': 25, '重武器': 25}
special_sub_skill_initial = {'爆破': 1, '催眠': 1, '读唇': 1, '炮术': 1, '潜水': 1, '驯兽': 1}
skills_initial = [5, 1, 5, 1, 5, 5, 5, 15, 20, 5,
                  0, 0, 5, 0, 20, 10, 1, 5, 25, fighting_sub_skill_initial,
                  fighting_sub_skill_initial, 20, firearms_sub_skill_initial, firearms_sub_skill_initial, 30,
                  5, 15, 20, 1, 1,
                  1, 0, 5, 20, 20, 1, 10, 1, 10, 10,
                  5, 1, 10, 1, 1, 10, 5, 1, 1, 1,
                  10, 25, 20, 10, 10, 20, 20, 10, special_sub_skill_initial, 1]

art_initial_skills = {}

initial_skills = [InitialSkill('会计', '', 5),
                  InitialSkill('人类学', '', 1),
                  InitialSkill('估价', '', 5),
                  InitialSkill('考古学', '', 1),
                  art_initial_skills,
                  art_initial_skills,
                  art_initial_skills,
                  InitialSkill('魅惑', '', 15),
                  InitialSkill('攀爬', '', 20),
                  InitialSkill('计算机使用 Ω', '', 5)]
