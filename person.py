import random

class Person():
    def __init__(self, name, hp, mp, atk, magic):
        self.name = name  
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.magic = magic
        self.action = ["Physical Attack", "Magic"]

    def get_stats(self):
        print(self.name)
        print(f"HP {self.hp} / MAX HP {self.max_hp}")
        print(f"MP {self.mp} / MAX MP {self.max_mp}")
    # This method should return a damage value
    # The value is a random number between atk_low and atk_high

    def generate_atk_dmg(self):#from self can access all of the above
        damage = random.randrange(self.atk_low, self.atk_high)
        return damage

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
     #   new_hp = self.hp - dmg
      #  return new_hp 
      #  print(self.action)

    def choose_action(self):
        index = 1
        print("ACTIONS:")
        for element in self.action:
            print(f"{index},{element}")
        index = index + 1
    #pass

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        if self.mp < used_mp:
            print("Not enough Mana!!!")
        return self.mp

    def choose_magic(self):
        number = 1
        print("\t\t Choose Magic:")
        for element in self.magic:
            print(f"\t\t {number}. {element.name}")
            number = number + 1