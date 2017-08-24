#! /usr/bin/python3
# This came from: https://kivy.org/docs/tutorials/crashcourse.html

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
# Well that looks like all of them.
#
# Perhaps I should use the same approach as I did for the Python Think like a
# Computer Scientist where numerous .py files focused on that section number.
# Perhaps video1.py, video2.py, ...

# Could I use main.py to be the menu to video1.py ... video14.py?
# TODO; How do I implement the switch/case statment in python?
# https://www.pydanny.com/why-doesnt-python-have-switch-case.html
def video1():
    print ("Video 1")
def video2():
    print ("Video 2")
def video3():
    print ("Video 3")
def video4():
    print ("Video 4")
def video5():
    print ("Video 5")
def video6():
    print ("Video 6")
def video7():
    print ("Video 7")
def video8():
    print ("Video 8")
def video9():
    print ("Video 9")
def video10():
    print ("Video 10")
def video11():
    print ("Video 11")
def video12():
    print ("Video 12")
def video13():
    print ("Video 13")
def video14():
    print ("Video 14")

# TODO; if 1 execute video1.py, ... 14
def numbers_to_functions_to_strings(argument):
    switcher = {1 : video1,
              2 : video2,
              3 : video3,
              4 : video4,
              5 : video5,
              6 : video6,
              7 : video7,
              8 : video8,
              9 : video9,
              10 : video10,
              11 : video11,
              12 : video12,
              13 : video13,
              14 : video14,
              }
    func = switcher.get(argument,lambda:"nothing")
    func()

# TODO; display video 1 .. video 14 menu
print(videos)
# TODO; user input 1 .. 14
item = input("From the list above: ")
print("You selected item '" + str(item) + "'.")
# TODO; error check what integer 1 .. 14 was entered.
results = numbers_to_functions_to_strings(item)
# TODO; allow some way to specify multiples (1 3 9) or (all)?
pass
