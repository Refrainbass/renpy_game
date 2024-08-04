#the start of advanture
label adventure_1:
      hide hunter
      show bg forest with fade
      "After leaving the town and decided to go on an adventure with a hunter."
      "All you see are trees, start off at sun above to where you can't see the sun again"

      show bg dark forest with fade
      stop music fadeout 0.2
      play music "audio/moonlight.mp3" volume 5.0
      show hunter at right 
      m "Where exactly we are going?"
      h "We are going to a city call Lafu, a city with many dungeons nearby."
      h "It is known for the start point of some legendary advantures."
      h "You ever heard of a person solo a T5 dungeons on his own?"
      
      label loop_2:
            menu:
                  "What is a T5 dungeon?":
                              h "Dungeons are divided by tiers, Tier 1 is the easiest and Tier 5 is the hardest."
                              jump continue_2

                  "Who is that person?":
                              h "No one know who that person is, 0 information about that person."
                              h "That person is one of the best adventurer, have the power to destorying anything he want, anytime he want."
                              h "He did that just for fun, that's all I know."
                              m "For fun?"
                              h "Yes, for fun and he did that on his own."
                              h "Usually a T5 need at least 5 people with very good teamwork to beat it. At that case can't even ensure getting out as a full squad."
                              jump continue_2



label continue_2:
      h "What else you want to know?"
      menu:
            "I want to know about..":
                  jump loop_2

            "No that's all":
                  h "Alright then"
                  "You continue walking"
                 

show wolf at center with dissolve
m "Why this dog so ugly"
h "That's a wolf you idiot."
h "This is normal, forest always full of unexpected monsters. "
h "I guess we have no choice but fight"
jump combat_3

label beatwolf:
      h "That's was easy."


  