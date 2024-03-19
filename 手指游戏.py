import random

aa = 1
ab = 1
ba = 1
bb = 1
s = 'player'

def di():
    global aa,ab,ba,bb,s
    b = random.randint(1,2)
    while True:
        if b == '1' and aa == 0 or b == '2' and ab == 0:
            b = random.randint(1,2)
        else:
            break
    a = random.randint(1,2)
    while True:
        if a == '1' and ba == 0 or a == '2' and bb == 0:
            a = random.randint(1,2)
        else:
            break
    if b == 1:
        if a == 1:
            aa += ba
        else:
            aa += bb
    else:
        if a == 1:
            ab += ba
        else:
            ab += bb
    print('敌方用',b,'抢了你的',a,'现在的情况是:你的左手是',ba,',你的右手是',bb,'敌方的左手是',aa,',敌方的右手是',ab,sep='',end='\n')
    s = 'player'

def player():
    global aa,ab,ba,bb,s
    while True:
        print('请输入你的要用哪只手(你的左手是',ba,',你的右手是',bb,'),(1代表左，2代表右)：',sep='',end='')
        b = str(input())
        if b == '1' and ba == 0 or b == '2' and bb == 0 or b != '1' and b != '2':
            print('不行！')
        else:
            break
    while True:
        print('请输入你的要碰敌人的那只手(敌方的左手是',aa,',敌方的右手是',ab,'),(1代表左，2代表右)：',sep='',end='')
        a = str(input())
        if a == '1' and aa == 0 or a == '2' and ab == 0 or a != '1' and a != '2':
            print('不行！')
        else:
            break
    a = int(a)
    b = int(b)
    if b == 1:
        if a == 1:
            ba += aa
        else:
            ba += ab
    else:
        if a == 1:
            bb += aa
        else:
            bb += ab
    print('好的,','现在的情况是:你的左手是',ba,',你的右手是',bb,'敌方的左手是',aa,',敌方的右手是',ab,sep='')
    s = 'di'

def look():
    global aa,ab,ba,bb
    if aa > 10:
        aa = 1
    if ab > 10:
        ab = 1
    if ba > 10:
        ba = 1
    if bb > 10:
        bb = 1
    
    if aa == 10:
        aa = 0
    if ab == 10:
        ab = 0
    if ba == 10:
        ba = 0
    if bb == 10:
        bb = 0

while True:
    if s == 'player':
        player()
    else:
        di()
    look()
    if aa == 0 and ab == 0:
        input('你输了！')
        break
    elif ba == 0 and bb == 0:
        input('你赢了！')
        break
