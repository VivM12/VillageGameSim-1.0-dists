image bg peaceful_summer = Transform("images/background/peaceful_summer.png", fit="cover")
image bg planning = Transform("images/background/planning.png", fit="cover")
image bg leadership = Transform("images/background/leadership.png", fit="cover")
image bg countdown = Transform("images/background/countdown.png", fit="cover")
image bg member_chat = Transform("images/background/member_chat.png", fit="cover")

# =========================
# TRACKERS
# =========================

default member_satisfaction = 70   # trust / patience of the group
default energy = 70                # leadership stamina
default standing = 50  # external political credibility
default leadership_cohesion = 70  # how well the HC team works together


# =========================
# VARIABLES
# =========================

default role = "hc"

default server_choice = None
default confidence = None
default alliance_goal = None

default wings = None
default member_count = 0

default doctrine = None
default tech_policy = None

default pre_confed = None

# November specific
default server_vibe = None  # gamble/curated

# Leadership & organization tracking
default account_plan_style = None  # strict/balanced/flexible
default discord_quality = None  # excellent/good/messy
default delegation_style = None  # centralized/distributed/reactive
default rules_strictness = None  # strict/balanced/loose
default co_hc_relationship = 70  # Separate from general leadership_cohesion

# Member path specific
default member_status = None  # "core" or "recruit"
default member_loyalty = 50  # Will you stay with this alliance?
default member_confidence = 50  # Trust in leadership?
default member_social = 0  # Friend connections
default member_happiness = 50  # Enjoying yourself?
default member_goals = None  # "competitive"/"strategic"/"social"/"flexible"
default dual_status = None  # "solo"/"dual"/"group"/"team"
default dual_count = 1  # How many duals in your group
default joining_style = None  # "together"/"scout"/"following"/"solo"
default play_style = None  # "off"/"deff"/"hybrid"/"tech"/"wwk"
default got_preferred_role = False  # Did you get what you wanted?
default leadership_impression = None  # "competent"/"messy"/"tryhard"/"chill"
default friend_list = []  # Names of friends made
default helpful_count = 0  # Track being helpful
default leadership_noticed = False  # Have they noticed you?
default member_role = "member"  # Can become "coordinator"
default complained_about_tech = False
default defended_leadership = False
default participated_in_gossip = False

# Friend path specific
default friend_engagement = 50  # How into it are you?
default friend_temptation = 0   # Tempted to join?
default friend_amusement = 50   # Are you entertained?
default friend_name = "Aloha"  # Your friend's name in the alliance

# bookkeeping flags
default lost_members = 0
default time_lost_hours = 0


# =========================
# START
# =========================

label start:
    play music "audio/Comfortable_Mystery.mp3" fadein 1.0
    menu:
        "Play as HC and lead the alliance":
            $ role = "hc"
            jump prolog
        
        "Play as Member":
            $ role = "member"
            jump member_start

        "Play as Friend":
            $ role = "friend"
            jump friend_start


# =========================
# PROLOG
# =========================

label prolog:
    scene bg peaceful_summer

    "It is June.{w=0.3}"

    "For the past few weeks, you already enjoyed the warmer weather, went outside more instead of sitting in front of the PC and your Village Game server has just ended."

    "You look forward to some weeks of not having to look at screens, not having to react to pings, not having to chat so much."

    "But in the back of your mind, you already know that you are going to miss the late nights clicking, the frustrations and joys this game brings."

    "Your fellow leader and you avoided the dreadful topic."

    "Every one of you were careful to assume."

    "You wrote stuff like 'If we play another server' and when the last days were ticking down you got a bit sad that this could be the end."

    "Although you knew it probably wasn't."

    "Two weeks before the WoW finished a new channel plopped up on your Discord."

    "'Next server orga'."

    "And you started already to talk about it."

    "There are ideas floating around, big plans, all the stuff you want to do different this time around."

    "And you know, after a few more weeks on vacation, with sunshine, you will be off again."

    "Fall is coming and the next server is guaranteed."

    scene black
    with fade
    
    "Weeks pass."
    
    "The sun gets lower in the sky."
    
    "Your phone buzzes more often."
    
    with fade

    jump august


# =========================
# SERVER DECISION
# =========================

label august:
    scene bg peaceful_summer
    

    "It's August and break is officially over."

    "Off the deep end we go."

    "Decisions need to be made and there is a question in your leadership channel."

    menu:
        "Go for the big October server. The October server is mostly full of big teching alliances.":
            $ server_choice = "october"
            "You type it out."
            "Hit send."
            "Watch the reactions roll in."
            with dissolve
            jump october_decision

        "Go for the smaller November server. It can be fun or it can be completely dead.":
            $ server_choice = "november"
            jump november_placeholder


label november_placeholder:
    "You consider the November server."

    "This path is not written yet."
    return


# =========================
# OCTOBER SERVER
# =========================

label october_decision:

    scene bg planning
    with fade

    # October server = high pressure from the start
    $ energy -= 15

    "It was a long discussion you had."

    "The October server is the busiest server you can go on."

    "It can be the greatest fun or bring the biggest despair, and you already lived through both."

    menu:
        "You are absolutely confident it was the right decision.":
            $ confidence = "confident"
            "The team is great and you are dedicated to work on your weaknesses."
            "You've said this before."
            "Every server."
            "This time will be different, you think."
            "This time you mean it."

        "You are unsure about the decision.":
            $ confidence = "doubt"
            "It might work out or you might fail and have to call for a mass delete."
            "But only time will tell."
            "The doubt sits in your chest like a stone."
            "You ignore it."
            "You're good at that."

    jump alliance_goal_choice


# =========================
# ALLIANCE GOAL
# =========================

label alliance_goal_choice:
    "You have played the Village Game for a long time and you yearn for a new challenge."

    "For this new server you need to decide what your alliance should play towards."

    menu:
        "Full focus on endgame, we go for level 100. (The Tryhards)":
            $ alliance_goal = "tryhards"
            jump tryhards_intro

        "We play Kingsmaker. (The Kingsmakers)":
            $ alliance_goal = "kingsmakers"
            jump kingsmakers_intro

        "We are just here for the fun. (The Chaos Troop)":
            $ alliance_goal = "chaos"
            jump chaos_intro


# =========================
# TRYHARDS
# =========================

label tryhards_intro:
    "You have reached a decision."

    "You are going for it all."

    "Level 100 is the goal, and you will do everything in your power to make it happen."

    scene bg leadership
    with dissolve
    
    "You post it in leadership chat."
    
    "For a moment, nothing."
    
    "Then:"
    
    menu:
        "Your co-HC sends a gif of someone jumping off a cliff.":
            "You laugh."
            "Send back a fire emoji."
            "Someone else chimes in: 'Let's fucking go.'"
            
            "This is why you do it."
            "These idiots."
            
            $ energy += 5
            $ leadership_cohesion += 5
            $ co_hc_relationship += 8

        "Your co-HC types: 'You sure about this?'":
            "The question hangs there."
            
            "You type back: 'No. But when has that stopped us?'"
            
            "A laugh react appears."
            "Then another."
            
            "It's enough."
            
            $ leadership_cohesion += 3
            $ co_hc_relationship += 5

        "Your co-HC immediately starts planning out loud.":
            "Message after message."
            "Ideas, concerns, logistics, hype."
            
            "You watch the chat scroll."
            "Feel the momentum building."
            
            "You're not in this alone."
            
            $ energy += 3
            $ leadership_cohesion += 5
            $ co_hc_relationship += 6

    with dissolve

    "But first you need the most important thing of all: members."

    "In the past you played in a lot of different sized groups."

    "From 35 to 90 but never beyond that."

    "You have a core group that has followed your leadership for several servers now."

    "But they have reduced in numbers and only about 50 accounts are left."

    menu:
        "Full three wings. (Getting some mass!)":
            $ wings = "three"
            $ member_count = 180
            $ lost_members += 5
            jump tryhards_mass

        "Two wings. (Gonna get some friends!)":
            $ wings = "two"
            $ member_count = 120
            jump tryhards_friends

        "Core group only. (Quality beats all!)":
            $ wings = "core"
            $ member_count = 50
            $ time_lost_hours += 48
            jump tryhards_quality


label tryhards_mass:
    "Some of your members are not happy with the direction you are taking your group. They do not say it outright but doubts are there."

    "You see it in the delayed responses."
    "The way some react with a thumbs up instead of actually engaging."
    "You tell yourself they'll come around."
    "They always do."
    "Right?"

    $ member_satisfaction -= 15
    $ energy -= 10

    "Filling up to 180 accounts is going to be hard."

    "You want to win, and for that you need bodies."
    
    "The message goes out."
    "Now you wait."
    
    scene bg planning
    with fade
    
    "A day passes."

    jump doctrine_event


