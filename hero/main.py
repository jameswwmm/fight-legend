from hero import hero_info
myhero = hero_info.HeroBase(100,10,0,8,
                            0,4,0,None,None,None
                            ,0)
fi = myhero.fight()
print(fi)
print("接受之前的体力值",myhero.stamina)
myhero.rececived_damge(10,0)
print("接受之后的体力值",myhero.stamina)
