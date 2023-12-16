class Player:

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        if damage > self.defense:
            self.health -= damage - self.defense
            return f'{self.name}受到了{damage}點傷害'
        else:
            return f'{self.name}成功抵擋攻擊'


class Mage(Player):

    def __init__(self, name, health, attack, defense, magic_power,
                 magic_attack):
        super().__init__(name, health, attack, defense)
        self.magic_attack = magic_attack
        self.magic_power = magic_power

    def cast_spell(self):
        self.magic_power -= 10
        return self.attack + self.magic_attack


class Warrior(Player):

    def __init__(self, name, health, attack, defense, armor):
        super().__init__(name, health, attack, defense)
        self.armor = armor

    def use_armor(self):
        self.health += self.armor
        self.armor = 0


# player1 = Player('韭菜', 100, 2, 9)
# print(f'玩家名稱:{player1.name}')
# print(f'玩家血量:{player1.health}')
# print(f'玩家攻擊:{player1.attack}')
# print(f'玩家防禦:{player1.defense}')

# player2 = Player('高麗菜', 50, 10, 5)
# print(f'玩家名稱:{player2.name}')
# print(f'玩家血量:{player2.health}')
# print(f'玩家攻擊:{player2.attack}')
# print(f'玩家防禦:{player2.defense}')

player1 = Warrior("戰士小明", 100, 15, 10, 5)  # 裡面包含了Player的物件，所以可以使用Player的方法
player2 = Mage("法師小華", 80, 10, 5, 20, 20)

print(f"{player1.name}血量剩餘: {player1.health}")
player1.use_armor()
print(f"{player1.name}血量剩餘: {player1.health}")

print(f"{player2.name}目前魔力: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對{player1.name}施放魔法攻擊！")
print(f"{player2.name}目前魔力: {player2.magic_power}")
print(f"{player1.name}血量剩餘: {player1.health}")