label tryhards_friends:
    "You announce that you will go for two wings."

    "Everyone is encouraged to reach out to people they played with before."

    "The mood is cautiously optimistic."
    
    "For now, that's enough."
    
    scene bg planning
    with fade
    
    "Time moves on."

    jump doctrine_event


label tryhards_quality:
    "Some of your members are not happy with the direction you are taking your group."

    "You spend days convincing them of your plan."
    "The same arguments."
    "Over and over."
    "In DMs, in voice chat, in carefully worded announcements."
    "You're so tired of explaining yourself."
    "But you do it anyway."

    "There is relief... and doubt."

    $ member_satisfaction -= 10
    $ energy -= 15
    
    jump account_plan_conversations


# =========================
# KINGMAKERS
# =========================

label kingsmakers_intro:
    "You have tried to play for the server win many times."

    "Often, you failed."

    "This time, winning the server is not the main goal."

    "You will be an influence."

    "Whatever you do will decide who wins — whether it is you or someone else."

    menu:
        "One wing (60 members)":
            "The vote does not align with your wish."
            jump kingsmakers_vote_lost

        "Two wings (120 members)":
            "The final vote aligns with your wishes."
            $ member_count = 120
            jump doctrine_event

        "Three wings (180 members)":
            "The vote does not align with your wish."
            jump kingsmakers_vote_lost


label kingsmakers_vote_lost:
    "You get outvoted."

    "Leadership settles on two wings."
    $ member_count = 120
    jump doctrine_event


# =========================
# CHAOS TROOP
# =========================

label chaos_intro:
    "After all these years, you just want to have some fun."

    "Bash some offs."

    "Disturb big pre-mades."

    "You agree to play with a maximum of 60 members."

    $ member_count = 60
    $ wings = "one"
    
    scene bg leadership
    with dissolve
    
    "You post it in leadership chat."
    
    "The reaction is immediate."
    
    menu:
        "Someone sends a gif of chaos and destruction.":
            "Perfect."
            "That's the energy."
            $ energy += 8
            $ leadership_cohesion += 8
            $ co_hc_relationship += 8
            
        "Your co-HC types: 'Finally, a server where we can just mess around.'":
            "You laugh."
            "This is going to be fun."
            $ energy += 5
            $ leadership_cohesion += 5
            $ co_hc_relationship += 8
    
    jump chaos_account_plans

# =========================
# CHAOS-SPECIFIC EVENTS
# =========================

label chaos_account_plans:
    scene bg planning
    with dissolve
    
    "Account planning for chaos is... not really planning."
    
    "You post in Discord: 'Play whatever sounds fun.'"
    
    "Someone asks: 'What if I want to build a wonder?'"
    
    menu:
        "Go for it. Sounds hilarious.":
            $ account_plan_style = "flexible"
            $ member_satisfaction += 8
            "The energy in chat shifts."
            "People are posting ridiculous build ideas."
            "This is going to be beautiful chaos."
            
        "Actually, let's have SOME structure.":
            $ account_plan_style = "balanced"
            $ member_satisfaction += 3
            "You outline some basics."
            "But keep it loose."
    
    $ energy -= 2
    
    jump chaos_discord

label chaos_discord:
    scene bg planning
    with dissolve
    
    "Discord setup for chaos is refreshingly simple."
    
    "You need: a place to post targets, a place to shitpost, and that's it."
    
    menu:
        "Set it up quickly yourself.":
            "Takes you 20 minutes."
            "Three channels. Done."
            $ discord_quality = "good"
            $ energy += 5
            
        "Let the chaos extend to Discord structure.":
            "You create three channels and call it a day."
            "Someone immediately starts posting memes in the wrong one."
            "Perfect."
            $ discord_quality = "messy"
            $ energy += 8
            $ member_satisfaction += 5
    
    jump chaos_name

label chaos_name:
    scene bg planning
    with dissolve
    
    "Alliance name time."
    
    "The suggestions are... exactly what you expected."
    
    menu:
        "The Disturbance":
            $ alliance_name = "The Disturbance"
            "Someone reacts with a Star Wars gif."
            
        "Organized Chaos":
            $ alliance_name = "Organized Chaos"
            "The irony is not lost on anyone."
            
        "We'll Figure It Out":
            $ alliance_name = "We'll Figure It Out"
            "Honesty is a virtue."
            
        "Let chaos decide (random)":
            $ alliance_name = renpy.random.choice(["The Disturbance", "Organized Chaos", "We'll Figure It Out", "The Fun Police", "Questionable Decisions"])
            "You let the vote descend into anarchy."
            "Somehow a decision is made."
    
    $ member_satisfaction += 5
    
    "Everyone loves it."
    "Or at least, no one hates it enough to argue."
    
    jump chaos_targets

label chaos_targets:
    scene bg leadership
    with dissolve
    
    "The question comes up: who are we targeting?"
    
    "This is the most important decision you'll make."
    
    "Who gets to suffer."
    
    menu:
        "Whoever looks most organized and serious.":
            "You're going to ruin someone's spreadsheets."
            "Their perfect plans."
            "Their sleep schedule."
            "Perfect."
            $ standing -= 5
            $ energy += 5
            $ member_satisfaction += 3
            
        "Let's just see who's annoying on the forums.":
            "Chaos is responsive, not planned."
            "You'll know your target when you see them."
            $ energy += 3
            
        "The biggest alliance we can find.":
            "Go big or go home."
            "They won't even see you coming."
            "Until they do."
            "Then it's too late."
            $ standing -= 8
            $ member_satisfaction += 5
            $ energy += 3
    
    "Leadership chat approves."
    
    "This is going to be fun."
    
    jump doctrine_event

# =========================
# ACCOUNT PLAN CONVERSATIONS
# =========================

label account_plan_conversations:

    scene bg planning
    with dissolve

    "Before anything else, there's one thing you can't avoid."

    "You need to talk to people about their account plans."

    if alliance_goal == "tryhards":

        "For a server like this, roles matter."

        "You need offs where offs are needed."
        "You need deff where deff is needed."
        "And you need people willing to sacrifice their preferences for the greater plan."

        "The conversations blur together."

        "Some people are excited."
        "Some are hesitant."
        "Some clearly hoped for something else."

        menu:
            "Push hard for optimal roles":
                "You explain the plan again and again."
                "You emphasize how important every role is."

                $ account_plan_style = "strict"
                $ energy -= 20
                $ member_satisfaction -= 10

            "Try to balance needs and preferences":
                "You spend a lot of time listening."
                "You adjust roles where you can."

                $ account_plan_style = "balanced"
                $ energy -= 15
                $ member_satisfaction -= 5

            "Give more freedom than planned":
                "You let some inefficiencies slide."
                "You tell yourself you'll make up for it later."

                $ account_plan_style = "flexible"
                $ energy -= 10
                $ member_satisfaction += 5


    elif alliance_goal == "kingsmakers":

        "You want to be effective but not rigid."

        "You talk through expectations, but leave room for interpretation."

        "Most people are open to discussion."

        menu:
            "Keep a clear structure":
                "You outline what you roughly need."
                "People adjust without much resistance."

                $ account_plan_style = "balanced"
                $ energy -= 10

            "Let things stay flexible":
                "You allow roles to form organically."
                "It feels less stressful."

                $ account_plan_style = "flexible"
                $ energy -= 5
                $ member_satisfaction += 5


    else:  # chaos

        "You keep it simple."

        "Play what you want."
        "Try weird things."
        "Have fun."

        "The conversations are short."
        "Mostly joking."
        "Mostly excitement."

        $ account_plan_style = "flexible"
        $ energy -= 2
        $ member_satisfaction += 10

    "When it's over, you lean back and stare at the screen."

    if energy < 30:
        "You feel drained. More than you expected."
        "Your back hurts."
        "Your eyes hurt."
        "When did you last eat?"
    elif energy < 60:
        "You feel tired, but it's manageable."
        "Just another part of the job."
        "The part no one sees."
    else:
        "For now, it feels fine."
        "You can handle this."
        "You've handled worse."

    jump discord_setup

# =========================
# DISCORD SETUP
# =========================

