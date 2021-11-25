import textgamelib as lib
import time

lib.clearConsole()

#Challenge 1 ----------------------------

lib.printDivider("-",10)
print("Jabari stands on the slippery deck of the pool.\nIn front of him stands a tall diving board.\nTo his left, three children his age are playing together in the water.\nHis dad stands behind him, smiling encouragingly.\nWhat will he do?")
lib.printDivider("-",10)
print("Options: Go left, Go forward, Go backwards")
lib.printDivider("-",10)
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
        print("Jabari goes towards the children, but they all glare at him coldly.\nChoose another option: (Forward, Backwards)")
        lib.printDivider("-",10)
        actionCounter == 0
    elif "forward" in jabariAction:
        lib.printDivider("-",10)
        print("Jabari awkwardly climbs on top of the diving board, and decides to take a leap of faith.")
        lib.printDivider("-",10)
        actionCounter == 0
        chooseAgain = "False"
    elif "backwards" in jabariAction:
        lib.printDivider("-",10)
        print("Jabari runs back towards his father, but he insists that he should try something new.\nChoose another option: (Left, Forward)")
        lib.printDivider("-",10)
        actionCounter == 0
    else:
        lib.printDivider("-",10)
        print("I don't recognize those words,\nTry again.")
        lib.printDivider("-",10)

#----------------------------------------

#Challenge 2 ----------------------------
