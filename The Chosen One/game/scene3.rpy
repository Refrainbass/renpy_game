#the start of advanture
label adventure_1:
      "After leaving the town and decided to go on an adventure with a hunter."
      show bg dark forest with fade
      show hunter at right 
      m "Where exactly we are going?"
      h "We are going to a city call Lafu, a city with many dungeons nearby."
      h "It is known for the start point of some legendary advantures."
      h "You ever heard of a person solo a T5 dungeons on his own?"
      
      label loop_2:
            menu:
                  "What is a T5 dungeon?":
                              m "What is a T5 dungeon?"
                              h "Dungeons are divided by tiers, Tier 1 is the easiest and Tier 5 is the hardest."
                              jump continue_2

                  "Who is that person?":
                              m "Who is that person?"



label continue_2:


  