label discord_setup:

    scene bg planning
    with dissolve

    "Before the server even starts, the Discord needs to become a place people can actually live in."

    "Channels."
    "Roles."
    "Pings."
    "A structure that doesn't collapse the first time someone asks where to post reports."

    if alliance_goal == "tryhards":
        "For Tryhards, it can't just be pretty."
        "It has to work."

    elif alliance_goal == "kingsmakers":
        "For Kingsmakers, it needs to be flexible."
        "Organized enough to coordinate, loose enough to breathe."

    else:
        "For Chaos, it mostly needs one thing:"
        "A place to laugh when something goes wrong."

    menu:
        "I enjoy setting up Discords. I do it myself.":
            "You open settings and start building."

            "It's oddly soothing."
            "Dragging channels into place."
            "Naming roles."
            "Setting permissions."
            "Watching chaos turn into something that almost makes sense."

            "For a moment, nobody is arguing with you."
            "Nobody wants anything from you."
            "It's just you and a system that can be solved."

            $ discord_quality = "excellent"
            $ energy += 12
            $ member_satisfaction += 3

            "When you're done, the server looks clean."
            "People react with little emotes and short messages of approval."

        "I don't enjoy this. I delegate it to someone else.":
            "You ask someone reliable to take over Discord setup."

            "They answer fast."
            "Relieved, almost."

            "You feel a small weight leave your shoulders."

            $ discord_quality = "good"
            $ energy += 8

            "It's not exactly how you would have done it."
            "But it works."
        
        "I ask my co-HC if they want to do it together.":
            "You hop in voice chat."
            
            "Two hours later, you've reorganized the entire server structure three times."
            
            "Argued about emoji choices."
            
            "Laughed at inside jokes no one else will understand."
            
            "It took twice as long as doing it alone."
            
            "Worth it."
            
            $ discord_quality = "excellent"
            $ energy += 10
            $ leadership_cohesion += 10
            $ co_hc_relationship += 10

        "I half-do it and promise myself I'll finish it later.":
            "You create the basics."
            "The rest can wait."

            "It's a lie you tell yourself every server."

            $ discord_quality = "messy"
            $ energy -= 5
            $ member_satisfaction -= 2

            "Within an hour, someone asks where to post something."
            "Then someone else asks again."

    "With Discord more or less in place, planning moves on."

    jump alliance_name_choice


# =========================
# ALLIANCE NAME
# =========================

default alliance_name = None

label alliance_name_choice:

    scene bg planning
    with dissolve

    "Somewhere between spreadsheets and pings, someone drops the question:"

    "\"So… what are we calling ourselves this time?\""

    "A lot of suggestions scroll by."
    "Most don't survive more than one reaction."

    "Three names keep coming back."

    menu:
        "Iron Pact":
            $ alliance_name = "Iron Pact"
            $ member_satisfaction += 3
            $ standing += 2

            "The name sounds solid."
            "Reliable."
            "People seem comfortable with it."

        "Nightfall":
            $ alliance_name = "Nightfall"
            $ member_satisfaction += 2

            "It's vague enough to mean anything."
            "Which, somehow, works."

        "Loose Formation":
            $ alliance_name = "Loose Formation"
            $ member_satisfaction += 6
            $ standing -= 2

            "There's immediate laughter."
            "Someone makes a joke about this being foreshadowing."

        "Let the vote decide":
            $ alliance_name = renpy.random.choice(["Iron Pact", "Nightfall", "Loose Formation"])
            $ member_satisfaction += 4

            "You lean back and let democracy do its thing."

            "[alliance_name] it is."

    # Safety cap
    $ member_satisfaction = min(member_satisfaction, 100)
    $ standing = min(standing, 100)

    "Once a name exists, the whole thing feels more real."
    "Less like a plan."
    "More like a server you're actually going to start."

    jump rules_expectations

# =========================
# RULES & EXPECTATIONS
# =========================

label rules_expectations:

    scene bg planning
    with dissolve

    "At some point, someone asks what everyone is probably already thinking."

    "\"Do we have rules for this server?\""

    "Not the small stuff."
    "The tone."
    "The expectations."
    "What happens when things go wrong."

    if alliance_goal == "tryhards":

        menu:
            "Set clear, strict expectations":
                "You write everything down."
                "Activity expectations."
                "Behavior."
                "Consequences."

                "It's not fun but it's clear."

                $ rules_strictness = "strict"
                $ member_satisfaction -= 5
                $ standing += 3

            "Keep it firm, but human":
                "You outline expectations without turning them into threats."
                "People nod. Some relax."

                $ rules_strictness = "balanced"
                $ member_satisfaction += 2

    elif alliance_goal == "kingsmakers":

        menu:
            "Lay out a loose framework":
                "You explain what matters and what doesn't."
                "Most people seem comfortable with that."

                $ rules_strictness = "balanced"
                $ member_satisfaction += 3

            "Keep it intentionally vague":
                "You trust leadership to handle issues case by case."
                "It feels flexible. Risky."

                $ rules_strictness = "loose"

    else:  # chaos

        "You keep it simple."

        "\"Don't be a dick.\""
        "\"Talk to us if something's wrong.\""

        "That's it."

        $ rules_strictness = "loose"
        $ member_satisfaction += 5

    "Once expectations are set — clearly or not — the discussion moves on."

    jump early_responsibility

# =========================
# EARLY RESPONSIBILITY
# =========================

label early_responsibility:

    scene bg planning
    with dissolve

    "As the server start gets closer, questions pile up."

    "Who handles what."
    "Who answers pings."
    "Who makes calls when you're not around."

    "You feel the familiar pull between control and trust."

    menu:
        "Keep most responsibility with leadership":
            "You stay central."
            "Most decisions still run through you."

            "It feels safe."
            "It's also a lot."

            $ delegation_style = "centralized"
            $ energy -= 5

        "Delegate early to trusted people":
            "You assign responsibility early."
            "Some things leave your hands entirely."

            "There's friction."
            "But also relief."

            $ delegation_style = "distributed"
            $ energy += 5
            $ member_satisfaction += 3

        "Wait and see how things develop":
            "You delay the decision."
            "There's time. Probably."

            $ delegation_style = "reactive"
            $ energy -= 2

    "Once roles begin to settle, the server finally starts to feel inevitable."

    jump doctrine_event


# =========================
# EVENT FOR EVERYONE – DOCTRINE
# =========================

label doctrine_event:
    "You need to decide how you want to build your alliance."

    menu:
        "Focus on Off. (The Lions roar!)":
            $ doctrine = "off"

        "Focus on Deff. (Let's Turtle!)":
            $ doctrine = "deff"

        "Keep it balanced. (Evenly balanced!)":
            $ doctrine = "balanced"

    "That one was easy."
    
    "The next one won't be."
    
    with dissolve

    jump tech_event


# =========================
# EVENT FOR EVERYONE – TECHS
# =========================

label tech_event:
    "Another decision you have to make is if you will be playing with personal techs."
    
    "Leadership chat explodes."
    
    "Your co-HC has strong opinions."
    "So does the off coordinator."
    "So does literally everyone."
    
    "You've been arguing about this for two days."
    
    "You already know this will go badly."
    "Every option pisses someone off."
    "That's leadership."

    menu:
        "Allow personal techs.":
            $ tech_policy = "personal"
            $ member_satisfaction -= 15
            $ energy -= 20
            "Your decision angers your core group."
            "The people who've followed you for years."
            "The ones who matter most."
            "You try to explain. They're not listening."
            
            "One of your co-HCs leaves three angry emojis."
            "Another goes offline without saying anything."
            
            $ leadership_cohesion -= 10
            $ co_hc_relationship -= 8
            
            if confidence == "confident":
                "You type out an explanation."
                "Delete it."
                "Type it again."
                "You hit send anyway."
                "This is the right call."
                "They'll see."
            else:
                "You're not sure this is right."
                "But the decision is made."

        "Do not allow personal techs.":
            $ tech_policy = "none"
            $ member_satisfaction -= 15
            $ energy -= 20
            "Some of the people you wanted to recruit decide to go with another team."
            
            "Your co-HC sends a thumbs up."
            "It should feel like support."
            "It feels like consolation."
            
            $ leadership_cohesion += 2
            $ co_hc_relationship += 3

        "Alliance-controlled tech accounts.":
            $ tech_policy = "alliance"
            $ member_satisfaction -= 10
            $ energy -= 15
            "Confusion breaks out between old and new members."
            "Leadership chat goes quiet for a moment."
            
            "Then someone types: 'Well, this is gonna be fun to manage.'"
            
            "Someone else: 'We've done worse.'"
            
            "You appreciate the attempt at optimism."
            "Even if nobody believes it."
            
            $ leadership_cohesion += 3
            $ co_hc_relationship += 5

    jump after_tech_bridge

label after_tech_bridge:
    scene bg leadership
    with dissolve

    if member_satisfaction < 40:
        "Leadership feels brittle after the tech debate."
    elif member_satisfaction < 60:
        "Tension lingers, even after the decision is made."
    else:
        "People grumble but they move on."

    "You close Discord."
    "Take a breath."
    "Open it again immediately."

    if energy < 30:
        "You're running on fumes."
    elif energy < 60:
        "You feel the strain settling into your shoulders."
    else:
        "You try to convince yourself it's manageable."

    "A day passes in logistics and message threads."

    "You catch up on pings, answer questions, rewrite the same explanation three different ways."

    $ energy -= 8
    
    "Your phone lights up."
    
    "Not a ping this time."
    
    "A DM."

    with fade
    jump confed_event

