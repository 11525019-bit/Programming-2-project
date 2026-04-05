# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Luna", color = "#cb2915")
define m = Character("Martin", color = "#e7e7e7ff")
define n = Character(None)
define phone = Character("Phone", color = "#ffffff8e")

init:
    # Luna image define
    image luna angry = "images/Luna/luna_angry.jpg"
    image luna happy = "images/Luna/luna_happy.jpg"
    image luna neutral = "images/Luna/luna_neutral.jpg"
    image luna shy = "images/Luna/luna_shy.jpg"
    image luna smile = "images/Luna/luna_smile.jpg"

    #background image define
    image room day = "images/background/bg_room_day.png"
    image room evening = "images/background/bg_room_evening.jpg"
    image room night = "images/background/bg_room_night.jpg"
    image street = "images/background/bg_street.jpg"
    image convenience store = "images/background/bg_convenience_store.jpg"
    image park = "images/background/bg_park.jpg"

    #sound effect define
    define sound_clothes   = "audio/sfx/sound_clothes.mp3"
    define sound_microwave = "audio/sfx/sound_microwave.mp3"
    define sound_small_ppl   = "<from 1 to 10>audio/sfx/sound_small_ppl.mp3"
    define sound_cash_shut_register = "audio/sfx/sound_cash_shut_register.mp3"
    define sound_tree_after_wind   = "audio/sfx/sound_tree_after_wind.mp3"
    define sound_walking_in_house = "<from 1 to 3>audio/sfx/sound_walking_in_house.mp3"
    define sound_walking_on_leaf   = "<from 1 to 3>audio/sfx/sound_walking_on_leaf.mp3"
    define sound_walking_on_rock = "<from 1 to 3>audio/sfx/sound_walking_on_rock.mp3"
    define sound_walking_on_street   = "<from 1 to 3>audio/sfx/sound_walking_on_street.mp3"
    define sound_wind = "audio/sfx/sound_wind.mp3"
    define sound_yawn   = "audio/sfx/sound_yawn.wav"
    define sound_cup_down = "<from 0 to 1>audio/sfx/sound_cup_down.mp3"
    define sound_coffee_down = "audio/sfx/sound_coffee_down.wav"
    define sound_convenience_store = "audio/sfx/sound_convenience_store.mp3"
    define sound_count_money = "<from 1 to 3>audio/sfx/sound_count_money.wav"
    define sound_paper_money = "<from 1 to 3>audio/sfx/sound_paper_money.wav"

    #background music define
    define music_beginning = "<from 1 to 64>audio/bgm1/beginning_music.mp3"
    define music_convenience_store = "<from  to 220>audio/bgm1/convenience_store_music.mp3"
    define music_park = "<from 0 to 283>audio/bgm1/park_music.mp3"
    define music_dead_ending = "<from 0 to 85>audio/bgm2/dead_ending_music.mp3"
    define music_ending = "audio/bgm2/ending_music.mp3"
    define music_locked_ending = "audio/bgm2/locked_ending_music.mp3"
    define music_street = "audio/bgm1/street_music.mp3"

# Chess_File is defined in chess_displayable.rpy
# define Chess_File = '00-chess-engine/'
init 5 python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, Chess_File, 'python-packages')
    # to prevent STOCKFISH_ENGINE from getting stored and pickled
    global_objects = {}

