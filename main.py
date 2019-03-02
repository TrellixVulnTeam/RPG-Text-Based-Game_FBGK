
from person import Person #in another file
from magic import Magic
import random

#MAGIC
Fire = Magic("Fire", 10, 30, "dark")
Tornado = Magic("Tornado", 15, 50, "dark")
Ice = Magic("Ice", 20, 70, "dark")

magic_list = [Fire, Tornado, Ice]#example of clean code

player = Person("Legolas", 1200, 500, 400, magic_list)
enemy = Person("Saruman", 1000, 700, 600, magic_list)

print("This is the instruction....")
print("\n")
print("--------------------------------")
player.get_stats()#calling method show player stats
print("--------------------------------")
enemy.get_stats()
print("--------------------------------")

print("\n")

running = True
while running:

  print(player.name)
  print("Player attacks first!") 
  player.choose_action()
  choice = int(input(">>>: "))
  action_index = choice - 1
  if action_index == 0:
      damage = player.generate_atk_dmg()
      enemy.take_dmg(damage) #call method take_dmg enemy
      print("--------------------------------")
      print(f"You Attacked {enemy.name} and dealt {damage} damage")

  elif action_index == 1:
      player.choose_magic()
      magic_choice = int(input("Choose your magic!"))
      magic_index = magic_choice - 1
      magic = player.magic[magic_index]
      magic_damage = magic.generate_damage()
      magic_name = magic.name
      magic_cost = magic.mp_cost
      #damage is the standalone variable
  else:
    print("Choose a correct number")
    continue
    
    print("--------------------------------")

    enemy.take_dmg(magic_damage)
    print(f"You Attacked with {magic_name} {enemy.name} and dealt {magic_damage} points of damage")


  #ENEMY TURN

  print("Enemy's turn now")
  enemy_choice = 0
  if enemy_choice == 0:
    enemy_damage = enemy.generate_atk_dmg()
    player.take_dmg(enemy_damage)#call method take_dmg player
    
    print(f"{enemy.name} attacked {player.name} and dealt {damage} damage")

#choose action = input("Choose Action") #enemy starts, choosing action (attack). input
   #call method generate_dmg enemy
  

#print out new stats of player and enemy
    print("\n")
    print("--------------------------------")
    player.get_stats()#calling method show player stats
    print("--------------------------------")
    enemy.get_stats()
    print("--------------------------------")

    print("\n")

#check damage
    if player.hp == 0:
      print("You lost!!!")
      running = False
    elif enemy.hp == 0:
      print("Enemy Lost!!!")
      running = False
    #break
    #elif player or enemy self.hp > 0
    #ctn = True
#if hp player == 0, elif hp enemy == 0, break(lost)
#Loop
