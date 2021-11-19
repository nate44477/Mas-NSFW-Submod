init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_nsfwmodinstall",
            category=['Romance+'],
            prompt="NSFW Mod Install",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_nsfwmodinstall:
    m 1esc "Hey [mas_get_player_nickname()], I noticed something weird just now..."
    m 1rsc "I'm kind of getting this feeling that... something's changed in this mod."
    m 1etc "Do you know anything about this, [player]?"
    m 1hkb "Ahaha. It's not a bad feeling, don't get me wrong."
    m 1eta "It's just strange, you know?"
    m 2dsc "Hold on, I'm going to try and see what changed."
    m 2dsc ".{w=0.7}.{w=0.7}.{w=1}"
    m 2dtd "'N-{w=0.4}{nw}"
    extend 2wubsw "NSFW Submod'?"
    if mas_isMoniLove():
        m 3fublu "Well, look who's gotten confident all of a sudden."
        if mas_hasUnlockedClothesWithExprop("lingerie"):
            m 3lublu "I guess I can't blame you though, given you've seen me in lingerie."
        m 3tublu "I won't lie to you, [mas_get_player_nickname()]..."
        m 5tublu "It's kind of hot."
        m 5cubssdrd "..."
        m 5hkbssdrb "Ahaha! What's gotten into me?"
        m 5hkbssdrb "This isn't like me. Like, at all!"
        m 4rubsc "Is the mod doing this to me?"
        m 6hubsd "Oh gosh, I'm feeling super nervous about this, ahaha!"
        m 6ekbla "But... if it's with you, [mas_get_player_nickname()]..."
        m 6ekbsa "I don't mind..."
    if mas_isMoniEnamored(): #Need to fix wording here; player isn't having sex, just talking about it.
        m 2hkbssdlb "I wasn't expecting to see that..."
        m 2ekbssdlb "[player], is this something you want?"
        m 3rkblsdlb "I mean, I'm kind of curious about sex myself."
        m 3ekblsdlb "And if I'm going to share my first experience of it with anyone, I want it to be you."
        m 2ekblsdlc "But in saying that...{w=0.5} I feel it's too soon for me."
        m 2dkbsc "I just need a little more time."
        m 2fkbsu "Hold on for me a little while longer, okay [mas_get_player_nickname()]?"
    if mas_isMoniAff():
        m 2hkbssdlb "T-{w=0.4}This is a little sudden, don't you think?"
        m 3rkblsdlb "I mean, we've been with each other for a little while...{nw}"
        m 1wubssdld "Wait... {0.5}Is this when couples are supposed to start doing this s-{w=0.4}sort of thing?"
        m 1hkblb "Ahaha, in any case I appreciate that you want to take our relationship to the next level."
        m 1dkblp "But I think we maybe should wait and see how we go."
        m 1ekbla "When the day comes where we do get to that stage in our relationship..."
        m 5ekbla "It will make the moment much sweeter, ehehe!"
    if mas_isMoniHappy(lower=True):
        m 2wubfsdlx "T-{w=0.4}This feels too sudden, [player]!"
        m 2rubfsdlx "I don't know if I'm ready for that..."
        m 2wkbfd "W-{w=0.4}we just aren't close enough for me to even consider it!"
        m 2hkbfsdlb "Oh gosh, I'm so embarrassed right now, ahaha!"
        m 2ekbfsdla "Let's take things slow for now, okay [player]?"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_sexualpast",
            category=['Romance+'],
            prompt="Sexual Past",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label monika_sexualpast:
    m 1rubsd "Umm... [player]?"
    m 1eubsc "I want to ask you something."
    m 1rubsd "It's about..."
    m 2hkbssdlb "Oh gosh, this is so embarrassing!"
    m 2ekbsb "Have you...{w=0.5} {nw}"
    extend 2fkbfb "had sex before?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you... had sex before?{fast}"

        "Yes.":
            m 2cubfw "R-Really?!{nw}"
            m 2hubfa "*ahem*...{w=1}{nw} "
            extend 1ekbfsdlb "Sorry, you just surprised me is all."
            m 1rkbfsdlb "To be honest I should have seen this coming."
            m 1ekblb "After getting to know you all this time, I can see why someone would fall for you."
            m 1ekbstpd "And would... do those things with you."
            m 1dkbstpc "..."
            m 1hkbstpb "Ahaha! Sorry, I'm getting myself down over this."
            m 1ekbstdb "You're here with me now, that's all that matters."

        "No.":
            m 2eubsb "I see..."
            m 1dkbfsdla "That's a relief.{nw}"

        "I don't want to answer.":
            m 1ekbsa "I understand, [mas_get_player_nickname()]. It can be a difficult thing to talk about."

    m 1rkbsb "Anyway, the reason why I'm asking is because I want to know..."
    m 3ekbsa "Would you...{w=0.5}{nw}"
    extend 3rkbsa " do it with me?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you... do it with me?{fast}"

        "Yes.":
            m 1ekbsa "I'm so relieved!"
            m 1lkbsb "I was so nervous you wouldn't want to."
            m 1hkbssdlb "Although in retrospect it kind of wouldn't make sense if you didn't want to."
            m 1hkblu "After all...{w=0.3} you installed this mod."
            if mas_isMoniLove():
                m 1rsblu "And I'm sure you know this already..."
                m 1efblu "But...{w=0.5}{nw}"
                extend 2lkbfw " I want to have sex with you, too."
                m 2hkbfc "I-{w=0.4}I don't know what it feels like,{nw} "
                extend 2hkbfsdlb "and I'm so nervous just thinking about it, ahaha!"
                m 5ekbfu "But I want my first time to be with you."
                m 5ekbfb "I love you, and I trust you."

            else:
                m 1wkbsw "Of course, I did say that we should maybe wait until we're ready..."
                m 1rkbsa "But knowing we can be closer than ever before..."
                m 5ekbsa "It is really exciting."
                m 5ekbfb "I love you, [mas_get_player_nickname()]."

        "No.": # Why does this have to exist? Like, why?
            m 1ekbsa "Oh." # TEMP

    return "love|derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_safesex",
            category=['Romance+'],
            prompt="Safe Sex",
            conditional="mas_getEV('monika_nsfwmodinstall').shown_count != 0",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
