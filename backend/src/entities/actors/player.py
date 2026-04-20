class PlayerEntity:
    def __init__(self, name, health=100, speed=10, damage=5, id=None):
        self.id = id
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
