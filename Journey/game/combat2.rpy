label combat_2:

    label dice_roll_2:
    $ d2 = renpy.random.randint(1,2)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(2,6)

show giga at right
stop music fadeout 0.2
play music "audio/combat.mp3" volume 0.5



# Player Stats
$ player_max_hp = 100
$ player_hp = player_max_hp

#Enemy  Stats
$ enemy_max_hp = 1000
$ enemy_hp = enemy_max_hp

"Enemy hp is [enemy_max_hp]"
"Player hp is [player_max_hp]"

while player_hp > 0:   
#player turn
    
    label attacks:
        menu:
            "Light Attack":
                $ player_attack_value = 15
                $ enemy_hp -= player_attack_value
                "The enemy took [player_attack_value] damage and now at [enemy_hp]"
            "Heavy Attack":
                if d20 >= 7:
                    $ player_attack_value = 30
                    $ enemy_hp -= player_attack_value
                    "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                else:
                    $ player_hp -= 4
                    "You took 4 damage for attacking too hard and now at [player_hp]"
            "Heal":
                    jump heal

  
    if player_hp >= 1:
        $ player_hp -= 25
        "Enemy hit player for 25 damage and now you have [player_hp]"
    if enemy_hp <= 0:
        jump won_giga
        
        

    if player_hp <= 0:
        stop music fadeout 0.2
        show black 
        with fade
        "You died"
        "You could have made better dicision to avoid this"
        "Ending 2: Death"
        return

label heal:
        menu:
            "Push up":
                if d2 == 2:
                    $ player_hp += 10
                    "You do some pushups to heal, health + 10"
                    " You are at [player_hp] "
                    jump attacks
                else:
                    $ player_hp -= 15
                    "You did too much pushups, It hurts, health - 5"
                    " You are at [player_hp] "
                    jump attacks
            
            "Sit up":
                if d2 == 1:
                    $ player_hp += 15
                    "Situp = good = good abs , health + 15"
                    " You are at [player_hp] "
                    jump attacks
                else:
                    $ player_hp -= 25
                    "Abs hurts, health - 25"
                    " You are at [player_hp] "
                    jump attacks

            "No":
                jump attacks    

    
  


    


    