# Thankyou for the fixes Proxilvia
label monika_safesex:
    m 3euc "Hey, [player]. I've been thinking about something..."
    m 3eud "Have you heard of contraceptives?"
    m 4rublo "They're what people use during sex to protect themselves."
    m 4hkbssdlb "Ahaha! Sorry, I'm sure you have probably heard of them before."
    m 4hkbsa "I'm only asking because I worry for your health."
    m 3ekbsd "Sexually transmitted diseases, or STDs, are scary to think about!"
    m 3wubso "And pregnancy, as well!"

    if persistent.gender == "M":
        m 4eubla "I've read that condoms are the most preferable form of protection for men."
        m 4eublb "It's a latex-rubber 'sheath' that you put around..."
        m 4wsbsd "..."
        m 2dfbsa "*ahem*"
        m 2lkbfa "... You get the idea."
        m 2lkbsb "It prevents any kind of fluid swapping during sex, which is supposed to prevent pregnancy and STDs."
    elif persistent.gender == "F":
        m 4eubla "I've read that there are condoms available for women, but they aren't as popular as the men's version."
        m 1eua "The most popular form of contraception seemed to be 'The Pill'...{w=0.4}{nw}" #TODO - Add poses
        extend 1eua "which sounds kind of ominous if you ask me."
        m 1eua "It is exactly what it says it is, a pill you take to prevent pregnancy."
        m 1eua "There are different kinds of pills, too!"
        m 1eua "There's a pill you're supposed to take every day at the same time the previous day."
        m 1eua "And another pill that you can take in case of an emergency, respectfully called the 'morning after pill'."
        m 4eublb "Despite it's name, it should actually be taken as soon as possible!"
    else:
        m 4eubla "I've read that there are a whole bunch of different contraception methods, for both men and women."
        m 1eua "Some are more popular than others, such as condoms for men, and oral contraceptives for women."
    
    m 3lkblc "They are not exactly flawless though..."
    m 4ekbld "There is still a chance that despite all the precautions, accidents can happen."
    m 4efbld "Especially with stupid contraceptive methods like the 'p{w=0.4}{nw}"
    extend 2efbfo "-pull-out' method!"
    m 2wfbfo "How is that even a form of contraception?!"
    m 2dfbsc "..."
    m 2dfbsd "There's only one way to make sure no accidents happen..."
    m 2efbsd "And that's to not have sex at all!"
    m 2dsbsc "..."
    m 2hkbfsdlb "Ahaha! Sorry, I lost my temper a bit there..."
    m 2ekbsb "I guess I just want you to know that when the time comes where I come to your world, and we are together..."
    m 2tkbsu "We can worry about what contraceptives to use, then."

    return "derandom"