# =========================
# EVENT – PRE-SERVER CONFED
# =========================

label confed_event:
    if alliance_goal == "chaos":
        jump chaos_pre_end

    "An alliance you are familiar with reaches out to you."

    "They are smaller but skilled."

    "They could help you win."
    "Or they could stab you in the back week 3."
    "You've seen it before."
    "But you've also seen confeds win servers."

    "You consider a pre-server confed."

    menu:
        "Agree to a pre-server confed.":
            $ pre_confed = "yes"
            $ standing += 10
            "You shake hands digitally."
            "It's done."

        "Politely refuse and stay in touch.":
            $ pre_confed = "later"
            "You keep the door open."
            "Just in case."

        "Refuse completely.":
            $ pre_confed = "no"
            $ standing -= 15
            "The conversation ends awkwardly."
            "You hope you won't regret this."

    scene black
    with fade
    
    "The days blur together."
    
    "More spreadsheets."
    "More pings."
    "More questions you've already answered."
    
    with fade
    
    scene bg countdown
    
    "And then, suddenly—"
    
    "The countdown timer appears in Discord."
    
    "72 hours until server start."
    
    if energy < 40:
        "Your stomach drops."
    else:
        "Here we go."

    jump pre_server_end

# =========================
# CHAOS PRE-SERVER END
# =========================

label chaos_pre_end:
    scene bg countdown
    with fade
    
    "The server start approaches."
    
    "No confeds."
    "No elaborate plans."
    "Just 60 people ready to cause problems."
    
    scene bg leadership
    with dissolve
    
    "Leadership chat is full of memes and terrible ideas."
    
    "Then someone drops it:"
    
    "Someone drops the idea:"
    "'Massive duck formation?'"
    
    "The chat goes quiet."
    
    "Then explodes."
    
    menu:
        "That's the dumbest thing I've ever heard. Let's do it.":
            $ member_satisfaction += 10
            $ energy += 5
            
            "You start planning duck coordinates."
            "This is why you play this game."
            
        "Let's at least make it a GOOD duck. I'll draw it out.":
            $ member_satisfaction += 8
            $ energy -= 3
            
            "You spend an hour on duck village placement."
            "It's weirdly fun."
            
        "Okay no, we need SOME coordination.":
            $ member_satisfaction -= 3
            $ energy -= 5
            
            "You try to be reasonable."
            "Leadership chat boos you."
            "The duck idea gains momentum anyway."
    
    scene bg countdown
    with fade
    
    "The countdown begins."
    
    if energy < 40:
        "You're tired, but excited."
        "No spreadsheets to stress over."
        "Just chaos to unleash."
    else:
        "You feel light."
        "No pressure."
        "No expectations."
        "Just a duck-shaped army about to ruin someone's day."
    
    "Leadership pings one last time."
    
    "Your co-HC: 'Quack quack, motherfuckers.'"
    
    "You laugh."
    
    $ co_hc_relationship += 5
    
    "There is no turning back now."
    
    return


# =========================
# END OF PRE-SERVER
# =========================

label pre_server_end:

    if member_satisfaction < 40:
        "The alliance enters the server fractured."
        "You pretend not to notice."
    elif member_satisfaction < 60:
        "The alliance enters the server tense, but functional."
        "Functional is good enough."
        "It has to be."
    else:
        "The alliance enters the server united."
        "Against all odds."
        "You let yourself feel proud."
        "Just for a moment."

    if energy < 30:
        "You start the server already exhausted. All the discussion you have to have already tired you out and you consider if all of this is worth it."
        "The answer should be no."
        "But you click 'ready' anyway."
    elif energy < 60:
        "You start the server tired. The discussions and conflicts took their toll. But you remember all the fun this game can bring."
        "The highs are worth the lows."
        "Usually."
    else:
        "You feel ready. At least for now."
        "Pre-server is always easier than the real thing."
        "You know what's coming."

    "The server start date is announced."
    "Leadership chat pings."
    
    if energy < 30:
        "Someone posts: 'Ready?'"
        
        "You type: 'No.'"
        
        "Three laugh reacts appear immediately."
        
        "Then someone else: 'Same. Let's do it anyway.'"
        
    elif energy < 60:
        "Someone posts a hype gif."
        
        "Your co-HC adds: 'Here we go again.'"
        
        "You add a salute emoji."
        
        "It's tradition at this point."
        
    else:
        "The usual pre-server energy fills leadership chat."
        
        "Jokes."
        "Last-minute panic."
        "Someone reminding everyone to sleep."
        
        "No one will sleep."
        "You all know this."
    
    "There is no turning back now."

    return


# =========================
# MEMBER ROUTE START
# =========================

label member_start:
    scene bg peaceful_summer
    
    "It's August."
    
    "Someone you played with before reaches out."
    
    "They're putting together an alliance for a new server starting in fall."
    
    menu:
        "You've played with this group for years. (Core member)":
            $ member_status = "core"
            $ member_loyalty = 70
            "You know these people."
            "You've been through servers with them before.
            The highs, the lows and everything in between. Of course you will join!"
            
        "You're joining this group for the first time. (Recruit)":
            $ member_status = "recruit"
            $ member_loyalty = 50
            "You have known of this group for a long time now. They are awesome."
            "Now they want you in the main group. There is really no question what you will do..."
    
    jump member_dual_setup

label member_dual_setup:
    scene bg peaceful_summer
   
    
    "An important question:"
    
    "Are you playing solo or with others?"
    
    menu:
        "Playing solo (just me)":
            $ dual_status = "solo"
            $ dual_count = 1
            $ member_social = 0
            $ joining_style = "solo"
            
            "You're on your own this server."
            "Flying solo has its advantages."
            
        "Playing dual":
            $ dual_status = "dual"
            $ dual_count = 2
            $ member_social = 10
            
            "You and your dual partner."
            "A team of two."
            
            jump member_dual_joining
            
        "Playing in a small group (3-4 people)":
            $ dual_status = "group"
            $ dual_count = renpy.random.randint(3, 4)
            $ member_social = 15
            
            "Your crew."
            "[dual_count] of you, ready to roll."
            
            jump member_dual_joining
            
        "Playing in a bigger team (5+ people)":
            $ dual_status = "team"
            $ dual_count = renpy.random.randint(5, 8)
            $ member_social = 20
            
            "Your squad."
    
            jump member_dual_joining
    
    jump member_playstyle

label member_dual_joining:
    if dual_status != "solo":
        "How are you joining?"
        
        menu:
            "We're all joining together":
                $ joining_style = "together"
                $ member_confidence = 55
                "Safety in numbers."
                "If it's bad, you leave together."
                
            "I'm checking it out first, then bringing them in":
                $ joining_style = "scout"
                $ member_confidence = 45
                "They're trusting your judgment."
                "No pressure."
                
            "They're already in, I'm joining them":
                $ joining_style = "following"
                $ member_confidence = 60
                "Your people are already there."
                "They say it's good."
    
    jump member_playstyle


label member_playstyle:
    scene bg planning
   
    
    "What's your preferred playstyle this server?"
    
    "What you WANT to play."
    
    menu:
        "Off (offensive, raiding, hammers)":
            $ play_style = "off"
            "You live for the attacks, you enjoy the hour long op sends."
       
            
        "Deff (defensive, protecting, support)":
            $ play_style = "deff"
            "You love playing deff!"
            
        "Hybrid (flexible, both off and deff)":
            $ play_style = "hybrid"
            "Adapt to what's needed."
            "Jack of all trades."
            
        "WWK Builder":
            $ play_style = "wwk"
            "You want THE account."
            "The one that matters most."
    
    jump member_expectations

label member_expectations:
    scene bg planning
   
    
    "What are you hoping for this server?"
    
    menu:
        "I want to compete. Push hard. Go for the win.":
            $ member_goals = "competitive"
            "You're here to prove yourself."
            "To see how far you can push."
            
        "I want strategic gameplay. Politics and influence.":
            $ member_goals = "strategic"
            "You like the chess game."
            "The alliances, the betrayals, the plays."
            
        "I'm here for my friends and good times.":
            $ member_goals = "social"
            "The memories matter more than the rank."
            "Good vibes, good people."
            
        "I'm flexible. Whatever the group needs.":
            $ member_goals = "flexible"
            "You'll adapt."
            "Just looking for a solid group."
    
    jump member_alliance_reveal