label start:
    $ point = Point() #Make sure the affection point do count
    
    #start when Martin just go home from work
    scene room evening with dissolve

    m "So tired, I should go to sleep"
    
    play sound sound_walking_in_house volume 0.25
    show black with dissolve

    n "......."
    n "......."
    play sound sound_wind

    n "A cold wind blow through window to wake you up."
    n "The room is quiet in the way a paused video is quiet: not peaceful, only waiting."

    play music music_beginning volume 0.5
    scene room night with dissolve
    play sound sound_yawn
    m "..."
    m "Another night pass."
    m "What a tired day."
    m "Thinking about what I have to suffer in the company is enough."
    m "Being pressured by the boss, envy look by the co-worker."
    m "Just thinking of it...."
    m "make me never want to leave the bed and go outside."

    n "The phone is ringing."
    n "It glows with tired attention, emotionless messages."
    n "It shine so much like it have never shined for the past few decades."
    m "Who can messages me this time?"
    m "The working time is over for a long time."

    menu:
        "Check the phone":
            n "Messages. Notifications. Promotions."
            n "A thousand tiny attempts to touch you without ever reaching you."
            m "So many voices."
            m "None of them feel alive."

        "Leave it alone":
            n "You turn your face away."
            n "The screen keeps shining like a small artificial moon."
            m "If I ignore it long enough, maybe it will stop pretending I matter."
            n "It does not."

    n "You stand up."
    n "The mirror catches you for a second."
    n "It shows a person-shaped absence."


    scene street with dissolve
    play sound sound_walking_on_street volume 0.5

    n "Outside, the city is already sleeping."
    n "The street with the absence of people make this moment so emotion."
    n "Nothing happen....."
    n "Just nothing....."
    n "Nothing....."
    n "....."
    n "....."
    n "....."

    stop sound
    play music music_street fadeout 1.0 fadein 1.0 volume 0.75

    l "You're late."

    show luna angry at center with dissolve

    m "Oh I forget that I invited you to go outside with me."

    l "That's a sad thing to say in a world full of people who are always 'busy.'"

    m "Busy is just a nicer word for unavailable."

    show luna neutral at center

    l "At least you're honest."

    n "She stands there, close enough to talk to, far enough to remain a gap as a stranger."

    n "She start walking slowly."

    n "Aren't you should ask her something?"

    menu:
        "Ask her to walk with you":
            m "Walk with me."

            show luna shy with dissolve
            l "W-Why?"
            m "I don't know."
            m "The street feels less empty if someone is beside me."

            l "That's a weak reason."
            m "It's the only real one."

            l "Ok. I'm accept that reason this time."
            show luna smile with dissolve
            $ point.add(20)

        "Say nothing":
            n "You stay silent."
            n "Silence is the only thing that still feels personal."
            l "..."
            l "You always do that when you're tired of existing."
            $ point.add(0)

        "Ask her if she is real":
            m "Are you actually here?"
            show luna shy with dissolve

            l "......."
            l "That's a strange question."
            m "I mean it."
            l "So do I."
            l "I don't know if 'here' means anything anymore."
            show luna neutral with dissolve
            $ point.add(10)

        "Walk with her without asking":
            play sound sound_walking_on_street volume 0.5
            n "......"
            n "....."
            n "...." 

            show luna shy with dissolve
            l "D...D-Do you want to walk with me?"
            m "Yea?"
            l "You are acting as a pervert."
            l "If you want it just ask me, don't just do it yourself."
            m "Okay?"
            $ point.add(10)

    play sound sound_walking_on_street volume 0.5

    n "She starts walking again."
    n "You follow."
    n "Two bodies moving together does not always mean two lives sharing the same world."

    play music convenience_store_music fadeout 1.0 fadein 1.0 volume 0.75
    play sound sound_convenience_store
    scene convenience store with dissolve
    show luna neutral at left with dissolve

    n "The convenience store is bright and hollow."
    n "Its light makes everything visible except meaning."

    m "Let's buy something."

    l "You say that like you're not already trying to buy time."

    menu:
        "Buy coffee":
            play sound [sound_paper_money, sound_count_money, sound_cash_shut_register]
            n "......"
            stop sound
            
            n "You take a bitter coffee from the shelf."
            m "It tastes like staying awake against your will."
            l "Most modern life does."

            play sound sound_coffee_down
            $ point.add(5)

        "Buy two drinks":
            play sound [sound_paper_money, sound_count_money, sound_cash_shut_register]
            n "......"
            stop sound
            n "You hand one to her."
            l "For me?"
            show luna happy with dissolve
            m "Maybe."
            l "Maybe is a kind of honesty."
            show luna neutral with dissolve
            $ point.add(10)

        "Buy nothing":
            n "You stand between the shelves and realize you do not need anything."
            m "I came here because I thought I was supposed to want something."
            show luna smile with dissolve
            l "And?"
            m "I don't."
            show luna neutral with dissolve
            l "That's rare."
            $ point.add(0)

        "Buy milk tea for both":
            n "You try to buy it but the full topping one cost more than the amount you bring."
            n "So you just buy a medium one with only black pearls."

            play sound [sound_paper_money, sound_count_money, sound_cash_shut_register]
            n "......"
            stop sound
            
            m "Here, I'll pay for it."
            show luna smile with dissolve
            l "So you are trying to be a man in front of my eye."
            l "Don't have to do that, I just need by your side."
            l "That is enough."
            show luna neutral with dissolve
            
            n "She smiled."
            n "Is she really smiled over what I do?"
            n "I hope that is true cuz look how shined she is after it."
            n "I mean ..."
            n "She is really happy and like my milk tea."

            play sound sound_cup_down
            $ point.add(20)

    play sound sound_small_ppl volume 0.75 loop
    n "You sit by the window."
    n "The city silently shifting to a new day."
    n "What a beautiful moment to enjoy."
    n "The same as the way you look the girl sit next to you."
    n "Shouldn't I ask her something?"
    play audio sound_microwave volume 0.2 
    menu:

        "Ask her something":
            l "Do you ever feel like everyone is performing?"
            m "Everyday."
            l "Posting, smiling, updating, disappearing."
            l "People keep turning themselves into objects and then complain that they feel empty."
            m "Maybe the emptiness was there first."
            l "Maybe."
            l "Or maybe the emptiness is what remains after being watched too much."
            $ point.add(10)

        "Stay silence":
            n "You enjoy the night."
            n "Enjoy the cold of the air."
            n "The air that make you wake up and have to stay for a full night."
            n "I don't know if it is good or bad."
            $ point.add(0)

    n "You stay silence for a minute."
    n "That make the atmosphere between you and her weirder."
    n "You feel like the world is just a matrix."
    n "People just like a machine working everyday."
    n "After the work done, the recharge and do that again."
    n "That make you feel like you aren't real."
    n "You thinking about it, thinking, thinking...."
    n "And then you want to ask her that questions."

    menu:
        "Tell her you feel invisible":
            m "Sometimes I think I don't exist unless someone needs me."

            l "That's not unusual."
            l "Most people are only visible in other people's emergencies."
            m "What a great way to explain it."

            l "That's a harsh truth."
            $ point.add(20)

        "Ask her what she wants":
            m "What do you want?"

            l "We should stop pretending that wanting things makes us less lonely."
            l "It doesn't."
            l "We should open to each other more."
            m "Can I?"
            l "I don't know, can you?"
            l "You can try your best to do it."
            $ point.add(10)

        "Look away":
            n "You stare through the glass."
            n "A reflection stands where your future should be."
            l "You do that when you're afraid of being understood."
            l "An afraid you always bring out when facing something harsh."
            m "I don't ..."
            m "Maybe I am."
            n "She laughed."
            n "Although it just in a fraction of a time."
            n "Maybe I should face that emotion."
            $ point.add(5)

        "Compliment her":
            m "What a great day isn't it?"
            m "As great as you."

            l "......."
            l "......"
            l "....."
            l "Did you make that up a minute ago?"
            l "If not that is so smooth."
            l "I think you are cute right now."

            n "I don't know if she really mean it."
            n "I think she is making joke of me or just trying to compliment me like what I did."
            $ point.add(10)

    stop sound fadeout 1.0
    n "After a minute or so, you and her decided to walk out toward the park."
    stop music fadeout 1.0

    show black with dissolve
    play sound [sound_walking_on_street, sound_walking_on_rock, sound_walking_on_leaf] volume 0.5

    n "It is midnight, the park is almost empty."
    
    stop sound

    scene park with dissolve
    show luna neutral at right with dissolve
    play music music_park fadein 1.0 volume 0.75

    n "The trees do not care who has names and who does not."
    n "They simply remain."

    m "It's quieter here."

    l "Quiet can be honest."
    l "Or it can just be another way to hide the noise."

    n "You sit on a bench."
    play sound sound_clothes
    n "The space between you is small, but it remain enough space to have a gap between you and her like a stranger."
    n "Loneliness is strange: it survives distance, and sometimes it survives closeness too."
    play sound sound_tree_after_wind loop

    menu:
        "Ask her to stay a while":
            m "Stay with me a bit longer."

            l "Why?"
            m "Because when you leave, it feels like the day never happened."
            l "Maybe it didn't."
            l "Maybe all of this is only in your thought."
            show luna happy at right with dissolve
            $ point.add(10)

        "Say what you feel":
            m "I don't know if I'm talking to you or to my own thoughts."

            l "Maybe that's the same thing."
            l "Maybe that's why no one ever feels completely heard."
            $ point.add(15)

        "Stay quiet":
            n "You listen to the wind instead."
            n "It sounds more reliable than people."
            l "You're quiet when you're thinking too hard."
            $ point.add(5)

    play audio sound_wind
    n "She looks up at the sky."
    n "Dusk makes everything look temporary."

    show luna neutral at right with dissolve
    l "Do you think a person still exists if nobody remembers them?"
    m "I want to say yes."
    m "I don't know if I believe it."
    l "That's the problem."
    l "We all want existence to be guaranteed by feeling."
    l "But feelings are unstable."
    l "So maybe the self is unstable too."

    m "Then what am I?"

    l "Maybe a pattern."
    l "Maybe a habit."
    l "Maybe the echo left behind after the world stops paying attention."

    n "You stare through the shinning moon go over your head."
    n "The best moment to relaxed yourself."
    n "However, a small voice start to rise next to you"

    l "{size=-18}There's{/size} {size=+3}something{/size} {size=+3}I{/size} {size=+3}want{/size} {size=+3}to{/size} {size=+3}ask{/size} {size=+3}you.{/size}"

    m "What is it?"

    l "If everything around us is only a surface..."
    l "and every person is just a version of what others can tolerate..."
    l "then how do you know you are real?"

    menu:
        "Answer that you don't know":
            m "I don't know."
            
            l "Hmmm, I think...."
            l "Anyone who claims certainty in a world like this is either lying or already gone."
            $ point.add(10)

        "Answer that she is real":
            m "Because you're here."

            l "That doesn't prove anything."
            l "It only proves that you need me to be real."
            l "Is that a flirt for me?"
            $ point.add(15)

        "Answer that maybe nobody is real":
            m "Maybe no one is real."
            m "Maybe we only keep each other alive by pretending."

            l "That's frightening."
            l "And maybe true."
            $ point.add(5)

    n "She watches you for a long moment."
    n "You stay silence for a whole time."
    n "You start to shift your focus to your feeling."
    n "It feel so good."
    stop sound

    if point.total()<=40:
        jump bad_ending
    elif point.total()<=60:
        jump locked_ending
    elif point.total()<=80:
        jump dead_ending
    else:
        jump chess_ending


    #Bad ending
    label bad_ending:

        n "The night feels longer than before."

        play sound sound_wind

        n "Even the wind sound more blue than before"
        n "Can't imagine how long I can enjoy this before tomorrow working day come."

        show luna neutral at right with dissolve

        l "You look tired."
        m "I think I'm just thinking too much."

        l "That's what lonely people call it when the silence starts answering back."

        m "Will I see you again?"

        n "She looks at you for a long moment."
        n "Her face is calm, but her eyes are already moving away."

        l "Maybe."
        l "Or maybe you just needed me to exist long enough to make tonight feel less empty."

        m "Don't say that."

        l "Why?"

        m "Because it feels like you're leaving."

        l "I already did."

        n "The words do not land like an insult."
        n "They land like a truth too late to stop."

        n "When you blink, she is gone."
        n "No footsteps."
        n "No goodbye."
        n "Only the streetlight, the pavement, and your own breathing."

        play sound [sound_walking_on_leaf, sound_walking_on_rock, sound_walking_on_street] volume 0.5
        scene street with dissolve
        scene room night with dissolve
        play music music_ending fadeout 1.0 fadein 1.0 volume 0.75

        n "You return home."
        n "The room is exactly the same as before, which is how you know something changed."

        m "..."
        m "Was she real?"

        n "No answer comes."
        n "The silence feels familiar now, almost domestic."
        n "You sit on the bed and wait for a message that never arrives."

        n "Maybe she was never a person."
        n "Maybe she was the shape your loneliness took when it finally learned your name."

        jump quit


    #Locked ending
    label locked_ending:
        n "You and Luna enjoy a night."
        n "A good night ...."
        n "A night you don't have to worry about anything...."
        n "A night that make you feel it never exist..."

        l "Can I go now?"

        n "She just suddenly say that out of the blue."

        n "You have nothing more to keep her."
        m "Yea, I feel like I want to stay here for a little bit longer."

        n "Then she stand up and leave."
        hide luna neutral
        n "After a half an hour, you feel that is enough for this night."
        m "I should go home and head to bed now."

        play sound [sound_walking_on_leaf, sound_walking_on_rock, sound_walking_on_street] volume 0.5
        n "......."
        stop sound
        show black with dissolve

        scene room day
        play music music_locked_ending fadeout 1.0 fadein 1.0 volume 0.75

        n "You wake up."
        n "Or think you do."

        m "That dream again..."

        n "The room is your room."
        n "The light is your light."
        n "The same hour seems to be waiting in the same place."

        n "Outside, the city sounds distant, muffled, unreal."
        n "Inside, the air feels too still to belong to morning."

        m "Look like everything is just a dream."
        m "And now I have to make my mind up to go to work."
        
        n "......"
        n "......"
        n "......"
        p "You just got a message from Luna {cps=10}....{/cps}"
        jump quit


    # Dead ending
    label dead_ending:
        n "You and Luna enjoy a night."
        n "A good night ...."
        n "A night you don't have to worry about anything...."
        n "A night that make you feel it never exist..."

        l "Look like the time is coming."
        l "I have to leave now."
        l "Goodbye. See you again."
        hide luna neutral

        n "When she leave, you start to feel some pain."
        n "The pain that you think it was already erased {cps=10}....{/cps} but no {cps=10}...{/cps} It was never be erased."
        n "You stay for a hour more to erase that feeling."
        n "But as long as you stay, that feeling still keep chasing you."
        n "It still stay there."
        n "Nothing change."
        m "Maybe I'm in love with her."
        n "That's what you can think of right now."
        m "Maybe I should go home now and make up my mind."
    
        scene street with dissolve
        n "....."
        scene room night with dissolve

        stop music fadeout 3
        stop sound fadeout 3
        $ quick_menu = False
        window hide
        show black with dissolve
        
        scene room day
        play music music_dead_ending fadeout 1.0 fadein 1.0 volume 0.75
        m "......"
        m "......."
        m "N....."
        m "No..."
        m "NO..."
        m "IT CAN'T BE A DREAM."
        m "NOO..."
        m "Maybe I should try to see her."
        m "Try all the way to sEe hEr aGaIn ...."
        m "{cps=12}I ThInK ShE iS iN LiMbO....{/cps}"
        m "{cps=12}ThErE FoR I HaVE to D#^D TO SEe Her AgAin...{/cps}"

        jump quit



    #Chess ending
    label chess_ending:
        # board notation
        $ fen = Start_FEN
        $ global_objects['STOCKFISH_ENGINE'] = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
        $ depth = 7  # harder from 1 to 20

        n "Suddenly, you feel she want to say something to you."

        l "Look like the time has come."
        l "I will tell you the truth."

        m "The truth? {cps=3}. . .{/cps} What truth?"

        l "I will let you play first."
        l "I will tell you the truth if you can make a draw with me."
        l "If you can win me then it is even better."

        play music music_ending fadeout 1.0 fadein 1.0 volume 0.75

        # user will play with white
        $ player_color = chess.WHITE 

        window hide
        $ quick_menu = False

        # avoid rolling back and losing chess game state
        $ renpy.block_rollback()

        # disable Esc key menu to prevent the player from saving the game
        $ _game_menu_screen = None

        call screen chess(fen, player_color, depth)

        # re-enable the Esc key menu
        $ _game_menu_screen = 'save'

        # avoid rolling back and entering the chess game again
        $ renpy.block_rollback()

        # restore rollback from this point on
        $ renpy.checkpoint()

        # kill stockfish engine
        $ quit_stockfish()

        $ quick_menu = True
        window show

        show luna happy at center with dissolve
        stop music
        if _return == Draw:
            l "The game ended in a draw."
            jump draw
        
        elif _return == chess.WHITE:
            l "You win!"
            jump win

        else:
            l "You lose."
            jump lose

        label win:

            l "Wow, I didn't know that you can win me."
            l "I will keep my promise, I will tell you the truth."

            jump truth

        label draw:

            l "Ha ha, nice try, but you can't still win me."
            l "But I still want to tell you the truth."
            l "Now. Come closer to me."

            jump truth

        label lose:
            
            l "I know you try your best."
            l "But you still can't win me."
            l "Maybe I was too harsh on you."
            l "Therefore, I will tell you the truth."

            jump truth


        label truth:

            l "Are you ready?"
            l "1...."
            l "2...."
            l "3...."

            window hide
            scene room day

            m "{cps=8}What just happen?{/cps}"
            m "{cps=10}Everything{/cps} {cps=2}...{/cps} {cps=10}EVERYTHING,{/cps}"
            m "No {cps=4}......{/cps} Everything can't just be a dream."
            m "No ... {cps=10} No! No! No! No! {/cps}"
            m "{cps=2}...........................{/cps}"
            m "{cps=2}...........................{/cps}"
            m "{cps=2}...........................{/cps}"
            
            #play sound "audio/sound_alarm.mp3" 

            m "Oh no!!!!"
            m "I have to go to work."
            m "Otherwise, I will be kicked."
            jump quit


    label quit:
        stop music fadeout 3
        stop sound fadeout 3
        $ quick_menu = False
        window hide
        show black with dissolve
        return

# This is the end of the game.