class Warrior():

    def __init__(self,name,power,endurance,hair_color):
        self.name = name
        self.power = int(power)
        self.endurance = int(endurance)
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать ")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого то ")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет ")

    def info(self):
        print(f" имя воина {self.name}")
        print(f" цвет волос воина {self.hair_color}")
        print(f"сила воина {self.power}")
        print(f"выносливость воина {self.endurance} ")

war1 = Warrior("Степа","76","54","коричневый")
war2 = Warrior("Егор","55","76","блондин")

war1.info()
print(war1.endurance)
war1.sleep()
print(war1.endurance)

print(war1.power)
war1.eat()
print(war1.power)

war2.info()
print(war2.power)
war2.eat()
print(war2.power)

print(war2.endurance)
war2.hit()
print(war2.endurance)


