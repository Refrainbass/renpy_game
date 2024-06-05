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


                        "Sit in room and wait for an hour":
                                    "One hour passed"
                                    show bg hotelm with dissolve


return
