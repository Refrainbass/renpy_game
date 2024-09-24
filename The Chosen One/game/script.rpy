# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define config.name = _('The Chosen One') #game name and version 
define gui.show_name = True
define config.version = "1.3"
define gui.about = _("Created by Setsu.S")
#music
define config.main_menu_music = "audio/mainland.mp3"
define config.game_menu_music = "audio/mainland.mp3"
define config.main_menu_music_fadein = 0.5



#images
define m = Character("Me", color="#0000FF")
define parent = Character("Sister", color="#FFFF00")
define h = Character("Hunter", color="#028A0F")
define g = Character("Giga Chad", color="#FFD700")
define who = Character("?")
define maid = Character("Maid", color="#ADD8E6")
define alice = Character("Alice", color="#ADD8E6")
image giga = "giga.png"
image sister = "sister.png"
image white = "#FFFFFF"
image black = "#000000"
image red = "#FF0000"
image bg forest = "bg forest.png"
image bg home = "bg home.jpg"
image wolf = "wolf.png"
image wolf1 = "wolf1.png"
image wolf2 = "wolf2.png"
image wolf3 = "wolf3.png"
image bg dark forest = "bg dark forest.png"
image bg sunset village = "bg village2.png"
image bg village1 = "bg village1.png"
image bg hotelm = "bg hotelmorning.jpg"
image bg hoteln = "bg hotelevening.jpg"
image bg note = "bg notes.png"
image bg note1 = "notes1.png"
image bg note2 = "notes2.png"
image bg note3 = "notes3.png"
image bg note4 = "notes4.png"
image bg note5 = "notes5.png"
image bg note6 = "notes6.png"
image bg note7 = "notes7.png"
image bg note8 = "notes8.png"
image bg note9 = "notes9.png"
image bg note10 = "notes10.png"
image bg note11 = "notes11.png"
image bg note12 = "notes12.png"
image bg note13 = "notes13.png"
image bg note14 = "notes14.png"
image bg note15 = "notes15.png"
image bg white = "white.jpg"
image bg black = "black.jpg"
image bg town1 = "town1.jpg"
image bg town2 = "town2.jpg"
image bg 3years = "3years.png"
image bg black = "black.jpg"
image bg fastfood = "fastfood.png"
image maidi = "maid.png"


# The game starts here.

label start:
    play music "audio/spring.mp3" volume 0.2

    show bg forest
    with vpunch

    m   "Where am I, I don't remember what happened."

    m "Last thing I remember was..."

    scene home
    show bg home
    with dissolve
    show sister at right

    parent "Why you are not eating your breakfast?"
    m "Sorry I was just daydreaming"
    parent "Be quick or else you will be late"

    menu:
        "Keep the same speed or hurry up?"

        "Be Quick":
            m "(You finish your breakfast very quick)"
        
        "Slow":
            m "(Keep eating with the same speed)"
            stop music fadeout 1.0
            jump ending_1

    hide sister
    show bg forest
    with vpunch
    stop music fadeout 0.2
    play music "audio/mainland.mp3" volume 0.5

    m "What???"
    m "What is this place"

    jump forest_1

return          
 
    
    
