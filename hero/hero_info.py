class HeroBase:
    def __init__(self, name,stamina,attack,attack_percent,
                 extra_attack,defense,defense_percent,speed,skill_1,
                 skill_2,skill_3,skill_3_cool_down):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.attack_percent = attack_percent
        self.defense_percent = defense_percent
        self.speed = speed
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
        self.skill_3_cool_down = skill_3_cool_down
        self.extra_attack = extra_attack

    def fight(self):
        #对自己的
        return self.attack, self.attack_percent #给目标的

    def received_damage(self,attack,attack_percent):
        self.stamina = self.stamina - attack * (100 - self.defense) / 100 - attack_percent



class Gladiator(HeroBase):
    def skill_1(self, target):
        print(f"{self.name}使用技能1:{self.skill_1}")
        target.received_damage(self.attack, 0)

    def skill_2(self, target):
        print(f"{self.name}使用技能2:{self.skill_2}")
        reduced_damage = target.attack * 0.4
        reflected_damage = target.attack * 0.6
        self.received_damage(reduced_damage, 0)
        target.received_damage(reflected_damage, 0)

    def skill_3(self, target):
        print(f"{self.name}使用技能3:{self.skill_3}")
        if target.stamina <= 20:
            target.stamina -= 40
        else:
            target.stamina -= 4#

    def __init__(self,skill_1="普攻",skill_2="反弹",skill_3="终结",#
                 skill_3_cool_down=3,
                 name = "角斗士",
                stamina=100,attack=10,speed=4,defense=8,
                 attack_percent=0,extra_attack=0,
                 defense_percent=0):

        super().__init__(name,stamina,attack,attack_percent,
                         extra_attack,defense,defense_percent,speed,skill_1,
                         skill_2,skill_3,skill_3_cool_down)

class Archer(HeroBase):
    def skill_1(self, target):
        print(f"{self.name}使用技能1:{self.skill_1}")
        target.received_damage(self.attack, 0)

    def skill_2(self, target):
        print(f"{self.name}使用技能2:{self.skill_2}")
        while True:
            damage = self.attack * 0.5 * 3
            break
        target.received_damage(damage, 0)

    def skill_3(self, target):
        print(f"{self.name}使用技能3:{self.skill_3}")
        import random
        damage_list = [0,1,40,5,1,1,2,10,0]
        damage = random.choice(damage_list)
        target.received_damage(damage, 0)
