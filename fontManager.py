import libtcodpy as libtcod
import os, fnmatch

def getFont():
    path = "./fonts/"
    fonts = populateFontMenu(path)
    showMenu(fonts)
    index = getFontIndex(fonts)
    return path + fonts[index]

def populateFontMenu(path):
    fonts = {}
    index = 1
    listOfFiles = os.listdir(path)
    pattern = "*.png"
    for entry in listOfFiles:
        if (fnmatch.fnmatch(entry, pattern)):
            fonts[str(index)] = entry
            index += 1
    return fonts

def showMenu(fonts):
    print("List of available options: ")
    print(" ")
    for key in fonts:
        print("[{0}] {1}".format(key, fonts[key]))
    print(" ")

def getFontIndex(fonts):
    index = input("Please select one font by typing the desired number: ")
    while not index in fonts:
        index = input("Option not available. Please select one font by typing the desired number: ")
    return index
