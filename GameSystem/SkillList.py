from GameSystem.Card import InitialSkill

basics_name = ['力量(STR)', '体质(CON)', '体型(SIZ)', '敏捷(DEX)', '外貌(APP)', '智力(INT)', '意志(POW)', '教育(EDU)']

art_initial_skills = {'表演': InitialSkill('技艺:', '表演', 5),
                      '美术': InitialSkill('技艺:', '美术', 5),
                      '摄影': InitialSkill('技艺:', '摄影', 5),
                      '伪造': InitialSkill('技艺:', '伪造', 5),
                      '写作': InitialSkill('技艺:', '写作', 5),
                      '书法': InitialSkill('技艺:', '书法', 5),
                      '音乐': InitialSkill('技艺:', '音乐', 5),
                      '厨艺': InitialSkill('技艺:', '厨艺', 5),
                      '裁缝': InitialSkill('技艺:', '裁缝', 5),
                      '理发': InitialSkill('技艺:', '理发', 5),
                      '建筑': InitialSkill('技艺:', '建筑', 5),
                      '舞蹈': InitialSkill('技艺:', '舞蹈', 5),
                      '酿酒': InitialSkill('技艺:', '酿酒', 5),
                      '捕鱼': InitialSkill('技艺:', '捕鱼', 5),
                      '农事': InitialSkill('技艺:', '农事', 5),
                      '打字': InitialSkill('技艺:', '打字', 5),
                      '速记': InitialSkill('技艺:', '速记', 5),
                      '歌唱': InitialSkill('技艺:', '歌唱', 5),
                      '制陶': InitialSkill('技艺:', '制陶', 5),
                      '雕塑': InitialSkill('技艺:', '雕塑', 5),
                      '杂技': InitialSkill('技艺:', '杂技', 5),
                      '风水': InitialSkill('技艺:', '风水', 5),
                      '木匠': InitialSkill('技艺:', '木匠', 5),
                      '莫里斯舞蹈': InitialSkill('技艺:', '莫里斯舞蹈', 5),
                      '粉刷/油漆工': InitialSkill('技艺:', '粉刷/油漆工', 5),
                      '锻造': InitialSkill('技艺:', '锻造', 5),
                      '乐器': InitialSkill('技艺:', '乐器', 5),
                      '无': InitialSkill('无', '', 0)}
fighting_initial_skills = {'鞭子': InitialSkill('格斗:', '鞭子', 5),
                           '电锯': InitialSkill('格斗:', '电锯', 10),
                           '斧': InitialSkill('格斗:', '斧', 15),
                           '剑': InitialSkill('格斗:', '剑', 20),
                           '绞索': InitialSkill('格斗:', '绞索', 15),
                           '链枷': InitialSkill('格斗:', '链枷', 10),
                           '矛': InitialSkill('格斗:', '矛', 20),
                           '无': InitialSkill('无', '', 0)}
firearms_initial_skills = {'步枪/霰弹枪': InitialSkill('射击:', '步枪/霰弹枪', 25),
                           '冲锋枪': InitialSkill('射击:', '冲锋枪', 15),
                           '弓术': InitialSkill('射击:', '弓术', 15),
                           '火焰喷射器': InitialSkill('射击:', '火焰喷射器', 10),
                           '机枪': InitialSkill('射击:', '机枪', 10),
                           '重武器': InitialSkill('射击:', '重武器', 10),
                           '无': InitialSkill('无', '', 0)}
language_initial_skills = {'英语': InitialSkill('语言:', '英语', 1),
                           '汉语': InitialSkill('语言:', '汉语', 1),
                           '日语': InitialSkill('语言:', '日语', 1),
                           '拉丁语': InitialSkill('语言:', '拉丁语', 1),
                           '阿拉伯语': InitialSkill('语言:', '阿拉伯语', 1),
                           '法语': InitialSkill('语言:', '法语', 1),
                           '西班牙语': InitialSkill('语言:', '西班牙语', 1),
                           '葡萄牙语': InitialSkill('语言:', '葡萄牙语', 1),
                           '德语': InitialSkill('语言:', '德语', 1),
                           '斯拉夫语': InitialSkill('语言:', '斯拉夫语', 1),
                           '希伯来语': InitialSkill('语言:', '希伯来语', 1),
                           '梵语': InitialSkill('语言:', '梵语', 1),
                           '朝鲜语': InitialSkill('语言:', '朝鲜语', 1),
                           '印地语': InitialSkill('语言:', '印地语', 1),
                           '藏语': InitialSkill('语言:', '藏语', 1),
                           '蒙古语': InitialSkill('语言:', '蒙古语', 1),
                           '无': InitialSkill('无', '', 0)}
