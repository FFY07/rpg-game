class Person():
    def __init__(self, name = "Tom", job: str = "Unemployed"):
        self.name = name
        self.job = job
        self.money = 1000
        self.girlfriend = None
        self.boyfriend = None
        self.alive = True
    def make_money(self, amount):
        self.money += amount

    def kill(self, target):
        target.alive = False
        print(self.name, 'kill', target.name)

    def revive(self):
        self.alive = True
        print(self.name, 'become jesus')

guy = Person('Trump', 'Wall Builder')
girl = Person('Linda', 'Porsche Driver')

# guy.kill(girl)

# print(girl.alive)


class Child(Person):
    def __init__(self, name = "Jesus", job = 'student'):
        super().__init__(name, job)
    
    def crawl(self):
        print(self.name, "is crawling")


baby = Child('babi')

print(baby.name, baby.job)


baby.crawl()
baby.kill(guy)

