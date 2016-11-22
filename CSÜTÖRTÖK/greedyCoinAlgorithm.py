import random
szazas,tizes,egyes = 0,0,0
for i in range(0,1):
    rnd = random.randint(0,666)
    print(rnd)
    szazas=rnd//100
    print(szazas)
    tizes=(rnd-szazas*100)//10
    print(tizes)
    egyes = rnd-szazas*100-tizes*10
    print(egyes)