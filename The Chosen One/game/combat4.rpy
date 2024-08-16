label combat_4:
    
    label dice_roll4:
    $ d2 = renpy.random.randint(1,2)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    $ d30 = renpy.random.randint(2,6)

stop music fadeout 0.2
play music "audio/combat.mp3" volume 0.3




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
                        $ player_attack_value = 50
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 2:
                        $ player_attack_value = 60
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif random4 == 3:
                        $ player_hp -= 50
                        "Took 50 damage for flexing too hard!"
                    elif random4 == 4:
                        $ player_hp -= 60
                        "Took 60 damage for flexing too hard!"
                "Front double biceps":
                    if d20 >= 15:
                        $ player_attack_value = 999
                        $ enemy_hp -= player_attack_value
                        "The enemy took [player_attack_value] damage and now at [enemy_hp]"
                    elif d20 <= 15:
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




    
        
    image smol_ame:
        "smol_ame/out-transparent-35-0.png"
        pause 0.1
        "smol_ame/out-transparent-35-1.png"
        pause 0.1
        "smol_ame/out-transparent-35-2.png"
        pause 0.1
        "smol_ame/out-transparent-35-3.png"
        pause 0.1
        "smol_ame/out-transparent-35-4.png"
        pause 0.1
        "smol_ame/out-transparent-35-5.png"
        pause 0.1
        "smol_ame/out-transparent-35-6.png"
        pause 0.1
        "smol_ame/out-transparent-35-7.png"
        pause 0.1
        "smol_ame/out-transparent-35-8.png"
        pause 0.1
        "smol_ame/out-transparent-35-9.png"
        pause 0.1
        "smol_ame/out-transparent-35-10.png"
        pause 0.1
        "smol_ame/out-transparent-35-11.png"
        pause 0.1
        "smol_ame/out-transparent-35-12.png"
        pause 0.1
        "smol_ame/out-transparent-35-13.png"
        pause 0.1
        "smol_ame/out-transparent-35-14.png"
        pause 0.1
        "smol_ame/out-transparent-35-15.png"
        pause 0.1
        "smol_ame/out-transparent-35-16.png"
        pause 0.1
        "smol_ame/out-transparent-35-17.png"
        pause 0.1
        "smol_ame/out-transparent-35-18.png"
        pause 0.1
        repeat

    if player_hp <= 0:
        stop music fadeout 0.2
        show black 
        with fade
        "You died"
        "You could have made better dicision to avoid this"
        "Ending 2: Death"
        return

    
    
    if enemy_hp <= 8700:
        jump smol_ameroll

label smol_ameroll:
    g "Nah this is taking too long."
    stop music fadeout 0.2
    play music "audio/amebgm.mp3"
    g "It's your show time."
    show smol_ame with moveintop
    play sound "audio/ame.mp3"
    "She ground pound your mum."
    "But you win so it doesn't matter"
    hide monster with moveoutbottom
    monster "I will be back...."
    $ player_hp -= 999999
    $ enemy_hp -= 999999
    "Both of you are seriously damaged by smol ame."
    g "Ok I guess it is gone now."
    g "Time to go."
    g "Let's go smol ame"
    play sound "audio/ame.mp3"
    hide smol_ame with moveoutleft 
    g "Well, time is up."
    g "We will meet again."
    hide smolgiga with moveouttop 
    "The heros went back to where they belong."
    

    
        
    
        


    
  


    


    


