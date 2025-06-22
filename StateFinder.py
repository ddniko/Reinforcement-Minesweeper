#asdasdasda
#test program

import pyautogui as gui
import PIL
from PIL import Image
import cv2 as cv
import numpy as np
import time



rows, cols = (16, 16)
arrCoordinates = [[0 for i in range(cols)] for j in range(rows)]
arrBoard = [[0 for i in range(cols)] for j in range(rows)]



def InitializeBoard():
    Minesweeper = gui.locateOnScreen("minesweeper.png", confidence=0.9)
    i = 0
    for pos in gui.locateAllOnScreen("field.png", grayscale=True, region=(Minesweeper), confidence=0.9):
        # print(f"{pos} + {i}")
        columb = i / cols
        # print(f"{int(columb)} + {i%rows}")

        arrCoordinates[int(columb)][i % rows] = pos
        arrBoard[int(columb)][i % rows] = "O"

        i = i + 1
    print(gui.pixel(int(arrCoordinates[1][0][0]), int(arrCoordinates[1][0][1])))
    global ColorBlank
    ColorBlank = gui.pixel(int(arrCoordinates[1][0][0]), int(arrCoordinates[1][0][1]))


def UpdateBoard():
    print("New Board loading")
    i = 0
    for row in arrBoard:
        columb = i / cols
        for col in row:
            if gui.pixel(int(arrCoordinates[int(columb)][i % rows][0]), int(arrCoordinates[int(columb)][i % rows][1])) != ColorBlank:
                arrBoard[int(columb)][i % rows] = 0
        print(row)
    i = i + 1
    #opdatere ikke ordentligt, tjekker ikke ordentligt array igennem





def GetBoard():
    for row in arrCoordinates:
        print(row)