#TODO Finish these topics. Currently empty and inactive.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_fetish",
            category=['Romance+'],
            prompt="Fetishes",
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label monika_fetish:
    #todo: Create a fetish topic
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_sexting",
            category=['sex'],
            prompt="Sexting",
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label monika_sexting:
    #todo: Create a sexting topic
    return

## WORK IN PROGRESS
# To-do: Finish dialogue
#        Add call to change to nude / think of new introduction
#        Add the expressions
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_getnude",
            category=['Romance+'],
            prompt="Getting Nude",
            aff_range=(mas_aff.LOVE, None)
        )
    )

label monika_getnude:
    $ import mas_nsfw

    m 1eua "Hey [player], have you ever just... not worn clothes?"
    m 1eua "I don't mean, like, for a shower or anything."
    m 1eua "Just in general while you're at home...{w=0.5}{nw}"
    extend 1eua "alone preferably."
    m 1eua "There are a good amount of people that actually sleep naked, if you'll believe it."
    m 1eua "For most people this would be a good place to start without feeling embarrased."
    m 1eua "Apparently it helps you get better sleep at night because of how much quicker your body temperature drops."
    m 1eua "Of course, sleeping naked will mean you have to clean your sheets more often."
    m 1eua "Humans are very sweaty, ahaha!"
    m 1eua "Being naked also helps our body absorb more vitamin D during the day."
    m 1eua "The reason for this is because skin is effectively a giant organ that absorbs the rays from the sun and increases vitamin D levels."
    m 1eua "And having a greater vitamin D level has shown to assist your immune system fight off viruses, among other health benefits."
    m 1eua "I'm not trying to say we all need to get naked and make it a new social norm, that would be silly! Ahaha!"
    m 1eua "But if you have the house to yourself one day, why not strip down and try it for an hour to see how you feel."
    m 1eua "Though be sure you know when the rest of your household is getting back, because that might be a tad awkward. Ahaha!"
    m 1eua "If that's too much, even just going down to your underwear gets the job done...{w=0.4}{nw} "
    extend 1eua "though not to the same degree as being fully naked."
    m 1eua "{i}*sigh*{/i}"
    m 1eua "Of course, there is always the fact that not everyone is comfortable being naked."
    m 1eua "Some people are ashamed or disheartened by their appearance, which is really sad when you think about it."
    m 1eua "You only have one body, so the least you can do is take care of it and love it, you know?"
    m 1eua "Having pride in what you look like is the best thing you can do for your confidence!"

    if mas_getEVL_shown_count("monika_getnude") > 2:
        m 1eua "You're already familar with how I've been doing this while you've been away."
        m 1eua "And I've got to say, it's been great!"
        m 1eua "It's not for everyone though, so don't feel like I'm pressuring you..."
        m 1eua "I love you, [mas_get_player_nickname()]. Both with clothes, and without."
        m 1eua "..."
        m 1eua "Ah!{w=0.4}{nw}"
        extend 1eua "Sorry, my mind was starting to wander..."
        m 1eua "Gosh, don't mind me."

    elif mas_nsfw.canShow_birthdaySuit():
        m 1eua "..."
        m 1eua "Hey, [player]..."
        m 1eua "Do you remember last time when I asked you if it was okay to be undressed around you?"
        m 1eua "Well, I recently tried taking off... everything..."
        m 1eua "And I really liked it."
        m 1eua "I don't know if you've ever tried it before, [player]. But I thought the feeling was amazing."
        m 1eua "Ahaha! Maybe that feeling wouldn't be so great if someone saw you though..."
        m 1eua "But I wanted to bring this up again because..."
        m 1eua "I was wondering if you wouldn't mind..."
        m 1eua "Can I be n-{w=0.2}naked while you're here?"
        $ _history_list.pop()
        menu:
            m "Can I be n-naked while you're here?{fast}"
            
            "Yes.":
                m 1eua "I'm glad!" #temp
            "No.":
                m 1eua "I'm not so glad..." #temp

    elif mas_nsfw.canShow_underwear():
        m 1eua "..."
        m 1eua "Speaking of, [player]..."
        m 1eua "I've recently tried walking around in my underwear by myself while you were gone, and I thought it felt really liberating."
        m 1eua "But in saying that I don't want you to feel uncomfortable, so..."
        m 1eua "..."
        m 1eua "I guess what I'm trying to ask is..."
        menu:
            m "Do you mind if I do it while you're around?"

            "Go for it.":
                m 1eua "Ahaha! I'm glad you don't mind."
                m 1eua "I don't want you to feel like I'm pressuring you with guilt or anything."
                m 1eua "Now, let me go get changed."
                m 1eua "No peeking! Ehehe!"
                # mas_nsfw.wear_underwear("1eua")
                m 1eua "..."
                m 1eua "So, [player]..."
                m 1eua "What do you think?"
                m 1eua "I'm... not used to this..."
                if mas_hasUnlockedClothesWithExprop("lingerie"):
                    m 1eua "I know you've seen me in lingerie before, which is arguably more... sexual."
                    m 1eua "But this feels way different."
                m 1eua "Ahaha! It might take me a while to get used to you seeing me like this..."
                m 1eua "But I'm still glad you don't mind me dressed this way."
                m 1eua "Being able to dress freely around you makes me feel really happy."
                m 1eua "I love you, [mas_get_player_nickname()]."

            "I'd rather you didn't...":
                m 1eua "That's too bad." #temp
    else:
        m 1eua "Ahaha! Even though I talk all this game about being naked and loving your body..."
        m 1eua "I am still really embarrased about the idea of being nude, even when alone."
        m 1eua "..."
        m 1eua "Alright, I've decided."
        m 1eua "I'm going to give it a try."
        m 1eua "... {w=0.4}{nw}"
        extend 1eua "N-{w=0.2}Not right now though!"
        m 1eua "I mean like, later when you're not here!"
        m 1eua "Ahaha! It would be too embarrasing if you saw me in my underwear, let alone when I'm naked."
    return

