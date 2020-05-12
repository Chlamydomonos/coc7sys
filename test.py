from GameSystem.Profession import *
import pickle
a = Profession('杂技演员',
               SkillPoints(0, 0, 0, 2, 0, 0, 0, 2), [9, 20], 2, [],
               ['攀爬', '闪避', '跳跃', '投掷', '侦察', '游泳'])
f = open('ProfessionList\\' + a.name + '.pfs', 'wb')
g = open('ProfessionIntroductions\\' + a.name + '.itd', 'w')
g.write('杂技演员可能是参加各级比赛(甚至奥运会)的业余运动员，也可能是专业的演员，在马戏团、嘉年华、歌舞团之类的地方作为娱乐业从业者工作。')
pickle.dump(a, f)
