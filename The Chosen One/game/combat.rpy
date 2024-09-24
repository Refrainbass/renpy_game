label combat_start:

    # dice random values
    label dice_roll:
    $ d2 = renpy.random.randint(1,2)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(2,6)

# the intro before the fight, start by showing the character and play music
show hunter at right
stop music fadeout 0.2
play music "audio/combat.mp3" volume 0.5




# Player Stats
$ player_max_hp = d2 + d4 + d6 + 3
$ player_hp = player_max_hp

#Enemy  Stats
$ enemy_max_hp = d4 + d6 + d10
$ enemy_hp = enemy_max_hp

"Enemy hp is [enemy_max_hp]"
"Player hp is [player_max_hp]"

while player_hp > 0:   
#player turn
    $ random = d4
    menu:
        "Light Attack":
            $ player_attack_value = 5
            $ enemy_hp -= player_attack_value
            "The enemy took [player_attack_value] damage and now at [enemy_hp]"
        "Heavy Attack":
            if random == 1:
                $ player_attack_value = 8
                $ enemy_hp -= player_attack_value
                "The enemy took [player_attack_value] damage and now at [enemy_hp]"
            elif random == 2:
                $ player_attack_value = 7
                $ enemy_hp -= player_attack_value
                "The enemy took [player_attack_value] damage and now at [enemy_hp]"
            elif random == 3:
                $ player_hp -= 3
                "Took 3 damage for attacking too hard!"
            elif random == 4:
                $ player_hp -= 4
                "Took 4 damage for attacking too hard!"

           


    #enemy turn and what will happen when player win
    if player_hp >= 1:
        $ player_hp -= 3
        "Enemy hit player for [3] damage and now you have [player_hp]"
    if enemy_hp <= 0:
        jump scene_2
        
        
    #fight end when player die
    if player_hp <= 0:
        stop music fadeout 0.2
        show black 
        with fade
        "You died"
        "You could have made better dicision to avoid this"
        "Ending 2: Death"
        return


    
  


    


    