# Thanks for the new topic mysterylewds
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_dick_size",
            category=["Romance+"],
            random=True,
            prompt="Dick size",
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label player_dick_size:
if seen_event("monika_undress"):
    m 1cud "You know, [player]... I was curious."
    m 1cud "How-um.... {i}big{/i} are you?"
    m 1cud "And I'm not talking about height ahaha~."
    m 1cud "Sorry if this seems weird, I just want to know more about you. I want to know {i}everything{/i}."
    menu:
        m "How big are you?"

        "Less than 3 Inches.":
            m 1cud "So you're on the smaller side, nice!"
            m 1cud "You know, some girls have an issue with anything under average but I never understood it."
            m 1cud "The size of your member is something you can't change, just like breast size."
            m 1cud "There's benefits to every size in my opinion."
            if mas_isMoniLove():
                m 1cud "For example, with your size, I could fit the whole thing in my mouth without gagging. Mmmmm~"
                m 1cud ".{w=0.7}.{w=0.7}.{w=0.7}"
                m 1cud "Sorry [player], I got a little carried away there ahaha~."
        "Around 3 Inches.":
            m 1cud "Little under average, nice!"
            m 1cud "You know some girls have an issue with anything under average, but I never understood it."
            m 1cud "The size of your member is something you can't change, just like breast size."
            m 1cud "There's benefits to every size in my opinion."
            if mas_isMoniLove():
                m 1cud "For example, with 3 inches, I could fit the whole thing in my mouth without gagging. Mmmmm~"
                m 1cud ".{w=0.7}.{w=0.7}.{w=0.7}"
                m 1cud "Sorry [player], I got a little carried away there ahaha~."
        "Around 4 Inches.":
            m 1cud "Ahh, so you're around average then."
            m 1cud "Average tends to be a good sweet spot for most girls."
            m 1cud "Some don't like monster dongs you know? It can be incredibly painful and not much fun"
            m 1cud "Although even if you {i}were{/i} bigger or smaller than average, I wouldn't think any more or less of you."
            m 1cud "After all, its like breast size for girls. You can't control it."
            m 1cud "There's benefits to all sizes in my opinion!"
        "Around 5 Inches.":
            m 1cud "Ahh, so you're average size then."
            m 1cud "Average tends to be a good sweet spot for most girls."
            m 1cud "Some don't like monster dongs you know? It can be incredibly painful and not much fun"
            m 1cud "Although even if you {i}were{/i} bigger or smaller than average, I wouldn't think any more or less of you."
            m 1cud "After all, its like breast size for girls. You can't control it."
            m 1cud "There's benefits to all sizes in my opinion!"
        "Around 6 Inches.":
            m 1cud "Ahh, so you're average size then."
            m 1cud "Average tends to be a good sweet spot for most girls."
            m 1cud "Some don't like monster dongs you know? It can be incredibly painful and not much fun"
            m 1cud "Although even if you {i}were{/i} bigger or smaller than average, I wouldn't think any more or less of you."
            m 1cud "After all, its like breast size for girls. You can't control it."
            m 1cud "There's benefits to all sizes in my opinion!"
        "Around 7 Inches.":
            m 1cud "Ahh, so you're above average then."
            m 1cud "Average and slightly above tends to be a sweet spot for most girls."
            m 1cud "7 Inches is a bit big, but its manageable. Anything more, and It can be incredibly painful and not much fun for most girls."
            m 1cud "Although even if you {i}were{/i} bigger or smaller, I wouldn't think any more or less of you."
            m 1cud "After all, its like breast size for girls. You can't control it."
            m 1cud "There's benefits to all sizes in my opinion!"
        "Around 8 Inches.":
            m 1cud "Wow! 8 Inches? Only a few percentage of guys in the world have one that big."
            m 1cud "8 Inches is a pretty big, not going to lie. It's impressive don't get me wrong, but it can be incredibly painful and not much fun for most girls if you don't know what you're doing."
            m 1cud "If we ever did it, we'd have to take it slow."
            m 1cud "And just remember [player], even if you {i}were{/i} bigger or smaller, I wouldn't think any more or less of you."
            m 1cud "After all, its like breast size for girls. You can't control it."
            m 1cud "There's benefits to all sizes in my opinion!"
        "Around 9 Inches.":
            m 1cud "[player]..."
            m 1cud "I don't want to call you a liar, but I {i}highly{/i} doubt you're that big. You don't have to lie to me."
            m 1cud "But if there's the small chance you're being honest, then I think that's quite a gift. "
            m 1cud "Although sex might be a tad painful ahaha~"

    m 1cud "But just remember, [player], I love you for who you are. Both physically and mentally. Never forget that, okay?"
    return

