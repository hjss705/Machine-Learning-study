import random

def calc_speed(BMW,KIA):
    speed = BMW and KIA /1000
    if speed < 0.05: return "느림"
    if speed < 0.15: return "보통"
    return "빠름"

fp = open("speed.csv","w",encoding="utf-8")
fp.write('BMW,KIA,label\r\n')

cnt = {'느림':0, '보통':0,'빠름':0}
for i in range(10000):
    BMW = random.randint(0,250)
    KIA = random.randint(0,200)
    label = calc_speed(BMW,KIA)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(BMW,KIA,label))
fp.close()
print('ok',cnt)