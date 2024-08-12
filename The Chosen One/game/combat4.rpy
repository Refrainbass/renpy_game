label combat_4:
    
    label dice_roll4:
    $ d2 = renpy.random.randint(1,2)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(2,6)

stop music fadeout 0.2
play music "audio/combat.mp3" volume 0.5




# Player Stats
$ player_max_hp = 70
$ player_hp = player_max_hp

#Enemy  Stats
$ enemy_max_hp = 9000
$ enemy_hp = enemy_max_hp

"Enemy hp is [enemy_max_hp]"
"Player hp is [player_max_hp]"
g "Don't worry let me add some hp for you."
$ player_hp += 69420
"Player hp is now [player_hp] after the Giga buff."


while player_hp > 0:   
#player turn
    $ random4 = d4
    "Choose character to attack:"
    menu:
        "Player":
            menu:
                "Light Attack":
                    $ player_attack_value = 3
                    $ enemy_hp -= player_attack_value
                    "The enemy took [player_attack_value] damage and now at [enemy_hp]"
               
                "Heavy Attack":
                    if random4 == 1:
                        $ player_attack_value = 3
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 2:
                        $ player_attack_value = 4
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 3:
                        $ player_hp -= 3
                        "Took 3 damage for attacking too hard!"
                    elif random4 == 4:
                        $ player_hp -= 4
                        "Took 4 damage for attacking too hard!"
            
                
        "Giga":
            menu:
                "Skull crushers":
                    $ player_attack_value = 50
                    $ enemy_hp -= player_attack_value
                    "The enemy took [player_attack_value] damage and now at [enemy_hp]"
               
                "Lat spread":
                    if random4 == 1:
                        $ player_attack_value = 5
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 2:
                        $ player_attack_value = 6
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 3:
                        $ player_hp -= 5
                        "Took 5 damage for flexing too hard!"
                    elif random4 == 4:
                        $ player_hp -= 6
                        "Took 4 damage for flexing too hard!"
                "Front double biceps":
                    if d20 >= 10:
                        $ player_attack_value = 999
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif d20 <= 10:
                        "Nothing happened, I guess he like the moon pose more."



        
        
       
           


    if player_hp >= 1:
        if random4 == 1:
            $ player_hp -= 50
            "Enemy hit player for [50] damage and now you have [player_hp]"
        elif random4 == 2:
            $ player_hp -= 65
            "Enemy hit player for [65] damage and now you have [player_hp]"
        elif random4 == 3:
            $ player_hp -= 72
            "Enemy hit player for [72] damage and now you have [player_hp]"
        elif random4 == 4:
            $ player_hp -= 81
            "Enemy hit player for [81] damage and now you have [player_hp]"   

    if player_hp <= 200:
        menu:
            "Healing" :
                $ player_hp += 16
                "You healed for 16 hp and now have [player_hp]"
            "Risky large healing ":
                if d20 <= 15:
                    $ player_hp -= 99
                    "Failed healing -99 health, now you are at [player_hp]"
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

    image smol_ame = Movie(play = "image/smolame.mp4")

    
    if enemy_hp <= 5500:
        jump smol_ameroll

    label smol_ameroll:
        g "Nah this is taking too long."
        g "It's your show time."
        show smol_ame 
        
    
        


    
  


    


    


