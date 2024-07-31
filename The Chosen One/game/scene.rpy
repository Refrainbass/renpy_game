label forest_1:
    show hunter at right
    h "Why are you here?"
    h "I thought we killed them all already"
    m "Wait What are you talking about"
    h "Why I have to do all the dirty work?"
    m "Hold up"
    "The hunter clearly didn't care and started pulling out her sword"
    jump combat_start

label scene_2:
    show bg forest
    with fade
    stop music fadeout 0.2
    play music "audio/mainland.mp3" volume 0.5
    h "Who even are you? Why you are so strong"
    
    menu:
        "Tell the truth":
            m "I have no idea."
            m "When I open my eyes"
            m "I am here for some reason"

        "Lie":
            m "I got lost in the forest when I was hunting."
            h "Getting lost? In this kind of time? it can't be true"
            "Proceed to pull out her sword"
            jump ending_3

    h "What do you mean by that?"
    "She stopped and think for a while..."
    "..."
    "..."
    h "Whatever, it doesn't matter now."
    h "I can guide you to the nearby town"
    h "Do you want to come along?"
    
    menu:
        "Yes":
            "You follow her and begin the journey"
        
        "No":
            m "Nah, I am going on my own"
            "You proceed to walk alone in the forest"
            jump ending_4

    "You and the hunter proceed to walk together"
    play music "audio/sonder.mp3" volume 0.5 
    h "Are you new to here?"
    m "Yes, as I said I got sent here for no reason."
    m "At least I don't remember why"
    "She stayed slicene for quite a while"
    "After a while , she said"
    h "Do you have any question for me?"

    menu loop_1:
        "What happened just before I got here":
            h "Umm, it is hard to explain"
            "You decided to stay quiet and don't interrupt her"
            h "In this world, there is a country called The Empire"
            h "They decided to attack my village"
            h "To steal resources and people for the up coming battle"
            h "We decided to fight back and start the fight right in the position you were"
            h "The fight lasted for days and finally ended just now"
            h "I am the only one left and I remembered I killed them all"
            h "I thought you are part of The Empire, that's why I attacked you"
            h "Sorry about that"
            jump continue
            
        "Ask about the the current state of the world":
            h "There are 2 main speices at the moment, at least strong enough to fight against human"
            m "What are those 2"
            h "Elf and human are at the top of the food chain"
            h "Elf ruling the natures"
            h "Human ruling outside the forests"
            h "What make elf powerful is that, they know magic"
            m "Why human can't just learn that"
            h "Because those are written in their language , on top of that the docements are kept within the hands of rulers"
            h "On the other hand , human have nothing to compare to them"
            h "Human are currently in danger, at least until The Empire decided to surrender to them"
            jump continue

        "No":
            "You shake your head"
            h "Are you sure?"
            menu:
                "Yes":
                    jump story_1
                "No, I changed my mind.":
                    jump loop_1


    label continue:
        "Any more questions?"
        menu:
            "Yes":
                jump loop_1

            "No, that's all.":
                "You continue walking "
    
    label story_1:
        "After a while, you finally arrived at the first village"
        show bg sunset village with dissolve 
        "It is a middle-age like village"
        h "It is getting late."
        h "Let's find a place to stay and decide what to do tomorrow."
        m "Sure."
        "You soon arrived at one of the hotel in the town."
        "She quickly booked 2 rooms "
        "and decided to meet up in the lobby at 9 am "
        hide hunter
        show bg hoteln with dissolve
        m "Finally have some time to rest"
        m "After I got here it only been running and fighting"
        m "Time to mark down the information of this world"
        "You grab the pen on the table"
        show bg note with dissolve
        "And start writing down what you have heard and experienced"
        menu:
            "About this world":
                jump notes1
            "About elf":
                jump notes2
            "About what is happening to human":
                jump notes3

    label notes1:
        show bg note1 with dissolve 
        menu:
            "About elf":
                show bg note2 with dissolve
                menu:   
                    "About what is happening to human":
                        show bg note3 with dissolve
                        jump story_2
            "About what is happening to human":
                show bg note7 with dissolve
                menu:
                    "About elf":
                        show bg note8 with dissolve
                        jump story_2
    label notes2:
        show bg note4 with dissolve 
        menu:
            "About this world":
                show bg note5 with dissolve
                menu:   
                    "About what is happening to human":
                        show bg note6 with dissolve
                        jump story_2
            "About what is happening to human":
                show bg note9 with dissolve
                menu:
                    "About this world":
                        show bg note10 with dissolve
                        jump story_2
    label notes3:
        show bg note11 with dissolve 
        menu:
            "About this world":
                show bg note12 with dissolve
                menu:   
                    "About elf":
                        show bg note13 with dissolve
                        jump story_2
            "About elf":
                show bg note14 with dissolve
                menu:
                    "About this world":
                        show bg note15 with dissolve
                        jump story_2
    
    
    
    label story_2:
        show bg hoteln with dissolve
        m "What should I do next..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        menu:
            "Sleep":
                show bg black with dissolve
            "Keep sitting":
                jump story_2

show bg white with dissolve
m "Where am I?"
m "What is this"
who "Haha"
m "Who are you?"
who "Well"
play music "gigachad.mp3"
show giga at right
g "It is me "
m "OMG it is you , Giga chad!!!"
m "What are you doing here??"
g "I come here to give you advice"
g "Well.."
g "You can choose to listen or not"
g "All I can say is , the chad is always right"

label giga1:
        menu:
    
            "Listen to Giga Chad , see what he is cooking.":
                jump continue_giga

            "Nah, he look kind of sus, don't listen to him.":
                jump unsure 


label unsure:
    g "Are you sure you don't want this banger advice?"
    menu:
        "Yes, I don't want it.":
            jump combat_warm

        "Nah, I change my mind.":
            jump giga1

label continue_giga:
    g "Wise choice my brother"
    g "Do 100 push up , pull up and sit up everyday"
    g "Get stronger"
    g "That will help you."
    g "Oh look like you about to wake up"
    g "See you again"
    "Giga chad started to fade out"
    hide giga with dissolve
    stop music fadeout 0.2
    show bg hotelm with dissolve


play music "audio/morning.mp3" volume 0.5
"It is 8am"
"1 hour before meet up time"

jump scene_3
        

        
            


 


return 