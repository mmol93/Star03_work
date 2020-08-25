import random

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{}이 1기 생성되었습니다.".format(self.name))
        print("hp : {}, Damage : {}".format(self.hp, self.damage))

    def getDamaged(self):
        global Marine_count
        global j
        random_damage = random.randint(1, 60)
        print("{}이 {}의 데미지를 받았습니다. [남은 체력 : {}]"
              .format(self.name, random_damage, self.hp - random_damage))
        if self.hp - random_damage <= 0:
            print("{}이 죽었습니다".format(self.name))
            j = 1
            Marine_count -= 1
            print("남은 {}은 {}기입니다".format(self.name, Marine_count))

Marine_count = 0    # 해병 유닛 카운터
Marine_Arr = []     # 해병 유닛 리스트



i = 0   #무한 루프
dead_unit = []  #죽은 유닛 리스트
while i < 1:
    Create_unit = input("생성할 유닛 커맨드 입력 : ")

    if Create_unit == "m" or Create_unit == "M":
        Marine_Arr.append(Unit("해병", 40, 5))
        Marine_count += 1
    elif Create_unit == "q":
        break;

# 모든 마린 공격하여 데미지 입기

for attack in Marine_Arr:
    j = 0  # 죽은 유닛 카운트
    attack.getDamaged()
    if j == 1:
        dead_unit.append(attack)

for dead_unit_delete in dead_unit:

    if Marine_count == 0:
        quit()
    Marine_Arr.remove(dead_unit_delete)

while i < 1:
    print("남은 해병은 {}기입니다.".format(Marine_count))
    dead_unit.clear()
    attack_command = input("다시 공격 ㄱㄱ? : ")
    if attack_command == "ok":
        for attack in Marine_Arr:
            j = 0  # 죽은 유닛 카운트
            attack.getDamaged()
            if j == 1:
                dead_unit.append(attack)

        for dead_unit_delete in dead_unit:
            if Marine_count == 0:
                quit()
            Marine_Arr.remove(dead_unit_delete)






