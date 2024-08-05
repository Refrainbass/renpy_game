label combat_3:
    
    label dice_roll3:
    $ d2 = renpy.random.randint(1,2)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(2,6)

show hunter at left 
show wolf at right with fade
stop music fadeout 0.2
play music "audio/combat.mp3" volume 0.5




# Player Stats
$ player_max_hp = 70
$ player_hp = player_max_hp

#Enemy  Stats
$ enemy_max_hp = 100
$ enemy_hp = enemy_max_hp

"Enemy hp is [enemy_max_hp]"
"Player hp is [player_max_hp]"

while player_hp > 0:   
#player turn
    $ random3 = d4
    "Choose character to attack:"
    menu:
        "Player":
            menu:
                "Light Attack":
                    $ player_attack_value = 3
                    $ enemy_hp -= player_attack_value
                    "The enemy took [player_attack_value] damage and now at [enemy_hp]"
               
                "Heavy Attack":
                    if random3 == 1:
                        $ player_attack_value = 3
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random3 == 2:
                        $ player_attack_value = 4
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random3 == 3:
                        $ player_hp -= 3
                        "Took 3 damage for attacking too hard!"
                    elif random3 == 4:
                        $ player_hp -= 4
                        "Took 4 damage for attacking too hard!"
            
                
        "Hunter":
            menu:
                "Light Attack":
                    $ player_attack_value = 5
                    $ enemy_hp -= player_attack_value
                    "The enemy took [player_attack_value] damage and now at [enemy_hp]"
               
                "Sword Attack":
                    if random3 == 1:
                        $ player_attack_value = 5
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random3 == 2:
                        $ player_attack_value = 6
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random3 == 3:
                        $ player_hp -= 5
                        "Took 5 damage for attacking too hard!"
                    elif random3 == 4:
                        $ player_hp -= 6
                        "Took 4 damage for attacking too hard!"
                "Epic Attack":
                    if d20 >= 10:
                        $ player_attack_value = 30
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif d20 <= 10:
                        "Nothing happened"



        
        
       
           


    if player_hp >= 1:
        if random3 == 1:
            $ player_hp -= 5
            "Enemy hit player for [5] damage and now you have [player_hp]"
        elif random3 == 2:
            $ player_hp -= 6
            "Enemy hit player for [6] damage and now you have [player_hp]"
        elif random3 == 3:
            $ player_hp -= 7
            "Enemy hit player for [7] damage and now you have [player_hp]"
        elif random3 == 4:
            $ player_hp -= 8
            "Enemy hit player for [8] damage and now you have [player_hp]"   

    if player_hp <= 10:
        menu:
            "Healing" :
                $ player_hp += 10
                "You healed for 10 hp and now have [player_hp]"
            "Risky large healing ":
                if d20 <= 15:
                    $ player_hp -= 20
                    "Failed healing -20 health, now you are at [player_hp]"
                if d20 >= 15:
                    $ player_hp += 20
                    "You healed for 20 hp and now have [player_hp]"


    if enemy_hp <= 0:
        jump beatwolf
        
        

    if player_hp <= 0:
        stop music fadeout 0.2
        show black 
        with fade
        "You died"
        "You could have made better dicision to avoid this"
        "Ending 2: Death"
        return


    
  


    


    


