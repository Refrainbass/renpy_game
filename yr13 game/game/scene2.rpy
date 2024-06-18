define girl = Character("Girl", color="#FF0000")
define m = Character("Me", color="#0000FF")
image girl = "girl.png"



label combat_warm:
            g "Well well well"
            g "That's the wrong answer"
            g "I don't like working with people like you"
            g "Time to fight"
            m "Wait wait wait."
            jump combat_2



label scene_3:
            "What you want to do next"
           
            menu:
                        "Go out and look around":
                                    show bg town1 with dissolve
                                    m "Time to look around"
                                    jump scene_4


                        "Sit in room and wait for an hour":
                                    "One hour passed"
                                    show bg hotelm with dissolve
                                    show bg white 
                                    show giga at right 
                                    g "Well well well"
                                    g "Look like someone is wasting his time"
                                    m "I have nothing else better to do anyway"
                                    g "Lazy!!!"
                                    g "YOU ARE VERY LAZY.."
                                    g "and you will get what you deserved"
                                    jump ending_5
                                    



label scene_4:
            "You started to walk around for no reason"
            "Suddenly you found a person look familiar."
            "You decided to go up and talk to her."
            m "Hi"
            show girl with dissolve
            girl "Who are you"
            girl "I don't know you"
            menu:
                        "Say she looks like someone you know":
                                    m "You just look like someone I know"
                                    girl "Then?"
                                    girl "Why you stop me"
                                    m "Nothing"
                                    girl "then move"
                                    hide girl with dissolve
                                    "She walked away"

                        "Just apologise and leave.":
                                    m "Sorry, wrong person"
                                    girl "Don't waste my time"
                                    "She walked away"

"You look at the clock tower and it is nearly the meet up time"
"You decided to go back to the hotel and wait for her"
show bg village1 with dissolve
"You see she is outside waiting for you"
show hunter at right with dissolve
h "What take you so long?"
m "I was just walking in the town"
h "Be on time "
h "What do you want to do next?"
h "Continue the advanture with me?"
h "Or we are on our own now."
h "I am not in a hurry anyway."
h "My village is gone and I am not planning on revenage."
h "What about you."
menu:
            "Go on advanture":
                        jump continue_ad

            "Stay in this town":
                        jump ending_6



label continue_ad:
            h "Alright"
            h "Let's go then"
            h "What you want to do? Go to try to beat some mazes?"
            h "There are some mazes with lot of treasures in it."
            m "Yeah, let's go"



return