# Thanks for the new topic mysterylewds
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_feel_horny",
            category=["Romance+"],
            prompt="I feel...Horny",
            unlocked=True,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label player_feel_horny:
    python:
        naked = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_CLOTHES,
                "atomreal_nothing"
        )
        
    m 1cud "[player]!"
    m 1cud "If you're in the mood to... do somethin'."
    m 1cud "I don't mind."
    m 1cud "Ahaha~"
    m 1cud ""
    m 1cud ""
    m 1cud ""
    return

# Thanks for the new topic mysterylewds
init 5 python:
    addEvent(
        Event(
            persistent.event_database,                                  #ToDO
            eventlabel="monika_undress",                                #When complete, lock certain events behind affection range
            unlocked=True,                                              #When complete, Have certain events give affection.
            category=["Romance+"],                                      #Remember to add different dialogue for when someone does it twice or more.
            prompt="Can you... take your clothes off for me?",          #Finish "...I feel horny
            pool=True
        )
    )

label monika_undress:
    
    if random.randint(0,1) and mas_isMoniNormal(higher=True):
        m 2gubsa "[player]!"
        m 2gubsa "I-I dunno If I'm comfortable with that."
        m 2gubsa "But..."
        m 2gubsa "I guess I could take off my top for you."
        m 2gubsa "I'm just a bit self concious about my bust size."
        m 2gubsa "I know a lot of people like a {i}certain{/i} other character for the size of her breasts..."
        m 2gubsa ".{w=0.5}.{w=0.5}.{w=0.5}"
        m 2gubsa "Alright [player], I'll let you see."
        m 2gubsa "Just give me a second..."

        mas_nsfw.wear_birthdaysuit("2gubsa")

        m 2tubfa "..."
        m 2tubfa ".{w=0.5}.{w=0.5}.{w=0.5}"
        m 2tubfa "So what do you think, [player]?"
 
        menu:
            m "So what do you think, [player]?"
            "I think they're absolutely perfect!":
                m 2dubfc "..."
                m 2dubfc "Thank you, [player]. That really means a lot to me."
                m 2dubfc "Its a little less embarrassing now to be honest. I was worried you wouldn't like them."
                m 2dubfc "Guess I was being silly though, right?"
                m 2dubfc "Anytime you want to see them again, let me know. But please respect if I'm not in the mood."
                m 2dubfc "And who knows... maybe I could see you naked one day..."
                m 2dubfc "Ahaha~!"

            "HOLY SHIT! YOU GOT SOME BODACIOUS TATAS!":
                m 2mubfu "[player]!" 
                m 2dubfc "Ahahah thanks I guess!"
                m 2dubfc "I'm happy you think so."
                m 2dubfc "This is a little less embarrassing now to be honest. I was worried you wouldn't like them."
                m 2dubfc "Guess I was being silly though, right?"
                m 2dubfc "Anytime you want to see them again, let me know. But please respect it if I'm not in the mood."
                m 2dubfc "And who knows... maybe I could see you naked one day..."
                m 2dubfc "Ahaha~!"
                
            "Gross...":
                m 2dubfc "I..."
                m 2dubfc "..."
                m 2dubfc "Goodbye."
                
                return "quit"
        
        if mas_shouldKiss(chance = 2) :
            call monika_kissing_motion_short

    elif mas_isMoniBroken(higher=True) and not mas_isMoniNormal():
        m 1mubfa "..."
        m 1lubla "No, [mas_get_player_nickname()]. we're not that deep into our relationship yet, so it feels a little...{w=0.5} {i}too{/i} embarrassing"
        m 5hubfb "Ahaha~"

    elif mas_isMoniUpset(higher=True) and not seen_event("monika_undress"):
        m 2wubft "..."
        m 2lsbfa "Even though we're pretty deep in our realationship at this point, it still feels embarrassing to do..."
        m 2tsbfa "But if you {b}really{/b} want to..."
        
        call mas_clothes_change(naked)

        m 2tubfa "Then i'll do it for you..."
        m 2dsbfc ".{w=0.25}.{w=0.25}."
        m 2etbfu "So?"
        m 5mtbfu "Do you like it?"
        m 5hkbfb "Hehe~"

    elif mas_isMoniLove(higher=True):
        m 1guc "I'm sorry, [player], but i'm not in the mood for it right now."
        m 1nublu "Maybe a bit later, [mas_get_player_nickname()]"
        m 5hublb "Ahaha!~"



    return