label member_alliance_reveal:
    scene bg planning
   
    
    "A few days later you get a message."
    
    "\"Okay, so here's the plan...\""
    
    # Randomize what the alliance is actually doing
    $ alliance_goal = renpy.random.choice(["tryhards", "kingsmakers", "chaos"])
    
    if alliance_goal == "tryhards":
        "\"We're going full send. Level 100 push.\""
        
        if member_goals == "competitive":
            "Your eyes light up."
            "This is exactly what you wanted."
            $ member_loyalty += 15
            $ member_confidence += 10
            $ member_happiness += 10
            
        elif member_goals == "social":
            "Your heart sinks a little."
            "You were hoping for something more relaxed."
            $ member_loyalty -= 10
            $ member_happiness -= 10
            
        elif member_goals == "strategic":
            "Interesting."
            "Not quite what you expected, but could work."
            $ member_loyalty += 0
            
        else:  # flexible
            "You can work with that."
            $ member_loyalty += 5
            
    elif alliance_goal == "kingsmakers":
        "\"We're playing kingmaker. Politics, strategy, influence.\""
        
        if member_goals == "strategic":
            "Perfect."
            "This is your game."
            $ member_loyalty += 15
            $ member_confidence += 10
            $ member_happiness += 10
            
        elif member_goals == "competitive":
            "You were hoping to actually WIN."
            "Not just... help someone else win."
            $ member_loyalty -= 5
            $ member_happiness -= 5
            
        elif member_goals == "social":
            "Could be fun."
            "As long as it doesn't get too serious."
            $ member_loyalty += 3
            
        else:  # flexible
            "You can work with that."
            $ member_loyalty += 5
            
    else:  # chaos
        "\"We're just here to have fun and cause problems.\""
        
        if member_goals == "social":
            "You grin."
            "Your people."
            $ member_loyalty += 15
            $ member_confidence += 10
            $ member_happiness += 10
            
        elif member_goals == "competitive":
            "You try not to show disappointment."
            "You wanted to compete."
            "Not just... mess around."
            $ member_loyalty -= 10
            $ member_happiness -= 10
            
        elif member_goals == "strategic":
            "This feels like a waste."
            "But maybe you can make something of it."
            $ member_loyalty -= 5
            
        else:  # flexible
            "Could be fun."
            $ member_loyalty += 5
    
    menu:
        "I'm in. Let's do this.":
            if member_loyalty >= 50:
                "You don't hesitate."
            else:
                "You say it anyway."
                "Even if you're not sure."
            jump member_generate_alliance
            
        "I'm in, but I hope this works out.":
            "Your friend picks up on the hesitation."
            "\"Trust me, it'll be good.\""
            $ member_loyalty -= 3
            jump member_generate_alliance
            
        "Actually... I think I'll sit this one out.":
            "Your friend is disappointed."
            "But understands."
            jump member_declined

label member_declined:
    "You decide to sit this server out."
    
    "Maybe next time."
    
    return

label member_generate_alliance:
    # Generate HC decisions that member will experience
    
    # Randomize HOW leadership runs things
    $ account_plan_style = renpy.random.choice(["strict", "balanced", "flexible"])
    $ discord_quality = renpy.random.choice(["excellent", "good", "messy"])
    $ delegation_style = renpy.random.choice(["centralized", "distributed", "reactive"])
    $ rules_strictness = renpy.random.choice(["strict", "balanced", "loose"])
    
    # Doctrine weighted by alliance goal
    if alliance_goal == "tryhards":
        $ doctrine = renpy.random.choice(["off", "balanced", "balanced"])
    elif alliance_goal == "chaos":
        $ doctrine = renpy.random.choice(["off", "off", "balanced"])
    else:
        $ doctrine = renpy.random.choice(["off", "deff", "balanced"])
    
    # Tech policy weighted by alliance goal
    if alliance_goal == "tryhards":
        $ tech_policy = renpy.random.choice(["alliance", "alliance", "none", "personal"])
    else:
        $ tech_policy = renpy.random.choice(["personal", "none", "alliance"])
    
    # Generate alliance name
    $ alliance_name = renpy.random.choice(["Iron Pact", "Nightfall", "Loose Formation", "The Vanguard", "Storm Front"])
    
    # Generate leadership cohesion (affects member experience)
    $ leadership_cohesion = renpy.random.randint(40, 85)
    
    jump member_discord_join

# Placeholder for next sections - to be continued
label member_discord_join:
    scene bg member_chat
    with fade
    
    "You get the Discord invite."
    
    if member_status == "core":
        "You join the server."
        "See the familiar names."
        "Welcome back messages pop up."
        
        $ member_social += 5
        $ member_confidence += 5
        
        "Home."
        "Sort of."
        
    else:  # recruit
        "You join the server."
        
        "So many channels."
        "So many people you don't know."
        
        "Deep breath."
    
    jump member_first_impression

label member_first_impression:
    # Experience the discord_quality
    
    if discord_quality == "excellent":
        "The Discord is... actually really well organized."
        
        "Clear channels."
        "Good descriptions."
        "Everything makes sense."
        
        $ member_confidence += 8
        $ leadership_impression = "competent"
        
        "These people know what they're doing."
        
    elif discord_quality == "good":
        "The Discord is decent."
        
        "Some channels could be clearer."
        "But you can figure it out."
        
        $ member_confidence += 3
        
    else:  # messy
        "The Discord is... chaos."
        
        "Channels everywhere."
        "No descriptions."
        "Three channels that seem to serve the same purpose."
        
        $ member_confidence -= 5
        $ member_happiness -= 3
        $ leadership_impression = "messy"
        
        "This is going to be interesting."
    
    jump member_general_chat

label member_general_chat:
    scene bg member_chat
   
    
    "General chat is active."
    
    "People talking about builds."
    "Sharing memes."
    "Discussing."
    
    if member_status == "core":
        "You recognize most of the names."
        
        "You jump in naturally."
        
        $ member_social += 8
        
    else:
        "You don't know most of these people."
        
        menu:
            "Introduce yourself":
                "You post a quick intro."
                
                "A few people welcome you."
                "Someone asks what you're planning to play."
                
                $ member_social += 8
                $ member_happiness += 5
                
                "Good start."
                
            "Lurk and read":
                "You watch the conversation."
                
                "Try to get a feel for the vibe."
                
                $ member_social += 2
                
                "You'll speak up when you have something to say."
                
            "Find your group and chat with them":
                if dual_status != "solo":
                    "You DM your people."
                    
                    "\"So... what do we think?\""
                    
                    $ member_social += 5
                    
                    "You'll get to know the others later."
                else:
                    "You're solo."
                    "Guess you'll just observe."
                    $ member_social += 1
    
    "A few days pass."
    
    "You're settling in."
    "Getting to know people."
    
    if member_status == "recruit" and member_social >= 10:
        "You're making friends."
        "Starting to feel like part of the group."
    
    "Then you get a message."
    
    jump member_account_talk

label member_account_talk:
    scene bg leadership
    with fade
    
    "A HC messages you."
    
    "You get a message."

    if delegation_style == "centralized":
     "It's one of the HCs directly."
    elif delegation_style == "distributed":
     "It's someone assigned to handle this."
    else:
     "Someone from leadership reaches out."
    
    "\"Hey, we need to talk about your account plans.\""
    
    
    # Now branch based on account_plan_style
    
    if account_plan_style == "strict":
        jump member_account_strict
    elif account_plan_style == "balanced":
        jump member_account_balanced
    else:
        jump member_account_flexible

