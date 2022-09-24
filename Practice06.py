# class
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp


class AttackObj(Unit):
    # 기존과 달리 생성자로 들어가는 파라미터의 수가 감소한다.
    def __init__(self, damage):
        self.damage = damage


class Flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{0} : {1} fly".format(name, self.speed))


# 다중 상속 클래스
class FlyableAttackObj(AttackObj, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackObj.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)

# super
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp


class Building(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location