mother_language_initial_skill = {'英语': InitialSkill('母语:', '英语', 1),
                                 '汉语': InitialSkill('母语:', '汉语', 1),
                                 '日语': InitialSkill('母语:', '日语', 1),
                                 '拉丁语': InitialSkill('母语:', '拉丁语', 1),
                                 '阿拉伯语': InitialSkill('母语:', '阿拉伯语', 1),
                                 '法语': InitialSkill('母语:', '法语', 1),
                                 '西班牙语': InitialSkill('母语:', '西班牙语', 1),
                                 '葡萄牙语': InitialSkill('母语:', '葡萄牙语', 1),
                                 '德语': InitialSkill('母语:', '德语', 1),
                                 '斯拉夫语': InitialSkill('母语:', '斯拉夫语', 1),
                                 '希伯来语': InitialSkill('母语:', '希伯来语', 1),
                                 '梵语': InitialSkill('母语:', '梵语', 1),
                                 '朝鲜语': InitialSkill('母语:', '朝鲜语', 1),
                                 '印地语': InitialSkill('母语:', '印地语', 1),
                                 '藏语': InitialSkill('母语:', '藏语', 1),
                                 '蒙古语': InitialSkill('母语:', '蒙古语', 1),
                                 '无': InitialSkill('无', '', 0)}
pilot_initial_skills = {'飞行器': InitialSkill('驾驶:', '飞行器', 1),
                        '船': InitialSkill('驾驶:', '船', 1),
                        '无': InitialSkill('无', '', 0)}
science_initial_skills = {'地质学': InitialSkill('科学:', '地质学', 1),
                          '化学': InitialSkill('科学:', '化学', 1),
                          '生物学': InitialSkill('科学:', '生物学', 1),
                          '数学': InitialSkill('科学:', '数学', 1),
                          '天文学': InitialSkill('科学:', '天文学', 1),
                          '物理学': InitialSkill('科学:', '物理学', 1),
                          '药学': InitialSkill('科学:', '药学', 1),
                          '植物学': InitialSkill('科学:', '植物学', 1),
                          '动物学': InitialSkill('科学:', '动物学', 1),
                          '密码学': InitialSkill('科学:', '密码学', 1),
                          '工程学': InitialSkill('科学:', '工程学', 1),
                          '气象学': InitialSkill('科学:', '气象学', 1),
                          '司法科学': InitialSkill('科学:', '司法科学', 1),
                          '无': InitialSkill('无', '', 0)}
survival_initial_skills = {'荒野': InitialSkill('生存:', '荒野', 10),
                           '沙漠': InitialSkill('生存:', '沙漠', 10),
                           '极地': InitialSkill('生存:', '极地', 10),
                           '海洋': InitialSkill('生存:', '海洋', 10),
                           '高山': InitialSkill('生存:', '高山', 10),
                           '孤岛': InitialSkill('生存:', '孤岛', 10),
                           '原始森林': InitialSkill('生存:', '原始森林', 10),
                           '废土': InitialSkill('生存:', '废土', 10),
                           '沼泽': InitialSkill('生存:', '沼泽', 10),
                           '无': InitialSkill('无', '', 0)}
special_initial_skills = {'爆破': InitialSkill('罕见:', '爆破', 1),
                          '催眠': InitialSkill('罕见:', '催眠', 1),
                          '读唇': InitialSkill('罕见:', '读唇', 1),
                          '炮术': InitialSkill('罕见:', '炮术', 1),
                          '潜水': InitialSkill('罕见:', '潜水', 1),
                          '驯兽': InitialSkill('罕见:', '驯兽', 5),
                          '无': InitialSkill('无', '', 0)}