label member_account_strict:
    "They don't waste time."
    
    "\"Here's what we need:\""
    
    "They send you a clear outline of their idea for the alliance."
    
    # Determine what they want based on doctrine
    python:
        if doctrine == "off":
            hc_wants = renpy.random.choice(["off", "off", "hybrid"])
        elif doctrine == "deff":
            hc_wants = renpy.random.choice(["deff", "deff", "hybrid"])
        else:
            hc_wants = renpy.random.choice(["off", "deff", "hybrid"])
    
    "\"We need you on [hc_wants].\""
    
    if hc_wants == play_style:
        # PERFECT MATCH
        "You smile."
        
        "That's exactly what you wanted to play."
        
        $ got_preferred_role = True
        $ member_loyalty += 10
        $ member_happiness += 10
        $ member_confidence += 5
        
        menu:
            "Perfect, I was planning that anyway.":
                "\"Great. That's settled then.\""
                
                "Easy."
                
            "Yeah, I can do that.":
                "\"Good. Check the sheet for details.\""
    
    else:
        # CONFLICT
        "Your stomach sinks."
        
        "That's not what you wanted to play."
        
        "You wanted [play_style]."
        
        menu:
            "Sure, I can do that.":
                $ got_preferred_role = False
                $ member_loyalty -= 10
                $ member_happiness -= 15
                $ member_confidence -= 5
                
                "You agree."
                "Even though it hurts."
                
                "\"Great. Thanks for being flexible.\""
                
                if dual_status != "solo":
                    "You message your group."
                    "\"We're playing [hc_wants].\""
                    "The response is... not enthusiastic."
                    
                    $ member_social -= 3
                
            "Actually, I was planning to play [play_style].":
                "There's a pause."
                
                $ member_confidence -= 3
                
                if member_status == "core":
                    "\"Look, we've played together before.\""
                    "\"You know how this works.\""
                    
                    menu:
                        "Fine. I'll play [hc_wants].":
                            $ got_preferred_role = False
                            $ member_loyalty -= 12
                            $ member_happiness -= 12
                            
                            "You cave."
                            
                        "No, I really need to play [play_style] this server.":
                            jump member_strict_pushback
                else:
                    "\"We need [hc_wants]. That's the plan.\""
                    
                    menu:
                        "Okay, I understand.":
                            $ got_preferred_role = False
                            $ member_loyalty -= 15
                            $ member_happiness -= 15
                            $ member_confidence -= 8
                            
                            "You give in."
                            "You're new here."
                            "Don't want to make waves."
                            
                        "I'm not sure this is going to work for me.":
                            $ member_loyalty -= 20
                            $ member_confidence -= 10
                            
                            "The conversation gets awkward."
                            
                            "\"Well... think about it.\""
                            
                            "They go offline."
                            
                            if member_loyalty < 30:
                                jump member_early_doubt
            
            "I need to think about this.":
                $ member_loyalty -= 5
                $ member_confidence -= 5
                
                "\"Don't take too long. We need to finalize plans.\""
                
                "You stall."
                "They're not happy about it."
    
    jump member_after_account_talk

label member_strict_pushback:
    "The conversation gets tense."
    
    "\"Everyone has to sacrifice something.\""
    "\"That's how this works.\""
    
    menu:
        "Okay, fine. [hc_wants] it is.":
            $ got_preferred_role = False
            $ member_loyalty -= 10
            $ member_happiness -= 10
            "You surrender."
            
        "Then maybe I'm not the right fit for this alliance.":
            $ member_loyalty -= 25
            $ member_confidence -= 15
            
            "Silence."
            
            "\"That's your call.\""
            
            if member_loyalty < 30:
                jump member_early_doubt
    
    jump member_after_account_talk

label member_account_balanced:
    "They start with a question."
    
    "\"What were you thinking for account plans?\""
    
    "You tell them: [play_style]."
    
    if dual_status != "solo":
        "You mention you're playing with [dual_count] duals total."
    
    "They think for a moment."
    
    # 70% chance they accommodate
    python:
        if renpy.random.random() < 0.7:
            hc_response = "accommodate"
        else:
            hc_response = "push_back"
    
    if hc_response == "accommodate":
        "\"That works. We can fit that in.\""
        
        $ got_preferred_role = True
        $ member_loyalty += 10
        $ member_happiness += 10
        $ member_confidence += 8
        
        "Relief washes over you."
        
        "This might actually be good."
        
    else:
        python:
            if play_style == "off":
                other_style = "deff"
            elif play_style == "deff":
                other_style = "off"
            else:
                other_style = renpy.random.choice(["off", "deff"])
        
        "\"Hmm. We're actually pretty heavy on [play_style] already.\""
        "\"Could you consider [other_style] instead?\""
        
        menu:
            "Yeah, I can be flexible.":
                $ got_preferred_role = False
                $ member_loyalty -= 5
                $ member_happiness -= 5
                $ member_confidence += 3
                
                "You adapt."
                "Not ideal, but they asked nicely."
                
            "I'd really prefer to stick with [play_style].":
                "\"Let me see what I can do.\""
                
                "They go quiet for a bit."
                
                "Then:"
                "\"Okay, you can play [play_style]. But we might need you to flex if things change.\""
                
                $ got_preferred_role = True
                $ member_loyalty += 5
                $ member_confidence += 5
                
                "Fair enough."
    
    jump member_after_account_talk

label member_account_flexible:
    "They're casual about it."
    
    "\"Play whatever you want.\""
    
    if dual_status != "solo":
        "\"All [dual_count] of you.\""
    
    "\"Just have fun.\""
    
    $ got_preferred_role = True
    $ member_loyalty += 8
    $ member_happiness += 12
    $ member_confidence += 5
    
    "You grin."
    
    "This is exactly what you needed to hear."
    
    if alliance_goal == "chaos":
        "Makes sense for a chaos alliance."
    else:
        "Interesting."
        if alliance_goal == "tryhards":
            "For a tryhard alliance, this is... loose."
            $ leadership_impression = "chill"
        else:
            "Very relaxed."
            $ leadership_impression = "chill"
    
    jump member_after_account_talk

label member_early_doubt:
    scene bg planning
   
    "You close Discord."
    
    "Stare at the ceiling."
    
    "This might have been a mistake."
    
    if dual_status != "solo":
        "You message your group."
        
        "\"I'm not sure about this.\""
        
        python:
            team_agrees = renpy.random.randint(0, dual_count)
        
        if team_agrees > dual_count // 2:
            "Most of them feel the same way."
            
            "\"Should we look for something else?\""
        else:
            "They want to give it more time."
            
            "\"We're already here. Let's see how it goes?\""
    
    menu:
        "Give it more time":
            $ member_loyalty += 5
            "You'll stick it out."
            "For now."
            jump member_after_account_talk
            
        "Leave now":
            jump member_leaves_early
    
    jump member_after_account_talk

label member_leaves_early:
    "You've made your decision."
    
    "You message the leadership."
    
    "\"Hey, I don't think this is the right fit. Thanks anyway.\""
    
    if member_status == "core":
        "The response is surprised."
        "Disappointed."
        "You've been with them before."
    else:
        "\"Okay. Thanks for letting us know.\""
    
    if dual_status != "solo":
        "Your group leaves with you."
    
    "You leave the Discord."
    
    "Back to looking."
    
    return

label member_after_account_talk:
    scene bg planning
    
    
    if got_preferred_role:
        "You're playing what you wanted."
        "That's a win."
    else:
        "You're not playing what you wanted."
        "But you're here."
    
    if dual_status != "solo":
        "You debrief with your group."
        
        if got_preferred_role:
            "Everyone seems happy."
            $ member_social += 5
        else:
            "The mood is... mixed."
            $ member_social += 2
    
    "A few more days pass."
    
    jump member_alliance_name_vote

label member_alliance_name_vote:
    scene bg planning
    
    
    "Leadership posts in announcements."
    
    "\"Time to vote on an alliance name.\""
    
    "Three options."
    
    # Use the generated name plus two alternatives
    python:
        options = [alliance_name]
        other_names = ["Iron Pact", "Nightfall", "Loose Formation", "The Vanguard", "Storm Front", "Rising Tide", "The Collective"]
        other_names = [n for n in other_names if n != alliance_name]
        options.extend(renpy.random.sample(other_names, 2))
        renpy.random.shuffle(options)
    
    "The options are:"
    "[options[0]]"
    "[options[1]]"
    "[options[2]]"
    
    menu:
        "Vote for [options[0]]":
            "You cast your vote."
            
        "Vote for [options[1]]":
            "You cast your vote."
            
        "Vote for [options[2]]":
            "You cast your vote."
    
    $ member_happiness += 3
    $ helpful_count += 1
    
    "At least you get to participate in something."
    
    "The votes come in."
    
    "The winner: [alliance_name]."
    
    if leadership_cohesion > 60:
        "Everyone seems happy with it."
    else:
        "Some people are complaining."
        "But it's done."
    
    jump member_social_moment

label member_social_moment:
    scene bg planning
    
    
    "Over the next few days, you get to know people better."
    
    "General chat is active."
    
    menu:
        "Be active in chat, make friends":
            "You post regularly."
            "Share ideas."
            "Make jokes."
            
            $ member_social += 10
            $ member_happiness += 8
            $ helpful_count += 1
            
            "You're becoming part of the community."
            
        "Stay mostly quiet, observe":
            "You lurk."
            "Watch the dynamics."
            
            $ member_social += 3
            
            "You'll speak when you have something important to say."
            
        "Focus on your group, ignore general":
            if dual_status != "solo":
                "You stick with your people."
                
                $ member_social += 5
                
                "The rest of the alliance is just... noise."
            else:
                "You're solo."
                "Not much to focus on."
    
    jump member_doctrine_announcement

