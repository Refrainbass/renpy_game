label workout:
#todomax is the number of exercises they need to do
    $ todomax = 30
    $ todo = todomax
   
   
   
   
   
    #when they click on option the todo number will decrease 1
    while todo >= 0:
        menu:
            "Push up":
                $ todo -= 1
                "You did 1 pushup. [todo] to go!"

            "Situp":
                $ todo -= 1
                "You did 1 situp. [todo] to go!"

            "Squat":
                $ todo -= 1
                "You did 1 squat. [todo] to go!"
    
    if todo <= 0:
        jump continue_4

