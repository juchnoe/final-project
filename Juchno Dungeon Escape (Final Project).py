import turtle as d

def waking_up():
    print("You awake in a dark room, locked behind bars. Find a way out.")
    print("You look around, and examine your options:")
    while True:
        response = input("1. Try to open door\n2. Check the floor of the room\n3. Call for help\n4. Go back to sleep\n")
        if response == "1":
            opendoor()
            break
        elif response == "2":
            checkfloor()
            break
        elif response == "3":
            callforhelp()
            break
        elif response == "4":
            backtosleep()
            break
        else:
            print("Please enter a valid response.")

def opendoor():
    print("You approach the metal door and try to push it open, it doesn't budge. It is most certainly locked.")
    while True:
        response = input("1. Check the floor of the room\n2. Call for help\n3. Go back to sleep\n")
        if response == "1":
            checkfloor()
            break
        elif response == "2":
            callforhelp()
            break
        elif response == "3":
            backtosleep()
            break
        else:
            print("Please enter a valid response.")

def checkfloor():
    print("You feel around along the floor until you come across some small strips of metal. Perhaps this can be useful.")
    while True:
        response = input("1. Try to open door\n2. Go back to sleep\n")
        if response == "1":
            unlockdoor()
            break
        elif response == "2":
            backtosleep()
            break
        else:
            print("Please enter a valid response.")