label member_doctrine_announcement:
    scene bg planning
        
    "Leadership announces the doctrine."
    
    if doctrine == "off":
        "\"We're focusing on offense.\""
        
        if play_style == "off" or play_style == "hybrid":
            "You nod."
            "That works for you."
            $ member_confidence += 3
        else:
            "You're on deff."
            "This means you'll will get a lot of points and probably will never have enough troops."
    
    elif doctrine == "deff":
        "\"We're focusing on defense.\""
        
        if play_style == "deff" or play_style == "hybrid":
            "Good."
            "You can work with that."
            $ member_confidence += 3
        else:
            "You're on off."
            "So you will have to crate your own fun."
    
    else:
        "\"We're staying balanced.\""
        
        "Safe choice."
        
        $ member_confidence += 2
    
    "Some discussion in general."
    "But nothing dramatic."
    
    "Yet."
    
    jump member_tech_drama

label member_tech_drama:
    scene bg member_chat
   
    
    "Then comes the announcement."
    
    "The one everyone was waiting for since this question has been repeated: are we playing with techs? 
     Techs are a difficult topic in this game. Most people do it nowadays but some are hardliner on it."
    
    if tech_policy == "personal":
        "\"Personal techs are allowed.\""
        
        "General chat explodes."
        
        "Half the people are furious."
        "The other half are celebrating."
        
        if member_status == "core":
            "You are absolutely shocked."
        
        jump member_tech_drama_choice
        
    elif tech_policy == "none":
        "\"No personal techs. Alliance only.\""
        
        "Some people are relieved."
        "Others are disappointed."
        
        if play_style == "tech":
            "Your entire plan just collapsed."
            $ member_loyalty -= 15
            $ member_happiness -= 15
            
            "You wanted to play tech."
            "Now you can't."
        
        jump member_tech_drama_choice
        
    else:  # alliance
        "\"Tech accounts will be run by alliance leadership.\""
        
        "Some confusion."
        "Some debate."
        
        "But not as explosive as it could have been."
        
        jump member_tech_drama_choice

label member_tech_drama_choice:
    "The discussion gets heated."
    
    "People are @ing leadership."
    "Demanding explanations."
    
    menu:
        "Defend leadership's decision":
            $ defended_leadership = True
            $ member_loyalty += 8
            $ member_confidence += 5
            $ member_social -= 5
            $ helpful_count += 2
            
            "You post in support."
            
            "Some people agree with you."
            "Others call you a bootlicker."
            
            "Whatever."
            
        "Join the complaints":
            $ complained_about_tech = True
            $ member_loyalty -= 5
            $ member_social += 8
            
            "You vent your frustration."
            
            "It feels good."
            "Others agree with you."
            
            "You're bonding through shared anger."
            
        "Stay completely out of it":
            $ member_social += 2
            
            "You mute the channel."
            
            "Let them fight."
            
            "You'll check back when the dust settles."
    
    if dual_status != "solo":
        "Your group is discussing it in private."
        
        if got_preferred_role:
            "At least you got your roles."
            "That's something."
        else:
            "This on top of the role situation."
            "Some of your people are getting frustrated."
            
            $ member_loyalty -= 3
    
    jump member_gossip_period

label member_gossip_period:
    scene bg planning
        
    "Leadership goes quiet for a few days."
    
    "Making decisions behind closed doors."
    
    "General chat fills the void."
    
    "With speculation."
    
    menu:
        "Participate in the speculation":
            $ participated_in_gossip = True
            $ member_social += 8
            
            "You share theories."
            "Make guesses."
            
            "It's entertaining."
            
        "Defend leadership from speculation":
            $ defended_leadership = True
            $ member_loyalty += 5
            $ member_social -= 3
            $ helpful_count += 1
            
            "You remind people that leadership is working hard."
            
            "Not everyone appreciates it."
            
        "Ignore the drama":
            $ member_social += 2
            
            "You focus on your own prep."
    
    # Check if member might get noticed for promotion
    if helpful_count >= 4 and not leadership_noticed:
        jump member_leadership_offer
    
    jump member_countdown

label member_leadership_offer:
    $ leadership_noticed = True
    
    "You get a message."
    
    "\"Hey, we've noticed you've been really helpful.\""
    
    "\"Would you want to help out during the server?\""
    
    menu:
        "Yes! I'd love to help.":
            $ member_role = "coordinator"
            $ member_loyalty += 15
            $ member_confidence += 10
            $ member_happiness += 10
            
            "You just got promoted."
            
            "Kind of."
            
            "You're still a member."
            "But now you're a member with responsibilities."
            
        "I'm good just being a member.":
            $ member_loyalty += 3
            
            "\"No worries. Just wanted to offer.\""
            
            "You appreciate being asked."
            
        "I don't think I'm qualified.":
            $ member_confidence -= 3
            
            "\"We think you are. Think about it.\""
    
    jump member_countdown

label member_countdown:
    scene bg countdown
    with fade
    
    "The countdown appears."
    
    "72 hours until server start."
    
    "General chat shifts energy."
    
    "Less planning."
    "More hype."
    
    if member_role == "coordinator":
        "You're in coordination channels now."
        "Seeing the last-minute preparations."
        "It's chaotic."
        "But exciting."
    
    if member_loyalty < 30:
        jump member_final_doubt
    else:
        jump member_final_ready

label member_final_doubt:
    "You stare at the countdown."
    
    "Are you really doing this?"
    
    if got_preferred_role == False:
        "Playing a style you didn't want."
    
    if member_happiness < 40:
        "You're not even having fun yet."
    
    if dual_status != "solo":
        "You message your group."
        
        "\"Are we sure about this?\""
        
        python:
            team_doubts = renpy.random.randint(0, dual_count)
        
        if team_doubts > dual_count // 2:
            "Most of them have doubts too."
            
            "\"Maybe we should look elsewhere?\""
        else:
            "They want to push through."
            
            "\"We're here now. Let's give it a shot.\""
    
    menu:
        "Stick it out. Give it a real chance.":
            $ member_loyalty += 10
            
            "You're committed now."
            "For better or worse."
            
            jump member_final_ready
            
        "Leave and find something else":
            jump member_leaves_late
    
    jump member_final_ready

label member_leaves_late:
    "You've made your decision."
    
    "You message leadership."
    
    "\"Hey, I'm sorry but I'm going to bow out.\""
    
    if member_status == "core":
        "They're disappointed."
        "You've been with them for years."
        "This hurts."
    else:
        "\"That's unfortunate. Good luck.\""
    
    if dual_status != "solo":
        python:
            team_leaving = renpy.random.randint(1, dual_count)
        
        "[team_leaving] of your group leaves with you."
        
        if team_leaving < dual_count:
            "The others stay."
            "Your group splits."
    
    "You leave the Discord."
    
    "72 hours later, the server starts."
    
    "Without you."
    
    return

label member_final_ready:
    scene bg countdown
    with fade
    
    if member_loyalty > 70 and member_happiness > 60:
        # HYPED
        "You're excited."
        
        "The server is about to start."
        
        if got_preferred_role:
            "Playing what you wanted."
        
        if member_social > 15:
            "With people you like."
        
        "This could be great."
        
    elif member_loyalty > 50:
        # CAUTIOUSLY OPTIMISTIC
        "You're... ready?"
        
        "As ready as you'll be."
        
        "It might work out."
        "It might not."
        
        "But you're here."
        
    else:
        # RESIGNED
        "You're going through with it."
        
        "Not excited."
        "Not really."
        
        "But you committed."
        
        "So here you are."
    
    if dual_status != "solo":
        "Your group is ready."
        
        if member_social > 15:
            "You've made friends in the alliance too."
        else:
            "You have each other."
            "That's enough."
    
    "The countdown hits zero."
    
    "Server start."
    
    "Here we go."
    
    return

# =========================
# FRIEND ROUTE START
# =========================

label friend_start:
    scene bg peaceful_summer
    
    "It's August."
    
    "Your friend messages you."
    
    "They're putting together an alliance for the next server."
    
    "\"You should join the Discord. Hang out with us.\""
    
    menu:
        "Who's your friend?":
            pass
    
    $ friend_name = renpy.input("What's your friend's name?", default="Aloha")
    $ friend_name = friend_name.strip() or "Aloha"
    
    "[friend_name]."
    
    "You've played with them before."
    "Good times."
    
    "But this server?"
    
    "You're not really feeling it."
    
    menu:
        "Why are you joining the Discord if you're not playing?":
            pass
    
    menu:
        "I'm bored and want to see what happens":
            $ friend_engagement = 60
            $ friend_amusement = 60
            "Might as well watch the chaos."
            
        "Moral support for my friend":
            $ friend_engagement = 50
            "They're gonna need it."
            "[friend_name] always gets stressed during planning."
            
        "FOMO - I want to see if it looks fun":
            $ friend_engagement = 55
            $ friend_temptation = 10
            "Maybe you'll change your mind."
            "Probably not."
            "But maybe."
            
        "Just want to hang out in chat":
            $ friend_engagement = 45
            $ friend_amusement = 55
            "No pressure."
            "No commitment."
            "Just vibes."
    
    jump friend_discord_join