knowledge_initial_skills = {'梦学问': InitialSkill('学问:', '梦学问', 1),
                            '死灵之书学问': InitialSkill('学问:', '死灵之书学问', 1),
                            'UFO学问': InitialSkill('学问:', 'UFO学问', 1),
                            '吸血鬼学问': InitialSkill('学问:', '吸血鬼学问', 1),
                            '佛教学问': InitialSkill('学问:', '佛教学问', 1),
                            '道教学问': InitialSkill('学问:', '道教学问', 1),
                            '神道教学问': InitialSkill('学问:', '神道教学问', 1),
                            '阴阳道学问': InitialSkill('学问:', '阴阳道学问', 1),
                            '狼人学问': InitialSkill('学问:', '狼人学问', 1),
                            '亚迪斯星人学问': InitialSkill('学问:', '亚迪斯星人学问', 1),
                            '都市传说学问': InitialSkill('学问:', '都市传说学问', 1),
                            '中国鬼怪学问': InitialSkill('学问:', '中国鬼怪学问', 1),
                            '无': InitialSkill('无', '', 0)}

initial_skills_dict = {'会计': InitialSkill('会计', '', 5),
                       '人类学': InitialSkill('人类学', '', 1),
                       '估价': InitialSkill('估价', '', 5),
                       '考古学': InitialSkill('考古学', '', 1),
                       '技艺#1': art_initial_skills,
                       '技艺#2': art_initial_skills,
                       '技艺#3': art_initial_skills,
                       '魅惑': InitialSkill('魅惑', '', 15),
                       '攀爬': InitialSkill('攀爬', '', 20),
                       '计算机使用 Ω': InitialSkill('计算机使用 Ω', '', 5),
                       '信用评级': InitialSkill('信用评级', '', 0),
                       '克苏鲁神话': InitialSkill('克苏鲁神话', '', 0),
                       '乔装': InitialSkill('乔装', '', 5),
                       '闪避': InitialSkill('闪避', '', 0),
                       '汽车驾驶': InitialSkill('汽车驾驶', '', 20),
                       '电气维修': InitialSkill('电气维修', '', 10),
                       '电子学 Ω': InitialSkill('电子学 Ω', '', 1),
                       '话术': InitialSkill('话术', '', 5),
                       '格斗:斗殴': InitialSkill('格斗:', '斗殴', 25),
                       '格斗#2': fighting_initial_skills,
                       '格斗#3': fighting_initial_skills,
                       '射击:手枪': InitialSkill('射击:', '手枪', 20),
                       '射击#2': firearms_initial_skills,
                       '射击#3': firearms_initial_skills,
                       '急救': InitialSkill('急救', '', 30),
                       '历史': InitialSkill('历史', '', 5),
                       '恐吓': InitialSkill('恐吓', '', 15),
                       '跳跃': InitialSkill('跳跃', '', 20),
                       '语言#1': language_initial_skills,
                       '语言#2': language_initial_skills,
                       '语言#3': language_initial_skills,
                       '母语': mother_language_initial_skill,
                       '法律': InitialSkill('法律', '', 5),
                       '图书馆使用': InitialSkill('图书馆使用', '', 20),
                       '聆听': InitialSkill('聆听', '', 20),
                       '锁匠': InitialSkill('锁匠', '', 1),
                       '机械维修': InitialSkill('机械维修', '', 10),
                       '医学': InitialSkill('医学', '', 1),
                       '自然学': InitialSkill('自然学', '', 10),
                       '导航': InitialSkill('导航', '', 10),
                       '神秘学': InitialSkill('神秘学', '', 5),
                       '操作重型机械': InitialSkill('操作重型机械', '', 1),
                       '说服': InitialSkill('说服', '', 10),
                       '驾驶': pilot_initial_skills,
                       '精神分析': InitialSkill('精神分析', '', 1),
                       '心理学': InitialSkill('心理学', '', 10),
                       '骑术': InitialSkill('骑术', '', 5),
                       '科学#1': science_initial_skills,
                       '科学#2': science_initial_skills,
                       '科学#3': science_initial_skills,
                       '妙手': InitialSkill('妙手', '', 10),
                       '侦察': InitialSkill('侦察', '', 25),
                       '潜行': InitialSkill('潜行', '', 20),
                       '生存#1': survival_initial_skills,
                       '生存#2': survival_initial_skills,
                       '游泳': InitialSkill('游泳', '', 20),
                       '投掷': InitialSkill('投掷', '', 20),
                       '追踪': InitialSkill('追踪', '', 10),
                       '罕见': special_initial_skills,
                       '学问': knowledge_initial_skills}
initial_skills_list = list(initial_skills_dict.values())
