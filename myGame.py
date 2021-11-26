import textgamelib as lib
import time

lib.clearConsole()

#Challenge 1 ----------------------------

lib.printDivider("-",10)
print("Jabari stands on the slippery deck of the pool with his father behind him, eager to play.")
time.sleep(1)
print("Some other children play in the kiddie pool to his left.")
time.sleep(1)
print("The main pool stands in front of him.")
time.sleep(1)
lib.printDivider("-",10)
print("Options: left, forward")
lib.printDivider("-",10)
allowDadCounter = 0
repeatCounter = 0
chooseAgain = 'True'
while chooseAgain == "True":
    actionCounter = 0
    jabariAction = input().lower()
    jabariActionList = jabariAction.split()
    if 'left' in jabariActionList:
        actionCounter += 1
    if 'forward' in jabariActionList:
        actionCounter += 1
    if 'backwards' in jabariActionList:
        actionCounter += 1

    if actionCounter >= 2:
        lib.printDivider("-",10)
        print("Too many arguments.\nTry again.")
        lib.printDivider("-",10)
        actionCounter == 0
    elif "left" in jabariAction:
        lib.printDivider("-",10)
        if repeatCounter == 0:
            print("Jabari goes and plays with the other children in the kiddie pool for a while.")
        else:
            print("Jabari goes and plays with the children in the kiddie pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Choose another option: left, forward")
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Choose another option: forward, backwards")
        lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"
    elif "forward" in jabariAction:
        lib.printDivider("-",10)
        if repeatCounter == 0:
            print("Jabari goes and plays around in the main pool, swimming around the place.")
        else:
            print("Jabari goes and swims in the main pool some more.")
        time.sleep(1)
        allowDadCounter += 1
        if allowDadCounter == 1:
            print("Jabari is slightly tired, but wishes to play some more.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Choose another option: left, forward")
        else:
            print("Jabari feels slightly bored. Maybe he should ask his father about what to do next.")
            time.sleep(1)
            lib.printDivider("-",10)
            print("Choose another option: left, backwards")
            lib.printDivider("-",10)
        actionCounter == 0
        repeatCounter += 1
        chooseAgain = "True"
    elif allowDadCounter == 2 and "backwards" in jabariAction:
        lib.printDivider("-",10)
        print("Jabari runs back towards his father, and he insists that Jabari should try something new.")
        lib.printDivider("-",10)
        actionCounter == 0
        chooseAgain = "False"
    else:
        lib.printDivider("-",10)
        print("I don't recognize those words,\nTry again.")
        lib.printDivider("-",10)

#----------------------------------------

#Challenge 2 ----------------------------