def unlockdoor():
    import random
    print("You fiddle around with the metal pieces in the lock...")
    x = True
    while x:
        inp = input("Roll two dice to see if you can pick the lock. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 8:
                doorhasopened()
                x = False
                break
            else:
                inp = input("It's not working, let's try again. (Enter '1' to roll)\n")
                continue
        else:
            print("Please enter a valid response.")

def doorhasopened():
    print("It worked!")
    print("The door unlocks and you open it cautiously.")
    print("You now proceed down the dark hall and reach an intersection.")
    intersectionturtle()
    input("Enter anything to examine your options.\n")
    print("To the left you see a faint light flickering along the wall, perhaps a fire?")
    print("To the right, you hear a slight rumble in the floor.")
    while True:
        response = input("1. Go left\n2. Go right\n")
        if response == "1":
            goleft()
            break
        elif response == "2":
            goright()
            break
        else:
            print("Please enter a valid response.")

def intersectionturtle():
    wn = d.Screen()
    wn.bgcolor("black")
    d.color("white")
    d.speed(11)
    d.pensize(8)
    d.up()
    d.right(90)
    d.fd(300)
    d.left(270)
    d.fd(150)
    d.right(90)
    d.down()
    d.fd(400)
    d.up()
    d.bk(400)
    d.right(90)
    d.fd(300)
    d.left(90)
    d.down()
    d.fd(400)
    d.right(90)
    d.fd(400)
    d.left(90)
    d.up()
    d.fd(300)
    d.down()
    d.left(90)
    d.fd(1100)
    d.up()
    d.left(90)
    d.fd(300)
    d.left(90)
    d.down()
    d.fd(400)
    d.up()
    d.fd(150)
    d.left(90)
    d.bk(60)
    d.shapesize(3,3,3)
    o = input("Enter anything to continue:\n")
    if o == "":
        d.clear()
        d.hideturtle()
        d.reset()

def callforhelp():
    print("You call out into the darkness. You hear only the echo of your voice.")
    while True:
        response = input("1. Try to open door\n2. Check the floor of the room\n3. Go back to sleep\n")
        if response == "1":
            opendoor()
            break
        elif response == "2":
            checkfloor()
            break
        elif response == "3":
            backtosleep()
            break
        else:
            print("Please enter a valid response.")

def backtosleep():
    print("You go back to sleep.")
    print("An unspecified amount of time later...")
    waking_up()

def goleft():
    print("You go left.")
    print("As you proceed down the hallway, you gradually approach the flickering light.")
    print("Along the way you trip on a piece of jewelry, do you pick it up?")
    while True:
        response = input("1. Pick up jewelry\n2. Ignore\n")
        if response == "1":
            pickedupjewelry()
            break
        elif response == "2":
            ignoredjewelry()
            break
        else:
            print("Please enter a valid response.")

def ignoredjewelry():
    print("You choose NOT to pick up the jewelry.")
    print("As you continue down the hall towards the light, you slowly see that there is a fire burning.")
    print("Around the fire are what appear to be two humanoid figures.")
    print("As you approach you realize these are not regular humans, however, but seemingly goblins.")
    print("They quickly notice you and call out. Soon enough they come to a stand and approach you.")
    print("They question your purpose.")
    while True:
        response = input("1. Attempt to persuade them to let you pass\n2. Tell them to leave you alone\n")
        if response == "1":
            persuade2()
            break
        elif response == "2":
            fight()
            break
        else:
            print("Please enter a valid response.")

def pickedupjewelry():
    print("You hold onto the jewelry.")
    print("As you continue down the hall towards the light, you slowly see that there is a fire burning.")
    print("Around the fire are what appear to be two humanoid figures.")
    print("As you approach you realize these are not regular humans, however, but seemingly goblins.")
    print("They quickly notice you and call out. Soon enough they come to a stand and approach you.")
    print("They question your purpose.")
    while True:
        response = input("1. Attempt to persuade them to let you pass\n2. Offer jewelry as a bribe\n3. Tell them to leave you alone\n")
        if response == "1":
            persuade()
            break
        elif response == "2":
            offerjewelry()
            break
        elif response == "3":
            fight()
            break
        else:
            print("Please enter a valid response.")

def persuade():
    import random
    print("You attempt to persuade the goblins.")
    x = True
    while x:
        inp = input("Roll two dice to determine your ability to persuade. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                persuasionhigh()
                x = False
                break
            elif 10 > doubleroll >= 6:
                persuasionmid()
                x = False
                break
            else:
                fight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def persuade2():
    import random
    print("You attempt to persuade the goblins.")
    x = True
    while x:
        inp = input("Roll two dice to determine your ability to persuade. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                persuasionhigh()
                x = False
                break
            elif 10 > doubleroll >= 6:
                persuasionmid2()
                x = False
                break
            else:
                fight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def persuasionhigh():
    print("Surprised by your ability to speak so well, the goblins back down and let you go on your way.")
    print("That was close, that might not have gone so well...")
    print("You continue down the hall until the flicker of the fire grows more and more faint behind you.")
    continuepastgoblins()

def persuasionmid():
    print("The goblins consider letting you pass, however, perhaps you can offer them something to forget about this interaction...")
    while True:
        response = input("1. Offer jewelry\n2. Offer nothing\n")
        if response == "1":
            offerjewelry()
            break
        elif response == "2":
            fight()
            break
        else:
            print("Please enter a valid response.")

def persuasionmid2():
    print("The goblins consider letting you pass if you can offer them something of interest.")
    print("You check your pockets, however, to find nothing...")
    print("The goblins don't look very pleased and ask more directly to pay up whatever you have.")
    while True:
        response = input("1. Offer nothing\n2. Attempt to run\n")
        if response == "1":
            fight()
            break
        elif response == "2":
            run()
            break
        else:
            print("Please enter a valid response.")

def run():
    import random
    x = True
    while x:
        inp = input("Roll a die to determine your athletic ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 5:
                runsuccess()
                x = False
                break
            else:
                runfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def runsuccess():
    print("With your quick speed and agility, you out maneuver the goblins and slip past them!")
    print("You sprint down the hall until you can't see the flicker of the fire any longer. You have escaped.")
    continuepastgoblins()

def runfailure():
    print("You attempt to slip past the two goblins but are immediately stopped.")
    fight()

def offerjewelry():
    print("You offer the jewelry you picked up to the two goblins.")
    print("They look in interest at what you show them.")
    print("Seemingly satisfied enough, they gladly take the bribe and tell you to get lost.")
    print("Afraid to push them further, you continue down the hall until the flicker of the fire grows more faint behind you.")
    continuepastgoblins()

def fight():
    import random
    print("The two goblins do not seem amused at your decision.")
    print("They begin to get increasingly aggressive as they push you around, there may not be an easy way out of this...")
    x = True
    while x:
        inp = input("Roll two dice to determine your fighting ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 9:
                winfighteasy()
                x = False
                break
            elif 9 > doubleroll >= 2:
                winfighthard()
                x = False
                break
            else:
                losefight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def winfighteasy():
    print("You take a fighting stance and hold your ground.")
    print("You exchange hits with the two goblins and fight them off.")
    print("After going back and forth, both of them are knocked unconscious while you remain in decent shape.")
    print("Lucky to have beaten them so easily, you proceed on down the hallway.")
    continuepastgoblins()

def winfighthard():
    import random
    print("You take a fighting stance and hold your ground.")
    print("You exchange hits with the two goblins and attempt to fight them off.")
    print("You are knocked on the ground and attacked by the two of them.")
    x = True
    while x:
        inp = input("Roll a die to determine your hit back. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll >= 5:
                hitbackhard()
                x = False
                break
            elif 5 > roll >= 3:
                hitbackmid()
                x = False
                break
            else:
                losefight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def hitbackhard():
    print("With all your strength you kick the goblins off of you and knock them both unconscious.")
    print("You aren't in the best of shape but you make it out alive.")
    print("Lucky to have survived that situation, you proceed on down the hallway.")
    continuepastgoblins()

def hitbackmid():
    print("With all your strength you kick the goblins off of you.")
    print("They continue to fight back but you overpower them just enough.")
    print("Wounded and growing exhausted, the goblins eventually step back and tell you to get lost.")
    print("You aren't in the best of shape but you manage to escape the situation.")
    print("You quickly continue down the hallway before they change their minds.")
    continuepastgoblins()

def losefight():
    print("You are suddenly knocked unconscious...")
    print("An unspecified amount of time later...")
    waking_up()

def goright():
    print("You choose to go right.")
    print("As you continue down the hallway, the booming noise of what sounds to be footsteps gradually grows more prominent.")
    print("Not far ahead you spot what appears to be a small window along the stone wall.")
    print("This window, however is both quite high up and rather small.")
    print("You aren't even sure if a person could fit through it.")
    print("As you approach the window, the rumbling footsteps are worryingly close, perhaps staying quiet could help the situation...")
    while True:
        response = input("1. Try to escape via window\n2. Continue on past the footsteps\n")
        if response == "1":
            inspectwindow()
            break
        elif response == "2":
            sneakpastfootsteps()
            break
        else:
            print("Please enter a valid response.")

def sneakpastfootsteps():
    import random
    print("You decide to try sneaking past the loud footsteps in the near darkness.")
    x = True
    while x:
        inp = input("Roll two dice to determine your stealth ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                sneakpasthigh()
                x = False
                break
            else:
                sneakpastlow()
                x = False
                break
        else:
            print("Please enter a valid response.")

def sneakpasthigh():
    print("Being very cautious of your movement, you sneak past rather silently.")
    print("The footsteps grow quieter in the distance as you continuously advance further ahead.")
    continuepastfootsteps()

def sneakpastlow():
    print("You attempt to sneak past the footsteps as quietly as you can.")
    print("In the process, you slip up and trip over a chain, echoing a loud sound around the room.")
    print("The footsteps suddenly come to a halt as you do as well.")
    while True:
        response = input("1. Continue sneaking past\n")
        if response == "1":
            sneakpastlow2()
            break
        else:
            print("Please enter a valid response.")

def sneakpastlow2():
    import random
    print("After minutes of silence, you proceed on once more...")
    x = True
    while x:
        inp = input("Roll two dice to determine your stealth once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                sneakpastsuccess()
                x = False
                break
            else:
                sneakpastfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def sneakpastsuccess():
    print("Being more cautious than you were initially, you manage to continue on past whatever lurked in the darkness.")
    print("You manage to successfully sneak past the footsteps.")
    continuepastfootsteps()

def sneakpastfailure():
    print("You attempt once more to sneak past but are not very successful...")
    print("Your feet make noticeable noise as you attempt to remain silent.")
    print("The footsteps start back up again and grow rapidly more louder, it seems like you've been found...")
    while True:
        response = input("1. Run down hallway\n2. Run back to window\n3. Do nothing\n")
        if response == "1":
            runhallway()
            break
        elif response == "2":
            runwindow()
            break
        elif response == "3":
            donothing()
            break
        else:
            print("Please enter a valid response.")

def runwindow():
    print("You make a break back to the window with the hope that you can quickly escape!")
    print("You make it to the base of the wall, but the window is too high!")
    print("You must decide fast!")
    while True:
        response = input("1. Attempt to escape via window\n2. Run down hallway\n3. Do nothing\n")
        if response == "1":
            runwindowescape()
            break
        elif response == "2":
            runhallway()
            break
        elif response == "3":
            donothing()
            break
        else:
            print("Please enter a valid response.")

def runwindowescape():
    import random
    x = True
    while x:
        inp = input("Roll a die to determine your climbing ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 5:
                quickclimbsuccess()
                x = False
                break
            else:
                quickclimbfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def quickclimbsuccess():
    print("You scale the wall as fast as you possibly can.")
    print("As you climb up, you can hear something large clawing just below you feet.")
    print("You choose to climb on even faster, not even bothering to look at the creature right under you.")
    print("You attempt to fit through the window...")
    repeatclimbthroughwindow()

def quickclimbfailure():
    import random
    print("You attempt to scale the bricks in the wall as fast as you can!")
    print("In the process, however, your foot slips and you fall back down to the floor.")
    x = True
    while x:
        inp = input("Roll a die to determine your climbing ability once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 5:
                finalwindowescapesuccess()
                x = False
                break
            else:
                finalwindowescapefailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def finalwindowescapesuccess():
    print("Quickly jumping back to your feet, you attempt to scale the wall once more, this time even faster!")
    print("As you climb up, you can hear something large clawing just below you feet.")
    print("You choose to climb on as fast as possible, not even bothering to look at the creature right under you.")
    print("You attempt to fit through the window...")
    repeatclimbthroughwindow()

def repeatclimbthroughwindow():
    import random
    x = True
    while x:
        inp = input("Roll two dice to see if you can make it through. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 8:
                throughwindowsuccess()
                x = False
                break
            else:
                inp = input("You have trouble fitting through, maybe push a little harder... (Enter '1' to roll)\n")
                continue
        else:
            print("Please enter a valid response.")

def finalwindowescapefailure():
    print("Unable to quickly get back on your feet, you are struck by a blunt force, knocking you unconscious...")
    waking_up()

def donothing():
    print("You choose to do nothing as the booming footsteps rapidly approach.")
    print("You are suddenly hit by a large blunt force and throw to the ground, knocking you unconscious...")
    waking_up()

def runhallway():
    import random
    print("You suddenly sprint forward, away from the sound!")
    x = True
    while x:
        inp = input("Roll a die to determine your agility. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll >= 4:
                runhallwaysucess()
                x = False
                break
            else:
                runhallwayfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def runhallwaysucess():
    print("Running as fast as you can, you escape into the darkness ahead.")
    print("Whatever was behind you has seemed to have lost interest.")
    continuepastfootsteps()

def runhallwayfailure():
    import random
    print("You run as fast as you can, but the footsteps still grow closer!")
    print("Suddenly, you are knocked on the ground by a blunt force!")
    x = True
    while x:
        inp = input("Roll a die to determine your agility once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll >= 5:
                runhallwayp2success()
                x = False
                break
            else:
                runhallwayp2failure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def runhallwayp2success():
    print("You get up from the floor as fast as you can and continue running.")
    print("You are likely injured but you don't seem to care at this very moment.")
    print("You sprint forward, evading whatever else is thrown at you.")
    print("You manage to escape.")
    continuepastfootsteps()

def runhallwayp2failure():
    print("You get up from the floor as fast as you can and continue running.")
    print("In the process, however, you trip once more and fall to the ground!")
    print("You are suddenly hit once more by some force you cannot see!")
    print("You slide across the floor and are knocked unconscious...")
    waking_up()

def inspectwindow():
    print("You go to get a closer look at the window.")
    windowturtle()
    print("With a minor light shining in, you can just barely see the immediate area as you look for a way to climb.")
    print("You look around to make out what appears to be an old barrel, with just enough light illuminating it.")
    print("You evaluate your options...")
    while True:
        response = input("1. Try to use barrel to climb (More noise/Easier)\n2. Try to scale stone brick wall (Less noise/Harder)\n3. Continue on past the footsteps\n")
        if response == "1":
            barrel()
            break
        elif response == "2":
            scalewall()
            break
        elif response == "3":
            sneakpastfootsteps()
            break
        else:
            print("Please enter a valid response.")

def scalewall():
    import random
    print("You choose to scale the wall.")
    x = True
    while x:
        inp = input("Roll two dice to determine your climbing ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 11:
                scalewallsuccess()
                x = False
                break
            else:
                scalewallfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def scalewallsuccess():
    print("You climb up the wall quietly.")
    print("You have little issue climbing the bricks and soon reach the top.")
    print("You attempt to fit through the window...")
    repeatclimbthroughwindow()

def scalewallfailure():
    import random
    print("You attempt to scale the wall.")
    print("Halfway up your foot slips and you fall to the floor, making a loud thud.")
    print("You hear the footsteps stop for a moment, then soon resume, getting louder.")
    print("It appears something is approaching...")
    x = True
    while x:
        inp = input("Roll a die to determine your climbing ability once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 5:
                quickclimbsuccess()
                x = False
                break
            else:
                quickclimbfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def windowturtle():
    d.color("white")
    d.speed(11)
    d.pensize(8)
    d.up()
    d.left(90)
    d.fd(300)
    d.left(90)
    d.fd(75)
    d.right(180)
    d.down()

    def filledrectangle(d, l, w):
        d.left(90)
        d.begin_fill()
        for f in range(2):
            d.right(90)
            d.forward(l)
            d.right(90)
            d.forward(w)
        d.end_fill()
        d.right(90)
    filledrectangle(d, 300, 150)
    d.up()
    d.right(90)
    d.fd(750)
    d.right(90)
    d.fd(400)
    d.right(180)
    d.down()
    d.fd(150)
    d.left(45)

    def curve(n):
        d.circle(n, 90)
    curve(200)
    d.left(45)
    d.fd(150)
    d.left(45)
    curve(200)
    d.left(135)
    for i in range(2):
        d.down()
        d.fd(283)
        d.right(90)
        d.up()
        d.fd(50)
        d.right(90)
        d.down()
        d.fd(283)
        d.left(90)
        d.up()
        d.fd(50)
        d.left(90)
    d.fd(50)
    d.left(90)
    d.down()
    d.fd(10)
    d.up()
    d.fd(227)
    d.down()
    d.fd(200)
    d.right(180)
    d.up()
    d.fd(430)
    d.down()
    d.fd(2000)
    o = input("Enter anything to continue:\n")
    if o == "":
        d.clear()
        d.hideturtle()
        d.reset()

def barrel():
    import random
    print("You decide to grab the barrel to assist you in climbing the wall.")
    print("With the footsteps still booming, you quietly approach the barrel.")
    x = True
    while x:
        inp = input("Roll two dice to determine your stealth ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 11:
                stealthhigh()
                x = False
                break
            else:
                stealthlow()
                x = False
                break
        else:
            print("Please enter a valid response.")

def stealthlow():
    print("Attempting to move silently, you push the barrel along the floor.")
    print("Doing so, however, emits a loud sound as it drags across the ground.")
    print("The nearby footsteps come to a halt, leaving the only sound in the room to be the dragging of the barrel.")
    while True:
        response = input("1. Continue pushing barrel\n2. Make a run for the window\n")
        if response == "1":
            continuepushing()
            break
        elif response == "2":
            runwindow2()
            break
        else:
            print("Please enter a valid response.")

def continuepushing():
    import random
    print("After minutes of silence, you proceed on once more...")
    x = True
    while x:
        inp = input("Roll two dice to determine your stealth once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                stealthhigh()
                x = False
                break
            else:
                continuepushingfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def continuepushingfailure():
    print("You attempt to push the barrel once more, but soon after you continue, the footsteps resume.")
    print("They grow both louder and faster, something is surely gaining on you...")
    while True:
        response = input("1. Continue pushing barrel\n2. Make a run for the window\n")
        if response == "1":
            continuepushing2()
            break
        elif response == "2":
            runwindow3()
            break
        else:
            print("Please enter a valid response.")

def continuepushing2():
    import random
    print("You choose to keep pushing the barrel until you reach the base of the wall.")
    print("Suddenly, as you attempt to climb on top of the barrel, you are instantly knocked off by an unknown blunt force!")
    print("You rise from the floor, potentially wounded.")
    print("You try once more to climb on top of the barrel, footsteps just behind you...")
    x = True
    while x:
        inp = input("Roll a die to determine your climbing ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 3:
                barrelclimbsuccess()
                x = False
                break
            else:
                barrelclimbfailure()
                x = False
                break
        else:
            print("Please enter a valid response.")

def barrelclimbsuccess():
    print("You proceed to scale the remaining wall as fast as you possibly can.")
    print("As you climb up, you can hear something large clawing just below you feet.")
    print("You choose to climb on even faster, not even bothering to look at the creature right under you.")
    print("You attempt to fit through the window...")
    repeatclimbthroughwindow()

def barrelclimbfailure():
    print("You climb up once more, perhaps you'll be able to escape!")
    print("With another strong hit, you are knocked down not long after.")
    print("You fall unconscious...")
    waking_up()

def runwindow2():
    print("You suddenly sprint out towards the window, leaving the barrel behind!")
    print("The footsteps resume and grow rapidly louder, something is chasing you...")
    print("You make it to the base of the wall, but the window is too high!")
    runwindowescape()

def runwindow3():
    print("You suddenly sprint out towards the window, leaving the barrel behind!")
    print("You make it to the base of the wall, but the window is too high!")
    runwindowescape()

def stealthhigh():
    import random
    print("Moving very silently, you push the barrel along the floor, cautious of its noise.")
    print("It takes a while to reach the window, but you manage to get the barrel there without alerting whatever lurks in the darkness.")
    x = True
    while x:
        inp = input("Roll a die to determine your climbing ability. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll == 6:
                climbinghigh()
                x = False
                break
            elif 6 > roll >= 3:
                climbingmid()
                x = False
                break
            else:
                climbinglow()
                x = False
                break
        else:
            print("Please enter a valid response.")

def climbinghigh():
    import random
    print("You proceed to climb onto the barrel, once more careful of the noise you make.")
    print("you then scale the remaining portion of the wall to reach the small opening.")
    x = True
    while x:
        inp = input("Roll two dice to see if you can make it through. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 8:
                throughwindowsuccess()
                x = False
                break
            else:
                inp = input("You have trouble fitting through, maybe push a little harder... (Enter '1' to roll)\n")
                continue
        else:
            print("Please enter a valid response.")

def throughwindowsuccess():
    print("With enough force and wiggling, you manage to slip through the window into the light.")
    print("You then fall from the wall onto the dirt below.")
    print("You have absolutely no idea where you might be, but you are now in the bright daylight, out of the dark prison in which you awoke.")
    ending()

def ending():
    print("Congratulations! You have successfully escaped!")
    print("Thank you for playing!")

#------------------------------------------------------------------------

def continuepastfootsteps():
    print("You continue on further into the darkness.")
    print("Suddenly, you hear a loud voice call out behind you to stop!")
    print("You turn around to find what appears to be some sort of guard.")
    print("He now approaches and begins to question you.")
    while True:
        response = input("1. Attempt to persuade\n2. Attempt to fight\n3. Run\n")
        if response == "1":
            guardpersuade()
            break
        elif response == "2":
            guardfight()
            break
        elif response == "3":
            guardrun()
            break
        else:
            print("Please enter a valid response.")

def guardpersuade():
    import random
    print("You attempt to persuade the guard.")
    x = True
    while x:
        inp = input("Roll two dice to determine your ability to persuade. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 10:
                guardpersuasionhigh()
                x = False
                break
            elif 10 > doubleroll >= 6:
                guardpersuasionmid()
                x = False
                break
            else:
                guardfight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def guardpersuasionhigh():
    print("Your persuasion appears to be very effective on the guard, enough so that they point you in the direction of the front gate.")
    while True:
        response = input("1. Proceed to front gate\n")
        if response == "1":
            frontgate()
            break
        else:
            print("Please enter a valid response.")

def guardpersuasionmid():
    print("Your persuasion appears to be mildly effective on the guard, however they are still suspicious.")
    print("You attempt one more time to persuade them.")
    import random
    x = True
    while x:
        inp = input("Roll a die to determine your ability to persuade once more. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            print("Roll: ", roll)
            if roll >= 6:
                guardpersuasionhigh()
                x = False
                break
            else:
                guardfight()
                x = False
                break
        else:
            print("Please enter a valid response.")

def guardfight():
    print("Not very pleased at you, the guard draws his sword and takes a fighting stance.")
    print("Armed with nothing, you make a decision.")
    while True:
        response = input("1. Attempt to fight unarmed\n2. Run\n")
        if response == "1":
            guardfight2()
            break
        elif response == "2":
            guardrun()
            break
        else:
            print("Please enter a valid response.")

def guardrun():
    print("You run off as fast as you can into the darkness, away from the guard.")
    print("That was rather easy...")
    while True:
        response = input("1. Continue on\n")
        if response == "1":
            continuepastgoblins()
            break
        else:
            print("Please enter a valid response.")

def guardfight2():
    import random
    print("You attempt to fight the guard unarmed.")
    x = True
    while x:
        inp = input("Roll two dice to determine your ability to fight. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 11:
                guardfightsuccess()
                x = False
                break
            elif 11 > doubleroll >= 5:
                guardfightmid()
                x = False
                break
            else:
                guardfightlose()
                x = False
                break
        else:
            print("Please enter a valid response.")

def guardfightmid():
    print("The guard swings his sword in your direction but you manage to just barely dodge it, receiving just a scrape.")
    print("Armed with nothing, there is not much you can do to counter their advances.")
    print("He swings again, however you dodge once more.")
    print("He immediately returns back with his arm and hits you with the hilt, knocking you to the floor.")
    import random
    x = True
    while x:
        inp = input("Roll a die to determine your agility. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll >= 4:
                guardfightsuccess2()
                x = False
                break
            else:
                guardfightlose2()
                x = False
                break
        else:
            print("Please enter a valid response.")

def guardfightsuccess2():
    print("You quickly get back up, surprising the guard with your speed.")
    print("You take a stance once more.")
    guardfightsuccess()

def guardfightlose2():
    print("You manage to get back up, but aren't very quick.")
    guardfightlose()

def guardfightsuccess():
    print("The guard swings his sword in your direction but you manage to evade it easily.")
    print("Before they are able to regain their stance, you sweep their legs, knocking them to the ground.")
    print("The sword drops from their hands onto the floor.")
    while True:
        response = input("1. Pick up sword and threaten\n2. Kick sword into the darkness\n")
        if response == "1":
            threaten()
            break
        elif response == "2":
            kicksword()
            break
        else:
            print("Please enter a valid response.")

def kicksword():
    print("You suddenly kick the sword away, sending it sliding far into the darkness of the hall.")
    print("Before the guard can stand and regain themselves, you quickly flee into the darkness...")
    while True:
        response = input("1. Continue on\n")
        if response == "1":
            continuepastgoblins()
            break
        else:
            print("Please enter a valid response.")

def threaten():
    print("You pick up the weapon and point it directly at the guard.")
    print("You then proceed to threaten them to guide you out of this place.")
    print("They accept and stand up.")
    print("The guard, with a sword pointed at their back, points you in the direction of the front gate.")
    while True:
        response = input("1. Proceed to front gate\n")
        if response == "1":
            frontgate()
            break
        else:
            print("Please enter a valid response.")

def frontgate():
    print("You proceed on in the direction of the front gate.")
    print("It takes a while but soon enough you see a light shining in.")
    print("You continue on to find the door partially opened...")
    print("It looks like you've found a way out.")
    print("You step through into the sunlight outside.")
    ending()

def guardfightlose():
    print("The guard swings his sword in your direction, barely wounding you.")
    print("He quickly brings his arm back and simply bonks you on the head with the hilt, knocking you unconscious.")
    print("An unspecified amount of time later...")
    waking_up()

#------------------------------------------------------------------------

def continuepastgoblins():
    print("You continue on, further into the darkness...")
    print("Soon enough, you hear a faint voice whisper out to you.")
    print("You look around to find nothing, however.")
    print("Suddenly, you feel a hand on your shoulder. You look over to see a mysterious individual wearing a cloak.")
    while True:
        response = input("1. Calmly question who he is\n2. Take a fighting stance\n")
        if response == "1":
            calmlyquestion()
            break
        elif response == "2":
            fightingstance()
            break
        else:
            print("Please enter a valid response.")

def fightingstance():
    print("You jump back into a fighting stance in front of the man.")
    print("He looks at you in disappointment, telling you that he will not fight you.")
    print("You return to a normal standing position as he then offers you a chance to escape, if you can trust him.")
    print("Do you decide to trust the man?")
    while True:
        response = input("1. Trust him\n2. Don't trust him\n")
        if response == "1":
            trust()
            break
        elif response == "2":
            dont_trust()
            break
        else:
            print("Please enter a valid response.")

def calmlyquestion():
    print("You ask questions to the mysterious man, however, you receive no real answer in return.")
    print("He offers you a chance to escape this place, if you trust him...")
    print("Do you decide to trust the man?")
    while True:
        response = input("1. Trust him\n2. Don't trust him\n")
        if response == "1":
            trust()
            break
        elif response == "2":
            dont_trust()
            break
        else:
            print("Please enter a valid response.")

def dont_trust():
    print("You choose not to trust the mysterious individual.")
    print("Looking rather displeased with your decision, he offers you one more chance to trust him.")
    print("Do you decide to trust the man?")
    while True:
        response = input("1. Trust him\n2. Don't trust him\n")
        if response == "1":
            trust2()
            break
        elif response == "2":
            dont_trust2()
            break
        else:
            print("Please enter a valid response.")

def dont_trust2():
    print("You decide once more not to trust the mysterious individual, angering him.")
    print("Saying nothing, he walks back into the darkness, leaving you alone once more.")
    while True:
        response = input("1. Continue on\n")
        if response == "1":
            caughtbyguards()
            break
        else:
            print("Please enter a valid response.")

def caughtbyguards():
    print("You continue to walk on but not long after, you hear the sound of several footsteps and the clanking of armor approaching your direction.")
    print("You soon enough find yourself surrounded by four guards, threatening you.")
    while True:
        response = input("1. Attempt to persuade the guards\n2. Surrender\n")
        if response == "1":
            guards_persuade()
            break
        elif response == "2":
            surrender()
            break
        else:
            print("Please enter a valid response.")

def surrender():
    print("You surrender to the guards and they proceed to grab you and take you away into the darkness.")
    print("They soon enough throw you onto a prison cell floor.")
    print("As time passes, you grow continually more tired until you pass out.")
    print("An unspecified amount of time later...")
    waking_up()

def guards_persuade():
    import random
    x = True
    while x:
        inp = input("Roll a die to determine your ability to persuade. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll >= 5:
                guardS_persuasion_high()
                x = False
                break
            else:
                guardS_persuasion_low()
                x = False
                break
        else:
            print("Please enter a valid response.")

def guardS_persuasion_low():
    print("You attempt to persuade the four guards, but fail in your attempt.")
    print("The displeased guards look at you in disappointment and proceed to grab you, taking you away into the darkness.")
    print("They soon enough throw you onto a prison cell floor.")
    print("As time passes, you grow continually more tired until you pass out.")
    print("An unspecified amount of time later...")
    waking_up()

def guardS_persuasion_high():
    print("You attempt to persuade the four guards, and seem to be rather successful.")
    print("The guards no longer seem to be suspicious of you and proceed to point you in the direction of the front gate, believing this to be some kind of misunderstanding.")
    frontgate()

def trust2():
    print("You decide to trust the mysterious individual.")
    print("He angrily tells you to follow him.")
    print("You follow as he guides you into the darkness...")
    print("Soon enough, you lose track of the man, finding yourself alone once more.")
    while True:
        response = input("1. Continue on\n")
        if response == "1":
            badendingmsyteriousman()
            break
        else:
            print("Please enter a valid response.")

def badendingmsyteriousman():
    print("You continue on into the darkness, but are suddenly struck in the head by an unknown object.")
    print("You fall to the floor unconscious.")
    print("An unspecified amount of time later...")
    waking_up()

def trust():
    print("You decide to trust the mysterious individual.")
    print("He looks pleased with this decision and tells you to follow him.")
    print("You follow as he guides you into the darkness...")
    print("Soon enough, you lose track of the man, finding yourself alone once more.")
    while True:
        response = input("1. Continue on\n")
        if response == "1":
            holeinwall()
            break
        else:
            print("Please enter a valid response.")

def holeinwall():
    print("You proceed onwards, not having any idea where you are.")
    print("You see a shimmer of light, barely shining in, perhaps this is a way out?")
    print("Your approach the source of the light to find a hole in the stone wall.")
    print("A chunk of bricks have been knocked out onto the ground, leaving enough room to perhaps fit through...")
    print("You try to squeeze through.")
    fitting_through_hole()

def fitting_through_hole():
    import random
    x = True
    while x:
        inp = input("Roll two dice to see if you can make it through. (Enter '1' to roll)\n")
        while inp == "1":
            roll = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            doubleroll = roll + roll2
            print("Roll: ", doubleroll)
            if doubleroll >= 8:
                through_hole_success()
                x = False
                break
            else:
                inp = input("You have trouble fitting through, maybe push a little harder... (Enter '1' to roll)\n")
                continue
        else:
            print("Please enter a valid response.")

def through_hole_success():
    print("With enough force and wiggling, you manage to slip through the small hole into the light.")
    print("You fall onto the dirt below.")
    print("You have absolutely no idea where you might be, but you are now in the bright daylight, out of the dark prison in which you awoke.")
    ending()

#---------------------------------------------------


waking_up()
