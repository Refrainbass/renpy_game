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
                                    jump ending_6
                                    



label scene_4:
            "You started to walk around for no reason"
            "Suddenly you found a person look familiar from the city you from"
            "You decided to go up and talk to her."
            m "Hi"
            show girl with dissolve
            girl "Who are you"
            girl "I don't know you"
            menu:
                        "Say she looks like someone you know":
                                    m "You just look like someone I know"

                        "Just apologise and leave.":
                                    m "Sorry, wrong person"





return
