#the start of advanture
label adventure_1:
      hide hunter
      show bg forest with fade
      "After leaving the town and decided to go on an adventure with a hunter."
      "All you see are trees, start off at sun above to where you can't see the sun again"

      show bg dark forest with fade
      stop music fadeout 0.2
      play music "audio/moonlight.mp3" volume 1.5 #music
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
#loop menu 


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
jump combat_3 #start of combat

image bg campfire = "campfire.png"
image monster = "monster.png"
define monster = Character("A̵̡̱̠͕̖̰̻͌͌̾͒͋s̸̖̎̆̑̽̒͌̈̽͌̕ȧ̴̛̮̭̓͗́̋̈͝n̷̡̤̣̘͙̩̳̠͐̊̎̎̚̚̕ã̴̙͓̠̲̪̜̿̎̅̈́̕͜͝͠ḧ̴͇͕͖̬͎̝̳̹̒́̅̑̿̌̈́͊̕k̶̛̭̗̬̹̖̐́͐ç̵̗̙͎͑͂̀̈́̈́", color="#FF0000")
label beatwolf:
      hide wolf with fade
      play music "audio/moonlight.mp3"
      h "That's was easy."
      m "Nah It was not easy, let me catch my breath for a bit."
      h "Yeah that is a good idea"
      h "It is getting late as well"
      h "We probably find a place to camp nearby to get through the night and continue tomorrow."
      h "There is a place overthere, let's camp there."
      show bg campfire with fade 
      h "Have a good rest and we begin our journey again tomorrow."
      m "Is that safe to rest in places like this?"
      h "I did check around this place and I don't think there is any monsters nearby."
      h "Even if there is , I will deal with it."
      m "Alright then"
      hide hunter
      stop music fadeout 0.5
      show bg black with fade 
      "You fell asleep"
      play sound "audio/wind.mp3" volume 0.75
      "..."
      "..." 
      "Can't sleep well with the amount of wind"
      "You wake up"
      jump monster_start      

image smolgiga = "smolgiga.png" 
label monster_start:
            show bg campfire with dissolve
            "You don't see her"
            "She is not around"
            "You get up to see where she at."
            "You see a shadow "
            "But that's not what you excepted"
            show bg black 
            show monster  with fade
            monster "Your time is up"
            monster "You need to pay for what you have done"
            g "No No No , Not so quick."
            monster "Who even are you"
            g "Well"
            play music "audio/gigachad.mp3"
            show monster at left
            show smolgiga at right with fade 
            m "OMG is you chad"
            g "Well we meet again"
            m "Why you are smol chad now"
            g "Well, I lost some of my power in the last fight with 'you'."
            m "ME?"
            g "You know who I am talking to."
            g "Shall we begin?"
            g "This will be a tough fight"
            jump combat_4 #start of combat

image wood = "wood.png"
label continue_3:
      show bg campfire with dissolve
      stop music fadeout 0.5
      play music "audio/moonlight.mp3"
      "You opened your eyes and end up in the same place."
      "Same campfire."
      "You got up and want to see where she is."
      "Still don't see her"
      m "What should I do now?"
      h "What are you doing?"
      show hunter at left with moveinleft 
      m "Where did you go?"
      h "Just got some wood for the fire."
      show wood at center
      "The wood just spawned in from middle of no where."
      h "What happened?"
      m "Just had a bad dream."
      "She threw the wood into the fire."
      hide wood with moveouttop
      h "We are leaving when the sun raises."
      h "I am going to take a nap."
      h "It is your turn to guard, even though you are very weak."
      h "I will help you if anything happen."
      m "Alright."
      hide hunter with moveoutleft
      
      "What shoud I do now?"
      menu:
            "Just stare at nothing.":
                  jump continue_4
            "Do the tasks which Chad gave you.":
                  jump workout
                  
image bg lafu = "lafu.png"
image bg lafu_b = "lafu_bird.png"
image bg tbc = "tbc.png"
label continue_4:
      stop music fadeout 0.5
      play music "audio/mainland.mp3"
      show bg dark forest with fade
      h "Time to go."
      show hunter with moveinleft
      h "It only going to take us about 2-3 hours to get to Lafu."
      m "Can't we just get a horse?"
      h "No, that's not possible."
      m "Why?"
      h "The forest is full of monsters."
      show bg forest with fade
      h "Now we are back on the main road"
      h "much safer than where we were."
      m "Are we close?"
      h "Probably like 15 more mintues"
      hide hunter
      show bg lafu with fade
      show hunter at right
      "Finally arrive at Lafu."
      "This city is different from what you have seen before."
      hide hunter
      show bg lafu_b with fade
      "The technology is more advanced than any other cities."
      "Advanture start here"
      "What is waiting for them in Lafu?"
      "Will they meet the girl again?"
      "Find out next time."
      show bg tbc with fade
      "Click to end the game."




      


           



      








  