label friend_discord_join:
    scene bg member_chat
    
    
    "You join the Discord."
    
    "\"Friend\" role."
    "Perfect."
    
    "You can see everything."
    "But no one expects anything from you."
    
    "It's liberating."
    
    "[friend_name] messages you immediately."
    "\"Thanks for being here lol\""
    
    menu:
        "Send a supportive message":
            $ friend_engagement += 5
            "\"Got your back!\""
            
        "Send a meme":
            $ friend_amusement += 5
            "You send something stupid."
            "They react with a laugh emoji."
            
        "\"No problem, this should be entertaining\"":
            $ friend_amusement += 3
            "\"Oh it will be\""
    
    jump friend_watch_planning

label friend_watch_planning:
    scene bg member_chat
   
    
    "Over the next few days, you watch."
    
    "People joining."
    "Introductions."
    "Build discussions."
    "The usual pre-server energy."
    
    "General chat is active."
    
    menu:
        "Participate casually in chat":
            $ friend_engagement += 8
            $ friend_amusement += 5
            
            "You post occasionally."
            "Share some opinions on builds."
            "Make jokes."
            
            "People seem to like you."
            
        "Lurk and read everything":
            $ friend_engagement += 3
            $ friend_amusement += 8
            
            "You're a silent observer."
            "Reading every message."
            "This is better than reality TV."
            
        "Only talk to your friend in DMs":
            $ friend_engagement += 5
            
            "You and [friend_name] have your own running commentary."
            "On everything happening in the alliance."
    
    jump friend_alliance_announcement

label friend_alliance_announcement:
    scene bg member_chat
    
    
    # Generate what the alliance is doing
    $ alliance_goal = renpy.random.choice(["tryhards", "kingsmakers", "chaos"])
    
    "Leadership announces the alliance goal."
    
    if alliance_goal == "tryhards":
        "\"We're going for level 100.\""
        
        "General chat gets serious."
        "People talking about commitment."
        "Activity requirements."
        
        "You're glad you're not playing."
        
    elif alliance_goal == "kingsmakers":
        "\"We're playing kingmaker this server.\""
        
        "Some debate in chat."
        "Politics talk."
        
        "Interesting."
        
    else:  # chaos
        "\"We're just here for chaos and fun.\""
        
        "General chat immediately fills with memes."
        
        $ friend_amusement += 10
        
        "This is going to be entertaining."
    
    "[friend_name] DMs you."
    
    "\"What do you think?\""
    
    menu:
        "Sounds like a solid plan":
            $ friend_engagement += 3
            "\"I think so too\""
            
        "I don't know, seems ambitious":
            "\"Yeah... we'll see\""
            "[friend_name] sounds tired already."
            
        "Honestly? I'm just here for the drama":
            $ friend_amusement += 5
            "\"LOL fair\""
    
    jump friend_watch_drama

label friend_watch_drama:
    scene bg member_chat
    
    
    "Days pass."
    
    "You watch the alliance take shape."
    
    # Generate some drama scenarios
    $ tech_policy = renpy.random.choice(["personal", "none", "alliance"])
    
    "Then it happens."
    
    "The tech announcement."
    
    "General chat explodes."
    
    if tech_policy == "personal":
        "People are furious about personal techs being allowed."
    elif tech_policy == "none":
        "People are mad that techs aren't allowed."
    else:
        "People are confused about alliance-run techs."
    
    "Arguments everywhere."
    "@ing leadership."
    "Drama."
    
    menu:
        "Grab popcorn and enjoy the show":
            $ friend_amusement += 15
            
            "This is exactly why you're not playing."
            
            "You sit back and read every message."
            
            "It's glorious."
            
        "Try to calm people down":
            $ friend_engagement += 10
            $ friend_temptation += 5
            
            "You post something diplomatic."
            
            "Some people appreciate it."
            
            "Others tell you to stay out of it."
            "You're not even playing."
            
        "DM your friend to see if they're okay":
            $ friend_engagement += 8
            
            "You check in on [friend_name]."
            
            "\"I'm so tired\""
            
            "You send support."
            "And memes."
    
    jump friend_leadership_stress

label friend_leadership_stress:
    scene bg member_chat
    
    
    "A few days later."
    
    "[friend_name] messages you at 1 AM."
    
    "\"Why did I agree to be HC again?\""
    
    "They're venting."
    "About members."
    "About decisions."
    "About the pressure."
    
    menu:
        "Remind them why they love this":
            $ friend_engagement += 8
            
            "You send a long message."
            "About the good times."
            "The victories."
            "The friendships."
            
            "\"Thanks. I needed that.\""
            
        "Offer to help somehow":
            $ friend_engagement += 5
            $ friend_temptation += 10
            
            "\"Is there anything I can do?\""
            
            "\"Nah, just... thanks for listening.\""
            
            "You feel like maybe you should be doing more."
            
        "Send memes until they laugh":
            $ friend_amusement += 8
            $ friend_engagement += 5
            
            "You flood them with stupid images."
            
            "Eventually:"
            "\"lmaooo okay I feel better\""
            
        "\"This is why I'm not playing\"":
            $ friend_amusement += 3
            $ friend_engagement -= 3
            
            "\"Yeah yeah rub it in\""
            
            "They're joking."
            "Mostly."
    
    jump friend_temptation

label friend_temptation:
    scene bg member_chat
  
    
    "A week before server start."
    
    "[friend_name] messages you."
    
    "\"So... we're a bit short on members.\""
    
    "Here it comes."
    
    "\"Any chance you'd want to join?\""
    
    if friend_temptation > 15:
        "You've been thinking about it."
        "Watching everyone prep."
        "It does look kind of fun."
    else:
        "You knew this was coming."
    
    menu:
        "Hard no - I'm just here to vibe":
            $ friend_temptation = 0
            
            "\"Nah, I'm good. Just here for moral support.\""
            
            "\"Fair enough. Worth a shot.\""
            
            "You remain a spectator."
            
        "Maybe next server?":
            $ friend_temptation += 5
            
            "\"I'm not ready this time.\""
            "\"But maybe next server.\""
            
            "\"I'll hold you to that.\""
            
        "You know what? Actually, I'm interested":
            $ friend_temptation += 20
            
            "Wait."
            
            "Are you actually considering this?"
            
            menu:
                "Yes, sign me up":
                    "\"Really?\""
                    "\"Yeah, why not.\""
                    
                    $ friend_engagement = 100
                    
                    # Note: This would transition to member route
                    # But for pre-server, we'll just acknowledge it
                    
                    "You're in."
                    "No longer a friend."
                    "Now a member."
                    
                    jump friend_now_member
                    
                "On second thought, no":
                    $ friend_temptation -= 5
                    
                    "\"Actually, nevermind.\""
                    "\"I'm good as a friend.\""
                    
                    "\"Lol okay\""
    
    jump friend_countdown

label friend_now_member:
    scene bg member_chat
    
    "You just went from spectator to participant."
    
    "That was impulsive."
    
    "[friend_name] is excited."
    "\"This is going to be great!\""
    
    "You get account assignments."
    "Role discussions."
    "Suddenly people expect things from you."
    
    "The vibe has changed."
    
    "You're in it now."
    
    # For pre-server purposes, just acknowledge the change
    # Full member experience would happen during actual server
    
    jump friend_countdown

label friend_countdown:
    scene bg countdown
    
    
    "The countdown appears."
    
    "72 hours until server start."
    
    if friend_temptation >= 20:
        # Joined as member
        "You're actually playing."
        
        "Wild."
        
        "General chat is hyped."
        "You're part of it now."
        
    else:
        # Still a friend
        "You're still just watching."
        
        "General chat gets intense."
        "Final preparations."
        "Hype building."
        
        "You read everything."
        
        if friend_amusement > 60:
            "This has been thoroughly entertaining."
        
        "[friend_name] seems stressed but excited."
    
    jump friend_ending

label friend_ending:
    scene bg countdown
    with fade
    
    if friend_temptation >= 20:
        # Became a member
        "Server starts."
        
        "You're in it."
        
        "For real."
        
        "Your friend is happy you joined."
        
        "Time to see if this was a good idea."
        
    elif friend_engagement > 60:
        # Engaged spectator
        "Server starts."
        
        "You watch Discord light up."
        
        "Reports flowing in."
        "Attacks."
        "Drama already."
        
        "You lean back."
        
        "This is better than TV."
        
        if friend_amusement > 70:
            "You made the right choice."
            "Let them stress."
            "You'll just enjoy the show."
        
    else:
        # Casual observer
        "Server starts."
    
    return
