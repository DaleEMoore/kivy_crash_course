#! /usr/bin/python3
# This came from: https://kivy.org/docs/tutorials/crashcourse.html

__author__ = "DaleEMoore@gMail.Com"
__version__ = "0.2" # TODO; increment this thing frequently; or automatically.

# Dale's plan. Start here https://github.com/inclement/kivycrashcourse and
# follow the Videos for each section. The sections I'd like to cover first:
videos = """
Video 1: Making a simple app - https://www.youtube.com/watch?v=F7UKmK9eQLY
Video 2: Building an android apk - https://www.youtube.com/watch?v=t8N_8WkALdE
Video 3: More interesting widget interactions - https://www.youtube.com/watch?v=-NvpKDReKyg
Video 4: Kivy language - https://www.youtube.com/watch?v=ZVWAKzR63ig
Video 5: Mixing python and kivy language - https://www.youtube.com/watch?v=ZmteLworB4E
Video 6: Kivy properties - https://www.youtube.com/watch?v=OkW-1uzP5Og
Video 7: Drawing on the canvas - https://www.youtube.com/watch?v=1d709erhpdQ
Video 8: Let's fix some bugs - https://www.youtube.com/watch?v=2Gc8iYJQ_qk
Video 9: Creating a scrollable label - https://www.youtube.com/watch?v=WdcUg_rX2fM
Video 10: Thinking about layouts - https://www.youtube.com/watch?v=0n8Rar3CgdI
Video 11: Animation and the Clock - https://www.youtube.com/watch?v=ChmfVOu9aIc&feature=youtu.be
Video 12: Using Android APIs - https://www.youtube.com/watch?v=8Jwp1PTvECI&feature=youtu.be
Video 13: Using Kivy's settings panel - https://www.youtube.com/watch?v=oQdGWeN51EE
Video 14: Using a ScreenManager - https://www.youtube.com/watch?v=xx-NLOg6x8o
"""

heading = "kivy_crash_course version " + __version__ \
    + " by " + __author__ \
    + "\n" + videos

# Well that looks like all of them.
#
# Perhaps I should use the same approach as I did for the Python Think like a
# Computer Scientist where numerous .py files focused on that section number.
# Perhaps video1.py, video2.py, ...

# Could I use main.py to be the menu to video1.py ... video14.py?
# https://www.pydanny.com/why-doesnt-python-have-switch-case.html
def video1():
    print ("Video 1")
    import video1
    video1.main()
    return 1
def video2():
    print ("Video 2")
    import video2
    video2.main()
    return 2
def video3():
    print ("Video 3")
    return 3
def video4():
    print ("Video 4")
    return 4
def video5():
    print ("Video 5")
    return 5
def video6():
    print ("Video 6")
    return 6
def video7():
    print ("Video 7")
    return 7
def video8():
    print ("Video 8")
    return 8
def video9():
    print ("Video 9")
    return 9
def video10():
    print ("Video 10")
    return 10
def video11():
    print ("Video 11")
    return 11
def video12():
    print ("Video 12")
    return 12
def video13():
    print ("Video 13")
    return 13
def video14():
    print ("Video 14")
    return 14

# display video 1 .. video 14 menu
print(heading)
while True:
    # user input 1 .. 14
    # why does this not allow me to enter the value "1"? Well - it does now. I wonder what happened those 24 hours?
    # TODO; can't I do some fancy entry using kivy here?
    item = input("From the list above, Videos to re-display or eXit to leave: ")
    print("You selected item '" + str(item) + "'.")
    # error check what integer 1 .. 14 was entered.
    results = ''
    # See the switch/case statment in python, if x: y() elif: z: ...
    if item == 'V' or item == 'v':
        print(videos)
    elif item == 'X' or item == 'x':
        print("eXit requested.")
        exit()
    elif item == str(1):
        results =video1()
    elif item == str(2):
        results =video2()
    elif item == str(3):
        results =video3()
    elif item == str(4):
        results =video4()
    elif item == str(5):
        results =video5()
    elif item == str(6):
        results =video6()
    elif item == str(7):
        results =video7()
    elif item == str(8):
        results =video8()
    elif item == str(9):
        results =video9()
    elif item == str(10):
        results =video10()
    elif item == str(11):
        results =video11()
    elif item == str(12):
        results =video12()
    elif item == str(13):
        results =video13()
    elif item == str(14):
        results =video14()
    else:
        print("You entered '" + str(item) + "' and I don't understand that!")

    #results = numbers_to_functions_to_strings(item)
    print("Results: " + str(results))
    # TODO; allow some way to specify multiples (1 3 9) or (all)?
    pass
